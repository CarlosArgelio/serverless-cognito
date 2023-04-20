import json
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('cognito-idp')

def signup(event, context):

    body = json.loads(event['body'])
    username = str(body['username'])
    password = str(body['password'])
    email = str(body['email'])

    create_user = client.sign_up(
        ClientId='jhebkck5l195ug1gbp66ok4j9',
        Username=username,
        Password=password,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': email
            }
        ]
    )

    confirmed = client.admin_confirm_sign_up(
        UserPoolId='us-east-2_RLHJC7R1L',
        Username=username
    )

    logger.info(body)
    logger.info(create_user)
    logger.info(confirmed)

    send_response = create_user|confirmed

    response = {"statusCode":200, "body": json.dumps(send_response, indent=4, sort_keys=True, default=str)}
    
    return response

