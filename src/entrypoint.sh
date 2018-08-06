#!/bin/sh
bash ./wait-for-it.sh postgres:5432
alembic upgrade head
python3 main.py