import os
import requests
from requests.auth import HTTPBasicAuth


GRIZZLY_HTTPBASIC_USER = os.environ['GRIZZLY_HTTPBASIC_USER']
GRIZZLY_HTTPBASIC_PASSWORD = os.environ['GRIZZLY_HTTPBASIC_PASSWORD']


log.debug( 'user, `%s`' % GRIZZLY_HTTPBASIC_USER )

r = requests.get( url, auth=HTTPBasicAuth(GRIZZLY_HTTPBASIC_USER, GRIZZLY_HTTPBASIC_PASSWORD) )

log.debug( 'r.content, ```%s```' % r.content )
