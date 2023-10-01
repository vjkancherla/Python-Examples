#!/usr/bin/env python3

import json
import boto3

event = {
   "version":"0",
   "id":"45553104-c15f-39e3-a3ed-0b8c2f58de87",
   "detail-type":"Restore Job State Change",
   "source":"aws.backup",
   "account":"333012124879",
   "time":"2023-02-13T19:30:58Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:ec2:us-east-1::image/ami-042519bae42da0bf8"
   ],
   "detail":{
      "restoreJobId":"D59196C8-8951-4C80-E71E-8F41E6D364E5",
      "backupSizeInBytes":"8589934592",
      "creationDate":"2023-02-13T19:28:39.032Z",
      "iamRoleArn":"arn:aws:iam::333012124879:role/service-role/AWSBackupDefaultServiceRole",
      "percentDone":0.0,
      "resourceType":"EC2",
      "status":"COMPLETED",
      "createdResourceArn":"arn:aws:ec2:us-east-1:333012124879:instance/i-00175d8c7c22c7a8d",
      "completionDate":"2023-02-13T19:29:55.681Z"
   }
}

context = ""

def process(event, context):

    print(f"Event: {event}")

    try:
        backupEventStatus = event["detail"]["status"]
    except Exception as e:
        print("Backup Restore Job's status not found. IGNORE_EVENT")
        return

    if backupEventStatus == "COMPLETED":

        backupResourceType = event["detail"]["resourceType"]

        if backupResourceType == "EC2":

            amiARN = event["resources"][0]

            amiID = (amiARN.split("/")[1]).strip()

            print(f"AMI_ID: {amiID}")

            ec2 = boto3.client("ec2", region_name="us-east-1")

            response = ec2.describe_images(
                ImageIds=[
                    amiID
                ]
            )

            amiName = response["Images"][0]["Name"]

            instanceID = (amiName.split("_")[1]).strip()

            print(f"Instance_ID: {instanceID}")

            backupRestoreJobID = event["detail"]["restoreJobId"]
            backupRestoreCompletionTime = event["detail"]["creationDate"]
            backupRestoreResultantInstanceID = (event["detail"]["createdResourceArn"].split("/")[1]).strip()

            dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
            table = dynamodb.Table("rax-test2")

            table.put_item(
                Item={
                    'instance_id': instanceID,
                    'restored_date': backupRestoreCompletionTime,
                    'backup_restore_job_id': backupRestoreJobID,
                    'resultant_restored_instance_id': backupRestoreResultantInstanceID
                }
            )

            response = table.get_item(
                Key={
                    'instance_id': instanceID
                }
            )

            item = response['Item']

            print(f"successfully added the following Item to DynamoDB table: {item}")

        else:
            print ("IGNORE_NON_EC2_RESOURCE")

    else:
        print ("IGNORE_EVENT")


process(event, context)
