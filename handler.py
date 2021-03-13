from src import save_transaction

def handler(event, context):
    # save_transaction(json.loads(event))
    return {'success': 200}
