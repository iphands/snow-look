#!/bin/bash
source /main/docker/snow-look/spec
cd /main/docker/snow-look/spec

docker stop snow-look
docker rm snow-look

bash ./build.sh

docker create --name $NAME \
  -v /main/docker/snow-look/data:/src/data
  $NAME
