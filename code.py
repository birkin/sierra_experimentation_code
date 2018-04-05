'''
SAE__ prefix for "Sierra API Experiementation"
'''

import datetime, logging, os, sys
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

## make a bib-request, just as a test

# bib_url = '%sbibs/?id=1000001' % API_ROOT_URL
bib_url = '%sbibs/' % API_ROOT_URL
payload = { 'id': '1000001' }
log.debug( 'token_url, ```%s```' % token_url )
custom_headers = {'Authorization': 'Bearer %s' % token }
r = requests.get( bib_url, headers=custom_headers, params=payload )
log.debug( 'bib r.content, ```%s```' % r.content )

## ok, we have the first bib, let's get the last (hack, close to the last)
"""
TODO thought... there's probably a way to query the api to get this value.
A hack, though, would be to run a cron job that would just get all the bibs over the last x/hours,
and save the last one to a file at a specified location that the code below would load.
"""
log.debug( '\n-------\ngetting end-bib\n-------' )
today_date = str( datetime.date.today() )
start_datetime = '%sT00:00:00Z' % today_date
end_datetime = '%sT23:59:59Z' % today_date
payload = {
    'limit': '1', 'createdDate': '[%s,%s]' % (start_datetime, end_datetime)  }
r = requests.get( bib_url, headers=custom_headers, params=payload )
log.debug( 'bib r.content, ```%s```' % r.content )
end_bib = r.json()['entries'][0]['id']
log.debug( 'end_bib, `%s`' % end_bib )


