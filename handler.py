import json
from src import save_transaction

import logging

logging.basicConfig(level=logging.INFO, format='[%(levelno)s] %(asctime)-15s %(module)s %(lineno)d %(message)s ')
logger = logging.getLogger(__name__)

def handler(event, context):
    logger.info(event)
    save_transaction(event)
    return {'success': 200}
