

『Linuxで動かしながら学ぶTCP/IPネットワーク入門』 ([Amazonリンク]( https://amzn.asia/d/4a7Nmkz )) を docker でセットアップして遊んだ際のメモ


## VSCode の DevContainers

* https://code.visualstudio.com/docs/devcontainers/tutorial
* https://code.visualstudio.com/docs/devcontainers/containers
* https://zenn.dev/streamwest1629/articles/vscode_wanderer-in-devcontainer


## ネットワークのコマンド

### ping

```bash
root@575e4ae2b207:/workspaces/tcp_ip_linux# ping -c 3 8.8.8.8 
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=36 time=7.84 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=36 time=8.58 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=36 time=5.34 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2008ms
rtt min/avg/max/mdev = 5.342/7.254/8.584/1.386 ms
```

### ip

`ip address show`

```bash
root@575e4ae2b207:/workspaces/tcp_ip_linux# ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
3: ip6tnl0@NONE: <NOARP> mtu 1452 qdisc noop state DOWN group default qlen 1000
    link/tunnel6 :: brd ::
52: eth0@if53: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:12:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.18.0.2/16 brd 172.18.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```


### tcpdump

```bash
root@575e4ae2b207:/workspaces/tcp_ip_linux# tcpdump -tn -i any icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked v1), capture size 262144 bytes
IP 172.18.0.2 > 8.8.8.8: ICMP echo request, id 4, seq 1, length 64
IP 8.8.8.8 > 172.18.0.2: ICMP echo reply, id 4, seq 1, length 64
IP 172.18.0.2 > 8.8.8.8: ICMP echo request, id 4, seq 2, length 64
IP 8.8.8.8 > 172.18.0.2: ICMP echo reply, id 4, seq 2, length 64
IP 172.18.0.2 > 8.8.8.8: ICMP echo request, id 4, seq 3, length 64
IP 8.8.8.8 > 172.18.0.2: ICMP echo reply, id 4, seq 3, length 64
^C
6 packets captured
6 packets received by filter
0 packets dropped by kernel
```


## References

* https://www.engilaboo.com/network-introduction-by-docker/
* https://zenn.dev/kawa1214/books/5888c6b3554ffa