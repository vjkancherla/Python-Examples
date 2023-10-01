#!/usr/bin/env python3

import boto3

def main():
    print("<---START--->")

    iam = boto3.client("iam")

    rolesFile = open('./files/all_roles.txt', 'r')
    rolesInFile = rolesFile.readlines()

    rolesWithSeparateS3Policy = []
    rolesWithOutSeparateS3Policy = []

    for roleName in rolesInFile:
        print(f"==> Processing Role: {roleName}")

        inlinePolicies = iam.list_role_policies(RoleName=roleName.strip())["PolicyNames"]

        if len(inlinePolicies) != 0:
            print(f"The Role has the following In-Line Policies defined: {inlinePolicies}")

            if "s3" in inlinePolicies:
                rolesWithSeparateS3Policy.append(roleName.strip())
            else:
                rolesWithOutSeparateS3Policy.append(roleName.strip())

        else:
            print("The Role has NO In-Line Policies defined")

        managedPolicies =  iam.list_attached_role_policies(RoleName=roleName.strip())["AttachedPolicies"]

        if len(managedPolicies) > 0:
            print("The Role has the following Managed Policies attached:")
            for managedPolicy in managedPolicies:
                print(managedPolicy["PolicyName"])
        # else:
        #     print("The Role has only AmazonEC2RoleforSSM Managed Policies attached")

        print("")

    print("<--FINISH-->")

    print(*rolesWithSeparateS3Policy,sep='\n')
    print("")
    print(*rolesWithOutSeparateS3Policy,sep='\n')


main()
