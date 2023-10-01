#!/usr/bin/env python3

import boto3

def main():
    print("<---START--->")

    iam = boto3.client("iam")

    rolesFile = open('./files/all_roles.txt', 'r')
    rolesInFile = rolesFile.readlines()

    policyToRemove = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
    policyToAdd = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"

    for roleName in rolesInFile:
        print(f"==> Evaluating Role: {roleName}")

        print(f"Detaching Managed-Policy: {policyToRemove}")

        try:
            response = iam.detach_role_policy(RoleName=roleName.strip(), PolicyArn=policyToRemove)
        except Exception as e:
            print(f"An error occurrend whilst detaching managed policy {policyToRemove}: {e}")

        print(f"Confirming Managed-Policy: {policyToRemove}'s removal")

        managedPolicies =  iam.list_attached_role_policies(RoleName=roleName.strip())["AttachedPolicies"]

        if len(managedPolicies) > 0:
            if "AmazonEC2RoleforSSM" in [managedPolicy['PolicyName'] for managedPolicy in managedPolicies]:
                print(f"Detaching failed for Managed-Policy: {policyToRemove}")
            else:
                print(f"Successfuly detached Managed-Policy: {policyToRemove}")
        else:
            print(f"Successfuly detached Managed-Policy: {policyToRemove}")


        print(f"Now attaching Managed-Policy: {policyToAdd}")

        try:
            response = iam.attach_role_policy(RoleName=roleName.strip(), PolicyArn=policyToAdd)
        except Exception as e:
            print(f"An error occurrend whilst attaching managed policy {policyToAdd}: {e}")

        print(f"Confirming Managed-Policy: {policyToAdd}'s attachment")

        managedPolicies =  iam.list_attached_role_policies(RoleName=roleName.strip())["AttachedPolicies"]

        if len(managedPolicies) > 0:
            if "AmazonSSMManagedInstanceCore" in [managedPolicy['PolicyName'] for managedPolicy in managedPolicies]:
                print(f"Successfuly attached Managed-Policy: {policyToAdd}")
            else:
                print(f"Attaching failed for Managed-Policy: {policyToAdd}")
        else:
            print(f"Attaching failed for Managed-Policy: {policyToAdd}")

        print("")

    print("<--FINISH-->")

main()
