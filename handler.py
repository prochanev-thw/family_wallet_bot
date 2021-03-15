import json
from src import save_transaction

import logging

if logging.getLogger().handlers:
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO, format='[%(levelno)s] %(asctime)-15s : %(module)s : %(lineno)d : %(message)s')

logger = logging.getLogger(__name__)

def handler(event, context):
    logger.info(event)
    logger.info(event['body'])
    save_transaction(json.loads(event['body']))

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': 'Execution started successfully!'
    }
