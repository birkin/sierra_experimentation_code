'''
SAE__ prefix for "Sierra API Experiementation"
'''

import logging, os, sys
import requests
from requests.auth import HTTPBasicAuth

logging.basicConfig(
    # filename=os.environ['SAE__LOG_PATH'],
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S'
    )
log = logging.getLogger(__name__)
log.debug( '\n-------\nstarting standard log' )

if (sys.version_info < (3, 0)):
    raise Exception( 'forcing myself to use python3 always' )

API_ROOT_URL = os.environ['SAE__ROOT_URL']
HTTPBASIC_KEY = os.environ['SAE__HTTPBASIC_USERNAME']
HTTPBASIC_SECRET = os.environ['SAE__HTTPBASIC_PASSWORD']

## ok, let's get to work! ##

## get the token

url = '%stoken' % API_ROOT_URL
log.debug( 'url for token, ```%s```' % url )





# r = requests.get( API_ROOT_URL, auth=HTTPBasicAuth(HTTPBASIC_KEY, HTTPBASIC_SECRET) )

# log.debug( 'r.content, ```%s```' % r.content )
