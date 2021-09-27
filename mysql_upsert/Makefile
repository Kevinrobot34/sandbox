MYSQL_PORT   := 3305
MYSQL_DBNAME := mysql_sandbox
MYSQL_CNAME  := mysql_sandbox_container
MYSQL_PWD    := test
CONTAINER_ID := $(shell docker ps -a | grep ${MYSQL_CNAME} | awk '{print $$1}')


run_local_mysql:
	docker run --mount 'type=bind,src=$(shell pwd)/sql,dst=/sql' \
			   --name ${MYSQL_CNAME} \
			   -e MYSQL_ROOT_PASSWORD=${MYSQL_PWD} \
			   -e MYSQL_DATABASE=${MYSQL_DBNAME} \
			   -p ${MYSQL_PORT}:3306 \
			   -d mysql:5.7 \
			   --character-set-server=utf8mb4 \
			   --collation-server=utf8mb4_bin \
			   --secure-file-priv=''

exec_bash:
	docker container exec -it ${CONTAINER_ID} /bin/bash

exec_sql:
	docker container exec -it -e MYSQL_PWD=${MYSQL_PWD} ${CONTAINER_ID} \
		bash -c 'cat /sql/${SQL} | mysql -u root ${MYSQL_DBNAME}'

delete_container:
	docker rm --force ${CONTAINER_ID}
