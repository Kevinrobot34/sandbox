select user(), current_user();

select user, host from mysql.user;

CREATE USER 'test_user1'@'192.168.100.2';
CREATE USER 'test_user2'@'192.168.100.0/24';
