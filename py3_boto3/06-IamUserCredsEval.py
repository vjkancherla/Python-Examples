#!/usr/bin/env python3

import boto3

def main():
    print("<---START--->")

    environment = "Production"

    iam = boto3.client("iam")

    iamUsers = iam.list_users(PathPrefix = '/system')["Users"]

    for iamUser in iamUsers:
        username = iamUser["UserName"]

        # print(f"==> Evaluating IAM User: {username}")

        accessKeyMetaData = iam.list_access_keys(UserName=username)["AccessKeyMetadata"][0]
        accessKeyId = accessKeyMetaData["AccessKeyId"]
        createDate = accessKeyMetaData["CreateDate"]

        keyUsageData = iam.get_access_key_last_used(AccessKeyId=accessKeyId)["AccessKeyLastUsed"]

        if "LastUsedDate" in keyUsageData:
            lastUsedDate = keyUsageData["LastUsedDate"]
            # print(f"==> IAM User {username}'s AccessKey {accessKeyId} was created on {createDate} and was last used on {lastUsedDate}")
            print(f"{environment},{username},{accessKeyId},{createDate},{lastUsedDate}")
        else:
            # print(f"==> IAM User {username}'s AccessKey {accessKeyId} was created on {createDate} and HAS NOT BEEN USED SINCE CREATION")
            print(f"{environment},{username},{accessKeyId},{createDate},None")

        # print("")

    print("<--FINISH-->")

main()
