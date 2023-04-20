import os
import json
import boto3

client = boto3.client('dynamodb')

IS_OFFLINE = os.getenv('IS_OFFLINE', False)
if IS_OFFLINE:
    boto3.Session(
        aws_access_key_id='ACESS_KEY',
        aws_secret_access_key='SECRET_KEY'
    )
    client = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

tablename = os.environ['tablename']

def create(event, context):
    
    body = json.loads(event['body'])

    item = {body}

    response = client.put_item(
        TableName = tablename,
        Item=item
    )

    return {
        "statusCode": 201,
        "Body": response
    }