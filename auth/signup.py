import json
import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



CognitoIdentityProvider = boto3.client('cognito-idp')

def signup(event, context):

    body = json.loads(event['body'])
    username = str(body['username'])
    password = str(body['password'])
    email = str(body['email'])

    try:
        create_user = CognitoIdentityProvider.sign_up(
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

        confirmed = CognitoIdentityProvider.admin_confirm_sign_up(
            UserPoolId='us-east-2_RLHJC7R1L',
            Username=username
        )

        send_response = create_user|confirmed

        response = {"statusCode":200, "body": json.dumps(send_response, indent=4, sort_keys=True, default=str)}

    except ClientError as error:
        if error.response['Error']['Code'] == 'UsernameExistsException':
            logger.warn(f'Error Api {error}')
            
            status_code = error.response['ResponseMetadata']['HTTPStatusCode']
            message_error = error.response['Error']['Message']
            
            response = {"statusCode": status_code, "body": json.dumps(message_error, indent=4, sort_keys=True, default=str)}
        
        else:
            raise {"statusCode": 500, "body": json.loads(error)} and logger.warn(error)
    
    return response

