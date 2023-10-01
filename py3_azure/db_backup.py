#!/usr/bin/env python3

import gzip
import subprocess
import datetime
import azure.functions as func
from azure.storage.blob import BlockBlobService
import platform, os
import uuid

HOST = os.environ["HOST"]
PORT = os.environ["PORT"]
DB_NAME = os.environ["DB_NAME"]
USER_NAME = os.environ["USER_NAME"]+"@"+HOST
PASSWORD = os.environ["PASSWORD"]
INSTANCE_NAME = os.environ["INSTANCE_NAME"]
BACKUP_FILE_NAME = ""
BACKUP_FILE_ABSOLUTE_PATH = ""
BLOB_CONTAINER_NAME = os.environ["BLOB_CONTAINER_NAME"]
BLOB_CONNECTION_STRING = os.environ["BLOB_CONNECTION_STRING"]

def take_backup():
    print(f"Backing up {DB_NAME} database to {BACKUP_FILE_ABSOLUTE_PATH}")

    try:
        process = subprocess.Popen(
            [
                "/usr/bin/pg_dump",
                "-Fc", "-h", HOST, "-U", USER_NAME, "--compress=0", "-c", "-O", "--if-exists", DB_NAME,
                "-f", BACKUP_FILE_ABSOLUTE_PATH
            ],
            stdout=subprocess.PIPE,
            env={"PGPASSWORD": PASSWORD, "PGSSLMODE": "require"}
        )

        output = process.communicate()[0]

        if process.returncode != 0:
            print(f"Command failed. Return code : {process.returncode}")
            exit(1)

        for line in output.splitlines():
            print(line)

        print("Dump file successfully created")
    except Exception as e:
        print(e)
        exit(1)


def compress_backup_file():
    print(f"Compressing {BACKUP_FILE_ABSOLUTE_PATH}")

    try:
        process = subprocess.Popen(
            [
                "/usr/bin/pigz",
                BACKUP_FILE_ABSOLUTE_PATH
            ],
            stdout=subprocess.PIPE
        )

        output = process.communicate()[0]

        if process.returncode != 0:
            print(f"Command failed. Return code : {process.returncode}")
            exit(1)

        for line in output.splitlines():
            print(line)

    except Exception as e:
        print(e)
        exit(1)

    print(f"Successfuly compressed {BACKUP_FILE_ABSOLUTE_PATH}")


def upload_backup_to_blob_storage():
    compressed_file = f"{BACKUP_FILE_ABSOLUTE_PATH}.gz"

    print(f"Uploading {compressed_file} to Blob Container '{BLOB_CONTAINER_NAME}'...")

    blobService = BlockBlobService(
        connection_string=BLOB_CONNECTION_STRING)

    blobService.create_blob_from_path(BLOB_CONTAINER_NAME, BACKUP_FILE_NAME+".gz", compressed_file)


    print(f"Sucessfully uploaded {compressed_file} to Blob Container '{BLOB_CONTAINER_NAME}'")


def cleanup():
    compressed_file = f"{BACKUP_FILE_ABSOLUTE_PATH}.gz"

    print(f"Deleting dump files {compressed_file}")

    if os.path.exists(compressed_file):
        os.remove(compressed_file)
        print(f"Successfuly Deleted dump file {compressed_file}")
    else:
        print(f"The dump file {compressed_file} does not exist")


def main():
    print("Starting Backup Job")

    global BACKUP_FILE_NAME
    global BACKUP_FILE_ABSOLUTE_PATH

    time_now = datetime.datetime.now().strftime("%d-%b-%Y_%H:%M")
    BACKUP_FILE_NAME = "backup_"+DB_NAME+"_"+INSTANCE_NAME+"_"+time_now+"_"+str(uuid.uuid4())[:8]
    BACKUP_FILE_ABSOLUTE_PATH = "/data/"+BACKUP_FILE_NAME+".dmp"

    take_backup()
    compress_backup_file()
    upload_backup_to_blob_storage()
    cleanup()

    print("Backup Job Successfuly Completed")

#Run the code
main()
