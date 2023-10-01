#!/usr/bin/env python3

import boto3
import json

def main():
    print("<---START--->")

    s3Client = boto3.client("s3")

    # bucketsFile = open("./files/open_buckets_dev.txt", "r")
    # bucketsNames = bucketsFile.readlines()

    response = s3Client.list_buckets()

    for bucket in response['Buckets']:
        bucketName = bucket["Name"]

        print(f"==> Evaluating Bucket: {bucketName}")

        if bucketName.find("-html") == -1 and bucketName.find("-artifacts") == -1:
            continue

        newPermissions = {
                "Sid": "DenyUnencryptedCommunication",
                "Effect": "Deny",
                "Principal": {"AWS" : "*"},
                "Action": ["s3:*"],
                "Resource": [
                    f"arn:aws:s3:::{bucketName}/*",
                    f"arn:aws:s3:::{bucketName}"
                ],
                "Condition": {
                    "Bool": {
                        "aws:SecureTransport": ["false"]
                    }
                }
            }

        response = {}
        try:
            response = s3Client.get_bucket_policy(Bucket=bucketName)
        except Exception as e:
            print("Bucket has no policy. We will create a new one shortly.")


        if "Policy" in response:
            policyString = response["Policy"]

            if policyString.find("DenyUnencryptedCommunication") != -1:
                print("The policy already has the necessary permissions. Modfying em")
                print("")

                policyJson = json.loads(policyString)

                print(f"Current Policy: {policyJson}")

                policyJson["Statement"][-1] = newPermissions

                policyString = json.dumps(policyJson)
            else:
                policyJson = json.loads(policyString)

                print(f"Current Policy: {policyJson}")

                policyJson["Statement"].append(newPermissions)

                print(f"Updated Policy : {policyJson}")

                policyString = json.dumps(policyJson)

        else:
            print(f"Bucket has no Policy. Creating a new one with the required permissons")

            newPolicy = {
                    "Version": "2012-10-17",
                    "Statement": [
                            newPermissions
                        ]
                    }

            policyString = json.dumps(newPolicy)

        try:
            s3Client.put_bucket_policy(Bucket=bucketName, Policy=policyString)
        except Exception as e:
            print(f"An error occurrend whilst updating bucket policy {policyString}: {e}")
            exit()

        print(f"Successfully updated Bucket: {bucketName}'s policy")

        print("")

    print("<--FINISH-->")

main()
