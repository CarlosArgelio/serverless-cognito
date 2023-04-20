import os
import json
import uuid
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.resource('dynamodb')

def create(event, context):
    
    id = str(uuid.uuid1())
    body = json.loads(event['body'])
    body['pk'] = id

    table = client.Table("data_bank")

    item = {
        "pk": str(body['pk']),
        "username": str(body['username']),
        "tdc": str(body['tdc']),
        "money": str(body['money'])
    }

    data = table.put_item(
        Item=item
    )

    send_response = item|data

    response = {"statusCode": 200, "body": json.dumps(send_response, indent=4, sort_keys=True, default=str)}

    return response