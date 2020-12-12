import json

from ..modelObjects.constants import *

def successResponse(json_obj):
    res = {
        'succesOrNot': SUCCESS_OR_NOT_Y,
        'statusCode': SUCCESS_STATUS_CODE,
        'desc': DEFAULT_DESC,
        'data': DEFAULT_DATA
    }
    res.update({'data': json_obj})
    return res

def failResponse(json_obj):
    res = {
        'succesOrNot': SUCCESS_OR_NOT_N,
        'statusCode': FAIL_STATUS_CODE,
        'desc': DEFAULT_DESC,
        'data': DEFAULT_DATA
    }
    res.update({'data': json_obj})
    return res