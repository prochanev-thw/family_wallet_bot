import json
from src.bot import save_transaction


def handler(event, context):
    save_transaction(json.loads(event))
    return {'success': 200}

