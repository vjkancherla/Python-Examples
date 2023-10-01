#!/usr/bin/env python3

# import boto3
# import hmac
# import hashlib
# import base64

# def create_cognito_user():
#     client = boto3.client("cognito-idp")
#
#     poolId = "eu-west-2_owIm9e3Xf"
#     phoneNumber = "+447810510970"
#     password = "ChangeMe22!"
#     clientId = "7u3aoeuvvcfidpgipt6v7cd1of"
#     clientSecret = "1hh9m55lmrndeo9bguacshh33c3c8cbu8s5mopr3glqorbokaii0"
#
#     try:
#         response = client.admin_create_user(
#             UserPoolId=poolId,
#             Username=phoneNumber,
#             UserAttributes=[
#                 {
#                     'Name': 'phone_number',
#                     'Value': phoneNumber
#                 },
#                 {
#                     'Name': 'phone_number_verified',
#                     'Value': 'true'
#                 }
#             ],
#             TemporaryPassword=password,
#             ForceAliasCreation=False,
#             MessageAction="SUPPRESS",
#         )
#         print(response)
#
#         response = client.admin_set_user_password(
#             UserPoolId=poolId,
#             Username=phoneNumber,
#             Password=password,
#             Permanent=True
#         )
#         print(response)
#
#         #Create a secret hash
#         secret_hash = hmac.new(
#             clientSecret.encode("utf-8"),
#             msg=(phoneNumber+clientId).encode("utf-8"),
#             digestmod=hashlib.sha256
#         ).digest()
#         secret_hash = base64.b64encode(secret_hash).decode()
#
#         response = client.admin_initiate_auth(
#             UserPoolId=poolId,
#             ClientId=clientId,
#             AuthFlow="ADMIN_NO_SRP_AUTH",
#             AuthParameters={
#                 "USERNAME": phoneNumber,
#                 "PASSWORD": password,
#                 "SECRET_HASH": secret_hash
#             }
#         )
#         print(response)
#
#         print("Log in success")
#         print("Access token:", response['AuthenticationResult']['AccessToken'])
#         print("ID token:", response['AuthenticationResult']['IdToken'])
#     except Exception as e:
#         print(e)
#
# create_cognito_user()

event = {
   "body":"eyJ0ZXN0IjoiYm9keSJ9",
   "resource":"/{proxy+}",
   "path":"/path/to/resource",
   "httpMethod":"POST",
   "isBase64Encoded":"true",
   "queryStringParameters":{
      "foo":"bar"
   },
   "multiValueQueryStringParameters":{
      "foo":[
         "bar"
      ]
   },
   "pathParameters":{
      "proxy":"/path/to/resource"
   },
   "stageVariables":{
      "baz":"qux"
   },
   "headers":{
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Accept-Encoding":"gzip, deflate, sdch",
      "Accept-Language":"en-US,en;q=0.8",
      "Cache-Control":"max-age=0",
      "CloudFront-Forwarded-Proto":"https",
      "CloudFront-Is-Desktop-Viewer":"true",
      "CloudFront-Is-Mobile-Viewer":"false",
      "CloudFront-Is-SmartTV-Viewer":"false",
      "CloudFront-Is-Tablet-Viewer":"false",
      "CloudFront-Viewer-Country":"US",
      "Host":"1234567890.execute-api.us-east-1.amazonaws.com",
      "Upgrade-Insecure-Requests":"1",
      "User-Agent":"Custom User Agent String",
      "Via":"1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Id":"cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
      "X-Forwarded-For":"127.0.0.1, 127.0.0.2",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https",
      "username":"+447810510970"
   },
   "multiValueHeaders":{
      "Accept":[
         "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
      ],
      "Accept-Encoding":[
         "gzip, deflate, sdch"
      ],
      "Accept-Language":[
         "en-US,en;q=0.8"
      ],
      "Cache-Control":[
         "max-age=0"
      ],
      "CloudFront-Forwarded-Proto":[
         "https"
      ],
      "CloudFront-Is-Desktop-Viewer":[
         "true"
      ],
      "CloudFront-Is-Mobile-Viewer":[
         "false"
      ],
      "CloudFront-Is-SmartTV-Viewer":[
         "false"
      ],
      "CloudFront-Is-Tablet-Viewer":[
         "false"
      ],
      "CloudFront-Viewer-Country":[
         "US"
      ],
      "Host":[
         "0123456789.execute-api.us-east-1.amazonaws.com"
      ],
      "Upgrade-Insecure-Requests":[
         "1"
      ],
      "User-Agent":[
         "Custom User Agent String"
      ],
      "Via":[
         "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
      ],
      "X-Amz-Cf-Id":[
         "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
      ],
      "X-Forwarded-For":[
         "127.0.0.1, 127.0.0.2"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ]
   },
   "requestContext":{
      "accountId":"123456789012",
      "resourceId":"123456",
      "stage":"prod",
      "requestId":"c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
      "requestTime":"09/Apr/2015:12:34:56 +0000",
      "requestTimeEpoch":"1428582896000",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "accessKey":"None",
         "sourceIp":"127.0.0.1",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"Custom User Agent String",
         "user":"None"
      },
      "path":"/prod/path/to/resource",
      "resourcePath":"/{proxy+}",
      "httpMethod":"POST",
      "apiId":"1234567890",
      "protocol":"HTTP/1.1"
   }
}

print (event["headers"]["username"])
