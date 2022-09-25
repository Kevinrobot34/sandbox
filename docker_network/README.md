
* `docker-compose up -d` で起動
  * `docker-compose ps` や `docker-container ls` で確認
* `docker exec -it ubuntu /bin/bash` でubuntuに入る


## IPアドレスの確認

* Ubuntuなど直接入れるやつ
    ```bash
    % docker exec -it ubuntu /bin/bash
    root@e0a231d37369:/# hostname -i
    10.254.249.3
    ```
* inspect使って確認
  * https://docs.docker.jp/engine/reference/commandline/inspect.html
  * 雑なやつ
    ```bash
    $ docker inspect myubuntu | grep IPAddress
                "SecondaryIPAddresses": null,
                "IPAddress": "",
                        "IPAddress": "10.254.249.3",
    ```
  * もうちょっとちゃんとしたやつ
    ```bash
    $ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' myubuntu
    10.254.249.2
    ```

### mysql

```
mysql> select user, host from mysql.user;
+---------------+-----------------------------+
| user          | host                        |
+---------------+-----------------------------+
| root          | %                           |
| test_user2    | 192.168.100.0/255.255.255.0 |
| test_user1    | 192.168.100.2               |
| test_user3    | 192.168.200.2               |
| mysql.session | localhost                   |
| mysql.sys     | localhost                   |
| root          | localhost                   |
+---------------+-----------------------------+
7 rows in set (0.01 sec)
```

### ubuntu1

```
% docker exec -it ubuntu1 /bin/bash
root@7d2cb3701690:/# hostname -i
192.168.100.2
root@7d2cb3701690:/# mysql -h 192.168.100.3 -u test_user3 -p
Enter password:
ERROR 1045 (28000): Access denied for user 'test_user3'@'192.168.100.2' (using password: NO)
root@7d2cb3701690:/# mysql -h 192.168.100.3 -u test_user2 -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 5.7.39 MySQL Community Server (GPL)
...

mysql> exit
Bye
root@7d2cb3701690:/# mysql -h 192.168.100.3 -u test_user1 -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 5.7.39 MySQL Community Server (GPL)
...
mysql>
```

### ubuntu2


### references

* [MySQLの接続元ホストをサブネットマスクで制限する方法 - Qiita]( https://qiita.com/hypermkt/items/fd4c34a1916ef9006ef6 )