import re

# 자막 수집 과정에서 '자막' 텍스트만 남기기 위한 전처리
# input: 처리 전 자막 string
# output: 처리 후 자막 string
def getRegexScript(p_str):
    ret_str = ""
    tgt_str = p_str
    ret_str = re.sub(r'\d+:\d+:\d+,\d+', ' ', tgt_str)
    ret_str = re.sub(r'\d+:\d+:\d+,\d+', ' ', ret_str)
    ret_str = re.sub(r'\d+\n', ' ', ret_str)
    ret_str = re.sub(r'-->', ' ', ret_str)
    ret_str = re.sub(r'\n', ' ', ret_str)
    ret_str = re.sub(r'\[\w*\]', ' ', ret_str)
    ret_str = re.sub(r'\s{2,}', ' ', ret_str)
    ret_str = re.sub(r'\"', ' ', ret_str)
    # ret_str = re.sub(r'[^가-힣0-9a-zA-Z?!,.;:$%'&\' ]', ' ', ret_str)
    # ret_str = re.sub(r'[^가-힣0-9a-zA-Z?!,.;:$%'&\'" ]', ' ', ret_str)
    ret_str = re.sub(r'\s+', ' ', ret_str).strip()
    ret_str = re.sub(r"ain['']t", ' am not', ret_str)
    ret_str = re.sub(r"([Cc]an)['']t", '\\1not', ret_str)
    ret_str = re.sub(r"n['']t", ' not', ret_str)
    ret_str = re.sub(r"['']ve", ' have', ret_str)
    ret_str = re.sub(r"['']s", ' is', ret_str)
    ret_str = re.sub(r"['']ll", ' will', ret_str)
    ret_str = re.sub(r"['']m", ' am', ret_str)
    ret_str = re.sub(r"['']re", ' are', ret_str)
    ret_str = re.sub(r"['']d", ' would', ret_str)
    ret_str = re.sub(r"(s[''])([ .])", '\\2', ret_str).strip()
    return ret_str