#!/bin/bash -x

env=${1}

if [[ "$env" != "test" &&  "$env" != "prod" ]]; then
	echo "None of the machines were specified - type [prod/test]"
	exit 1
fi

scp docker-compose.yaml ec2-user@${env}:~/.

if [ "$env" == "test" ]; then
	scp devops/test.sh ec2-user@${env}:~/.
fi
