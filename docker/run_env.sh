#!/bin/bash
PARENT_DIR_PATH=$(dirname $PWD)
PROJECT_NAME=$(basename $PARENT_DIR_PATH)

# kill old containers
echo "stop old ${PROJECT_NAME} env ..."
OLD_CONTAILERS=$(docker ps -a | grep -w ${PROJECT_NAME})
if [ $? != 0 ]; then
    echo "Failed to get old containers"
elif [ -n "$OLD_CONTAILERS" ]; then
    echo "$OLD_CONTAILERS" | awk '{print $1}' | xargs docker stop
    echo "Succeed to stop old containers"
else
    echo "No old containers found"
fi
echo "----------------------------------"

# run new container
echo "start ${PROJECT_NAME} env ..."
docker run -it -d --rm --name ${PROJECT_NAME} \
    -v ${PARENT_DIR_PATH}:/home/project \
    ${PROJECT_NAME}

if [ $? -eq 0 ]; then
    docker exec -it ${PROJECT_NAME} bash
else
   echo "Failed to run ${PROJECT_NAME} env"
fi
echo "----------------------------------"