#!/bin/bash -x

rc=0

request() {
	page="${1}"
	word="${2}"
	request=$( curl -s http://localhost:5000/${page} | grep "${word}" | wc -l )
	if [ $request -eq 0 ]; then
        	echo "${page} Test Failed"
        	rc=1
	fi	
}

main() {
	request "attendance" "Valery Khirin"
	request "about" "Valery Khirin"
	request "flow" "dockerization"
	request "home" "Valery Khirin"

	exit ${rc}
}

main


