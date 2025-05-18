#!/bin/bash
rsync -avPS ../src .
docker build -t snow-look .
