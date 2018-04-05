import logging, os
import requests
from requests.auth import HTTPBasicAuth


logging.basicConfig(
    # filename=settings.SOME_PATH,
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S'
    )
log = logging.getLogger(__name__)
log.debug( '\n-------\nstarting standard log' )


GRIZZLY_HTTPBASIC_KEY = os.environ['GRIZZLY_HTTPBASIC_KEY']
GRIZZLY_HTTPBASIC_SECRET = os.environ['GRIZZLY_HTTPBASIC_SECRET']


log.debug( 'user, `%s`' % GRIZZLY_HTTPBASIC_KEY )

r = requests.get( url, auth=HTTPBasicAuth(GRIZZLY_HTTPBASIC_KEY, GRIZZLY_HTTPBASIC_SECRET) )

log.debug( 'r.content, ```%s```' % r.content )
