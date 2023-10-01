#!/usr/bin/env python3

import gzip
import subprocess
import datetime
import logging
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
    logging.info(f"Backing up {DB_NAME} database to {BACKUP_FILE_ABSOLUTE_PATH}")

    try:
        process = subprocess.Popen(
            [
                "/usr/bin/pg_dump",
                "-Fc", "-h", HOST, "-U", USER_NAME, "--compress=9", "-c", "-O", "--if-exists", DB_NAME,
                "-f", BACKUP_FILE_ABSOLUTE_PATH
            ],
            stdout=subprocess.PIPE,
            env={"PGPASSWORD": PASSWORD, "PGSSLMODE": "require"}
        )

        output = process.communicate()[0]

        if process.returncode != 0:
            logging.info(f"Command failed. Return code : {process.returncode}")
            exit(1)

        for line in output.splitlines():
            logging.info(line)

        logging.info("Backup complete")
    except Exception as e:
        logging.info(e)
        exit(1)


def compress_backup_file():
    logging.info(f"Compressing {BACKUP_FILE_ABSOLUTE_PATH}")

    compressed_file = "{}.gz".format(str(BACKUP_FILE_ABSOLUTE_PATH))

    with open(BACKUP_FILE_ABSOLUTE_PATH, "rb") as f_in:
        with gzip.open(compressed_file, "wb") as f_out:
            for line in f_in:
                f_out.write(line)

    logging.info(f"Successfuly compressed {BACKUP_FILE_ABSOLUTE_PATH}")


def upload_backup_to_blob_storage():
    compressed_file = f"{BACKUP_FILE_ABSOLUTE_PATH}.gz"

    logging.info(f"Uploading {compressed_file} to Blob Container '{BLOB_CONTAINER_NAME}'...")

    blobService = BlockBlobService(
        connection_string=BLOB_CONNECTION_STRING)

    blobService.create_blob_from_path(BLOB_CONTAINER_NAME, BACKUP_FILE_NAME+".gz", compressed_file)


    logging.info(f"Sucessfully uploaded {compressed_file} to Blob Container '{BLOB_CONTAINER_NAME}'")


def cleanup():
    compressed_file = f"{BACKUP_FILE_ABSOLUTE_PATH}.gz"
    non_compressed_file = BACKUP_FILE_ABSOLUTE_PATH


    logging.info(f"Deleting dump files {compressed_file} and {non_compressed_file}")

    if os.path.exists(compressed_file):
        os.remove(compressed_file)
        logging.info(f"Successfuly Deleted dump file {compressed_file}")
    else:
        logging.info(f"The dump file {compressed_file} does not exist")

    if os.path.exists(non_compressed_file):
        os.remove(non_compressed_file)
        logging.info(f"Successfuly Deleted dump file {non_compressed_file}")
    else:
        logging.info(f"The dump file {non_compressed_file} does not exist")


def main(mytimer: func.TimerRequest) -> None:
    logging.info("Starting Backup Job")

    if mytimer.past_due:
        logging.info('The invocation time does not match the trigger time specified in function.json, exiting function')
        exit(1)

    global BACKUP_FILE_NAME
    global BACKUP_FILE_ABSOLUTE_PATH

    time_now = datetime.datetime.now().strftime("%d-%b-%Y_%H:%M")
    BACKUP_FILE_NAME = "backup_"+DB_NAME+"_"+INSTANCE_NAME+"_"+time_now+"_"+str(uuid.uuid4())[:8]
    BACKUP_FILE_ABSOLUTE_PATH = "/postgres-dump/"+BACKUP_FILE_NAME+".dmp"

    take_backup()
    compress_backup_file()
    upload_backup_to_blob_storage()
    cleanup()

    logging.info("Backup Job Successfuly Completed")
