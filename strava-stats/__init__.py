import logging
import json
import azure.functions as func
from opencensus.ext.azure.log_exporter import AzureLogHandler
from .redis_client import get_redis, get_hash, set_hash
from .strava import request_monthly_activities
import os

KEY = 'DIST_DICT'

_logger = logging.getLogger('opencensus')
_logger.addHandler(
    AzureLogHandler(
        connection_string=os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"]
    )
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    _logger.info('Python HTTP trigger function processed a request.')

    r = get_redis()
    cache_hit = True
    distances = get_hash(r, KEY)
    if distances == None:
        distances = request_monthly_activities()
        set_hash(r, KEY, distances)
        cache_hit = False

    properties = {'custom_dimensions':{'cache_hit': 1 if cache_hit == True else 0}}
    _logger.info('cache_hit_or_miss', extra=properties)
    
    return func.HttpResponse(
             json.dumps(distances),
             status_code=200,
             headers={"cache_hit": 1 if cache_hit == True else 0})
