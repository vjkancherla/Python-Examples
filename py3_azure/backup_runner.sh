#!/usr/bin/bash

echo ""
echo ">> Starting script at $(date)"
echo ""

dbName=$1

if [ "${dbName}" == "sso" ]
then
  set -a
  source /home/vija0326/scripts/envs/sso.env
  set +a
elif [ "${dbName}" == "oo" ]
then
  set -a
  source /home/vija0326/scripts/envs/oo.env
  set +a
elif [ "${dbName}" == "web" ]
then
  set -a
  source /home/vija0326/scripts/envs/web.env
  set +a
fi

/usr/bin/python3 /home/vija0326/scripts/db_backup.py

echo ""
echo ">> Script finished at $(date)"
echo ""
