#!/usr/bin/env bash
set -e

export DB_NAME=test_$DB_NAME
export PYTHONDONTWRITEBYTECODE=1

python3 -m pytest tests/ --ff --lf --cov-report term-missing -s -vv -ra --junitxml=./unit.xml --cov . --cov-report xml
