import logging
import json
import azure.functions as func
from .redis_client import get_redis, get_hash, set_hash
from .strava import request_monthly_activities

KEY = 'DIST_DICT'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    r = get_redis()
    cache_hit = True
    distances = get_hash(r, KEY)
    if distances == None:
        distances = request_monthly_activities()
        set_hash(r, KEY, distances)
        cache_hit = False

    logging.info('cache_hit_or_miss', {"cache_hit": 1 if cache_hit == True else 0})
    
    return func.HttpResponse(
             json.dumps(distances),
             status_code=200,
             headers={cache_hit: 1 if cache_hit == True else 0})
