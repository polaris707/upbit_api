#!/bin/bash
PARENT_DIR_PATH=$(dirname $PWD)
PROJECT_NAME=$(basename $PARENT_DIR_PATH)

docker ps -a | grep -w ${PROJECT_NAME} | awk '{print $1}' | xargs docker stop
docker run -it -d --rm --name ${PROJECT_NAME} \
    -v ${PARENT_DIR_PATH}:/home/project \
    ${PROJECT_NAME}

docker exec -it ${PROJECT_NAME} bash