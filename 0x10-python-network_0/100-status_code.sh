#!/bin/bash
<<<<<<< HEAD
#loazeo
curl -s -o /dev/null -w "%{http_code}" "$1"
=======
#binobasha
curl -o /dev/null -s -w "%{http_code}\n" "$1"

>>>>>>> refs/remotes/origin/main
