import os
import json
import boto3

client = boto3.client('dynamodb')

def data(event, context):

    data = client.scan(
        TableName='data_bank',
        Select='ALL_ATTRIBUTES'
    )

    response = {"statusCode": 200, "body": json.dumps(data, indent=4, sort_keys=True, default=str)}

    return response