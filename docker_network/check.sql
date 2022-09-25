select user(), current_user();

select user, host from mysql.user;

CREATE USER 'test_user1'@'192.168.100.2';
CREATE USER 'test_user2'@'192.168.100.0/255.255.255.0';
CREATE USER 'test_user3'@'192.168.200.2';
