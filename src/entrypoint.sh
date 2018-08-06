#!/bin/sh
bash ./wait-for-it.sh postgres:$DB_PORT -t 25
alembic upgrade head
python3 main.py