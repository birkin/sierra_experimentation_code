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

## get the token; looks like it's good for an hour

token_url = '%stoken' % API_ROOT_URL
log.debug( 'token_url, ```%s```' % token_url )
r = requests.post( token_url, auth=HTTPBasicAuth(HTTPBASIC_KEY, HTTPBASIC_SECRET) )
log.debug( 'token r.content, ```%s```' % r.content )
token = r.json()['access_token']
log.debug( 'token, ```%s```' % token )

## make a bib-request

bib_url = '%sbibs/?id=1000001' % API_ROOT_URL
log.debug( 'token_url, ```%s```' % token_url )
custom_headers = {'Authorization': 'Bearer %s' % token }
r = requests.get( bib_url, headers=custom_headers )
log.debug( 'bib r.content, ```%s```' % r.content )




# r = requests.get( API_ROOT_URL, auth=HTTPBasicAuth(HTTPBASIC_KEY, HTTPBASIC_SECRET) )

# log.debug( 'r.content, ```%s```' % r.content )
