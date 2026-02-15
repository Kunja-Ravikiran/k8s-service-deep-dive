#!/bin/bash

MINIKUBE_IP=$(minikube ip)

for i in {1..6}
do
  curl http://$MINIKUBE_IP:30007
  echo -e "\n-----------------------------\n"
done

