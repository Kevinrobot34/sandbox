INSERT INTO time_series (time_series_id, date, value) 
VALUES (1, '2020-01-01', 1111), 
       (1, '2020-04-01', 440)
ON duplicate key update value = VALUES(value);