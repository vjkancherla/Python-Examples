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

        if bucketName.find("-artifacts") != -1:
            #example bucketName = 064530618445-hayday-update-to-base-artifacts

            tokens = bucketName.split("-")
            accNo = tokens[0]
            gameName = tokens[1]

            tokens = bucketName.split("-artifacts")
            tmpString = tokens[0]

            tokens = tmpString.split(f"{accNo}-{gameName}-")

            branchName = tokens[1]

            print(f"GameName={gameName}, BranchName={branchName}")

            print("")

    print("<--FINISH-->")

main()
