#!/bin/bash

unset KUBECONFIG

cd .. && docker build -f docker/Dockerfile.latest \
             -t benny12388/chatgpt-on-wechat .

docker tag benny12388/chatgpt-on-wechat benny12388/chatgpt-on-wechat:$(date +%y%m%d)
