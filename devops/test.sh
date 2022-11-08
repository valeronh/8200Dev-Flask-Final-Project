#!/bin/bash -x

rc=0
request=$( curl -s http://localhost:5000/attendance | grep "Valery Khirin" | wc -l )
request2=$( curl -s http://localhost:5000/about | grep "Valery Khirin" | wc -l )
request3=$( curl -s http://localhost:5000/flow | grep "dockerization" | wc -l )
request4=$( curl -s http://localhost:5000/home | grep "calculation" | wc -l )

if [ $request -eq 0 ]; then
        echo "Attendance test failed"
        rc=1
elif [ $request2 -eq 0 ]; then
        echo "About test failed"
        rc=1
elif [ $request3 -eq 0 ]; then
        echo "Flow test failed"
        rc=1
elif [ $request4 -eq 0 ]; then
        echo "Home page test failed"
        rc=1
fi

exit ${rc}

