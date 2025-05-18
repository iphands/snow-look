#!/bin/bash
source /main/docker/snow-look/spec
cd /main/docker/snow-look/spec

docker create --name $NAME \
  -v /main/docker/snow-look/data:/src/data
  $NAME
