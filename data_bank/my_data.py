import os
import json
import boto3

client = boto3.client('dynamodb')
tablename = os.environ['tablename']

def data(event, context):

    body = json.loads(event['body'])

    response = client.scan(
        TableName = tablename,
        Select= 'ALL_ATTRIBUTES'
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }