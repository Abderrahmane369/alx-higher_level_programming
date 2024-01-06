#!/bin/bash
#lloeazo

curl -X POST -H "Content-Type: application/json" -d "@$2" $1
#!/bin/bash
#lloeazo

response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d "@$2" $1)
echo $response
