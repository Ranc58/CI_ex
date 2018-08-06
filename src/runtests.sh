#!/usr/bin/env bash
set -e

export DB_NAME=test_$DB_NAME

python3 -m pytest tests/ -s -vv -ra --junitxml=./unit.xml --cov . --cov-report xml
