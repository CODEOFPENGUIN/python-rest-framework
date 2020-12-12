from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import os
from rest_framework.decorators import api_view

from .apis.youtubeApis import *
from .common.response import *

from .common.logger import *

logger = getLogger(__name__)
# import logging

# Create your views here.
@api_view(['GET'])
def youtube(request):
    #GET youtube info
    res = {}
    try:
        url = request.query_params['url']
        df = getSourceDataFrameSingle(url)
        rec_df = df.to_json(orient="records")
        json_obj = json.loads(rec_df)[0]
        res = successResponse(json_obj)

        logger.debug(f'URL PARAMETER:{url}')
    except:
        res = failResponse({'message': 'Youtube Fail'})
        
    return JsonResponse(res, status=status.HTTP_200_OK)
