#!/usr/bin/env python3

import boto3

def main():
    print("<---START--->")

    iam = boto3.client("iam")

    rolesFile = open('./files/roles2.txt', 'r')
    rolesInFile = rolesFile.readlines()

    rolesWithS3Perms = []
    rolesWithoutS3Perms = []

    for roleName in rolesInFile:
        print(f"==> Evaluating Role: {roleName}")

        inlinePolicies = iam.list_role_policies(RoleName=roleName.strip())["PolicyNames"]

        if len(inlinePolicies) != 0:
            for pol in inlinePolicies:
                print(f"Evaluting In-Line Policy: {pol}")
                response = iam.get_role_policy(RoleName=roleName.strip(), PolicyName=pol)
                policyDoc = response["PolicyDocument"]
                print(policyDoc)
                if str(policyDoc).find("arn:aws:s3") != -1:
                    print("In-Line Policy defines S3 permissions")
                    rolesWithS3Perms.append(roleName.strip())
                    break
                else:
                    print("In-Line Policy DOES NOT define S3 permissions")
            if roleName.strip() not in rolesWithS3Perms:
                rolesWithoutS3Perms.append(roleName.strip())
        else:
            print("The Role has NO In-Line Policies defined")

        print("")

    print("<--FINISH-->")

    print(*rolesWithS3Perms,sep='\n')
    print("")
    print(*rolesWithoutS3Perms,sep='\n')

main()
