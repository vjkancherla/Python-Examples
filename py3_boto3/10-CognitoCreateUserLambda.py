import boto3
import hmac
import hashlib
import base64
import json

def lambda_handler(event, context):
    client = boto3.client("cognito-idp")

    poolId = "eu-west-2_owIm9e3Xf"
    phoneNumber = event["headers"]["username"]
    password = "ChangeMe22!"
    clientId = "7u3aoeuvvcfidpgipt6v7cd1of"
    clientSecret = "1hh9m55lmrndeo9bguacshh33c3c8cbu8s5mopr3glqorbokaii0"
    responeBody = ""
    statusCode = 200

    try:
        response = client.admin_create_user(
            UserPoolId=poolId,
            Username=phoneNumber,
            UserAttributes=[
                {
                    'Name': 'phone_number',
                    'Value': phoneNumber
                },
                {
                    'Name': 'phone_number_verified',
                    'Value': 'true'
                }
            ],
            TemporaryPassword=password,
            ForceAliasCreation=False,
            MessageAction="SUPPRESS",
        )
        print(response)

        response = client.admin_set_user_password(
            UserPoolId=poolId,
            Username=phoneNumber,
            Password=password,
            Permanent=True
        )
        print(response)

        #Create a secret hash
        secret_hash = hmac.new(
            clientSecret.encode("utf-8"),
            msg=(phoneNumber+clientId).encode("utf-8"),
            digestmod=hashlib.sha256
        ).digest()
        secret_hash = base64.b64encode(secret_hash).decode()

        response = client.admin_initiate_auth(
            UserPoolId=poolId,
            ClientId=clientId,
            AuthFlow="ADMIN_NO_SRP_AUTH",
            AuthParameters={
                "USERNAME": phoneNumber,
                "PASSWORD": password,
                "SECRET_HASH": secret_hash
            }
        )
        print(response)

        print("Access token:", response['AuthenticationResult']['AccessToken'])
        print("ID token:", response['AuthenticationResult']['IdToken'])

        responeBody = {
            "access_token": response['AuthenticationResult']['AccessToken'],
            "id_token": response['AuthenticationResult']['IdToken'],
            "refresh_token": response['AuthenticationResult']['RefreshToken'],
            "username": phoneNumber,
            "password": password
        }
    except Exception as e:
        print(e)
        statusCode = 500
        responeBody = str(e)


    return {
        'statusCode': statusCode,
        'body': json.dumps(responeBody)
    }
