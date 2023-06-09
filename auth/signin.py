import json
import boto3

client = boto3.client('cognito-idp')

def signin(event, context):

    body = json.loads(event['body'])
    username = str(body['username'])
    password = str(body['password'])

    authentication = client.initiate_auth(
        # UserPoolId='us-east-2_RLHJC7R1L',
        ClientId='jhebkck5l195ug1gbp66ok4j9',
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    response = {"statusCode": 200, "body":json.dumps(authentication, indent=4, sort_keys=True, default=str) }

    return response
