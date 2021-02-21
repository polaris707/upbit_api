#!/bin/bash
PARENT_DIR_PATH=$(dirname $PWD)
PROJECT_NAME=$(basename $PARENT_DIR_PATH)

docker build -t ${PROJECT_NAME} .
