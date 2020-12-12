from pytube import YouTube
import pandas as pd
from ..common.utils import *
import re

def getSourceDataFrameSingle(p_url):
    return getSourceDataFrame([p_url])

# 하나 이상의 유튜브 영상에 대한 한글 혹은 영문 자막을 가져와 DataFrame 형태로 리턴
# input: url 리스트
# output: 유튜브 영상 정보 및 자막을 저장하고 있는 DataFrame(테이블 형식)
def getSourceDataFrame(p_url_list):
    # TP에서 필요로 하는 정보는 'id'와 'content'이고 나머지는 유튜브 영상 정보 및 유튜브 영상 분석 대상을 표시하는 열('chk_ko_en')
    src_df = pd.DataFrame(columns=['id', 'title', 'author', 'url', 'chk_ko_en', 'content', 'ret'])
    # input url 리스트에서 각 url별로 for loop을 돌면서 각 영상별로 분석 대상인지 확인 후 자막 수집
    for u_idx, url in enumerate(p_url_list):
        # 현재는 id를 url 리스트의 순서로 제공. 추후 변경 가능 (예. 유튜브 url 내 고유 id 혹은 이 id와 날짜와의 결합 등)
        tmp_id = u_idx
        # url의 유튜브 객체 생성
        yt = YouTube(url)
        # http 부분을 제외한 www 이하 url
        tmp_url = re.sub(r'(http[s]?:/{1,2})(.*)', '\\2', url)
        # 해당 유튜브 영상의 제목
        tmp_title = yt.title
        # 해당 유튜브 영상의 제작자
        tmp_author = yt.author
        # 한글, 영어, 영어(자동 생성) 자막의 유무를 표시하기 위한 플래그
        tmp_chk_cap = False
        # 유튜브 자막 string default값
        tmp_content = ''
        tmp_row = [tmp_id, tmp_title, tmp_author, tmp_url]
        # caption_lang_list는 영상 내 어떤 자막이 있는지 저장하고 있는 리스트
        caption_lang_list = yt.caption_tracks
        # caption_lang_str_list는 위 caption_lang_list의 값을 str()변환한 값을 저장하고 있는 리스트
        caption_lang_str_list = [str(language) for language in caption_lang_list]
        # 영상 내 어떠한 언어인지 관계 없이 '자막' 자체가 있는지에 따라 진행
        # 만약 영상 내 무엇이든 '자막'이 있다면
        if caption_lang_str_list:
            cap_ko = '<Caption lang="한국어" code="ko">'
            cap_en = '<Caption lang="영어" code="en">'
            cap_en_auto = '<Caption lang="영어 (자동 생성됨)" code="en">'
            # 타겟 자막 리스트
            cap_ko_en_list = [cap_ko, cap_en, cap_en_auto]
            cap_pat = re.compile(r'(?<=code=["])(\w+)')
            # # 언어의 중복 제거. 즉, 고유한 code만 저장하고 있는 리스트
            # tmp_cap_list = []
            # for cap_lang_str in caption_lang_str_list:
            #     cap_pat_search = cap_pat.search(cap_lang_str)
            #     if cap_pat_search:
            #         cap_pat_search_ret = cap_pat_search.group()
            #         if cap_pat_search_ret not in tmp_cap_list:
            #             tmp_cap_list.append(cap_pat_search_ret)
            # 한국어, 영어, 그리고 영어(자동생성) 순으로 for loop을 돌면서 자막 유무를 확인
            for cap_lang in cap_ko_en_list:
                # 만약 해당 언어(예. 한국어)가 해당 영상의 자막 리스트에 있다면
                if cap_lang in caption_lang_str_list:
                    # 해당 언어의 인덱스 값 가져오기. 영상의 자막을 generate_srt_captions()로 가져오기 위해
                    l_idx = caption_lang_str_list.index(cap_lang)
                    # generate_str_captions()로 자막 가져오기
                    raw_text = caption_lang_list[l_idx].generate_srt_captions()
                    # regex를 활용해 텍스트 전처리
                    tmp_content = getRegexScript(raw_text)
                    # tmp_content = raw_text
                    # 자막이 있으므로 플래그를 True로 할당
                    tmp_chk_cap = True
                    # ret = f"{cap_lang} is available among {', '.join(tmp_cap_list)} captions in this video url ({tmp_url}) [{tmp_title[:10] + '...'}]"
                    ret = f"{cap_lang} is available in this video url ({tmp_url}) [{tmp_title[:10] + '...'}]"
                    # 한국어, 영어, 영어(자동생성) 순으로 자막이 있어서 처리가 완료되면 break. 영상 내 하나의 자막에 대해서만 처리하기 위해
                    break
            # 자막 유무 플래그와 자막 append
            tmp_row.append(tmp_chk_cap)
            tmp_row.append(tmp_content)
            if not tmp_chk_cap:
                # ret = f"Neither Korean nor English but only {', '.join(tmp_cap_list)} captions in this video url ({tmp_url}) [{tmp_title[:10] + '...'}]"
                ret = f"Neither Korean nor English in this video url ({tmp_url}) [{tmp_title[:10] + '...'}]"
        else:
            ret = f"No captions in this video url ({tmp_url}) [{tmp_title[:10] + '...'}]"
        tmp_row.append(ret)
        # 행 단위로 src_df에 append
        ret_row = pd.Series(tmp_row, index=src_df.columns)
        src_df = src_df.append(ret_row, ignore_index=True)
    return src_df