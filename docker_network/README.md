
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


```
mysql -h 192.168.100.3 -u test_user1 -p
```