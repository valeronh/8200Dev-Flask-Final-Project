#!/bin/bash -x

env=${1}

if [[ "$env" != "test" &&  "$env" != "prod" ]]; then
	echo "None of the machines were specified - type [prod/test]"
	exit 1
fi

main () {
	scp docker-compose.yaml ec2-user@${env}:~/.
	ssh ec2-user@${env} docker pull valeron12345/flask_app:latest
	ssh ec2-user@${env} docker-compose up -d

	if [ "$env" == "test" ]; then
		scp devops/test.sh ec2-user@${env}:~/.
		sleep 10
		ssh ec2-user@${env} ./test.sh
	fi
}

main
