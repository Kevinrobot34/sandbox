INSERT INTO time_series (time_series_id, date, value) 
VALUES (1, '2020-01-01', 1111), 
       (1, '2020-02-01', 2222),
       (1, '2020-05-01', 555),
       (2, '2020-02-01', 20000)
ON duplicate key update value = VALUES(value);
SELECT * FROM time_series;