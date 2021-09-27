# mysql_upsert

## Overview

MySQLでupsertするためには `INSERT ON DUPLICATE KEY UPDATE` 構文を使う。

> ON DUPLICATE KEY UPDATE を指定したとき、**UNIQUEインデックス** または **PRIMARY KEY** に重複した値を発生させる行が挿入された場合は、MySQL によって古い行の UPDATE が実行されます。

## Important points

* UNIQUEインデックスを適切に用意しておくこと
  * ``UNIQUE `idx_ts_date` (time_series_id, date)`` が対応
* UPDATE文の中では `VALUES` 関数を使うと良い感じに更新できる

## Execution

```bash
$ make exec_sql SQL=0_schema.sql
docker container exec -it -e MYSQL_PWD=test 589c02372432 \
                bash -c 'cat /sql/0_schema.sql | mysql -u root mysql_sandbox'
Table   Non_unique      Key_name        Seq_in_index    Column_name     Collation       Cardinality     Sub_part        Packed  Null    Index_type      Comment Index_comment
time_series     0       PRIMARY 1       id      A       0       NULL    NULL            BTREE
time_series     0       idx_ts_date     1       time_series_id  A       0       NULL    NULL            BTREE
time_series     0       idx_ts_date     2       date    A       0       NULL    NULL            BTREE

$ make exec_sql SQL=1_initial_insert.sql
docker container exec -it -e MYSQL_PWD=test 589c02372432 \
                bash -c 'cat /sql/1_initial_insert.sql | mysql -u root mysql_sandbox'
id      time_series_id  date    value   created_at      updated_at
1       1       2020-01-01      110     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
2       1       2020-02-01      220     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
3       1       2020-03-01      330     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
4       1       2020-04-01      440     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
5       2       2020-01-01      1000    2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
6       2       2020-02-01      2000    2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
7       2       2020-03-01      3000    2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563

$ make exec_sql SQL=2_upsert.sql
docker container exec -it -e MYSQL_PWD=test 589c02372432 \
                bash -c 'cat /sql/2_upsert.sql | mysql -u root mysql_sandbox'
id      time_series_id  date    value   created_at      updated_at
1       1       2020-01-01      1111    2021-09-27 09:55:51.015563      2021-09-27 09:55:54.202394
2       1       2020-02-01      2222    2021-09-27 09:55:51.015563      2021-09-27 09:55:54.202394
3       1       2020-03-01      330     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
4       1       2020-04-01      440     2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
5       2       2020-01-01      1000    2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
6       2       2020-02-01      20000   2021-09-27 09:55:51.015563      2021-09-27 09:55:54.202394
7       2       2020-03-01      3000    2021-09-27 09:55:51.015563      2021-09-27 09:55:51.015563
8       1       2020-05-01      555     2021-09-27 09:55:54.202394      2021-09-27 09:55:54.202394

```

## References

* [Docs - 13.2.5.3 INSERT ... ON DUPLICATE KEY UPDATE 構文]( https://dev.mysql.com/doc/refman/5.6/ja/insert-on-duplicate.html )
