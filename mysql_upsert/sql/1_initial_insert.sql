INSERT INTO time_series (time_series_id, date, value) 
VALUES (1, '2020-01-01', 110), 
       (1, '2020-02-01', 220),
       (1, '2020-03-01', 330),
       (1, '2020-04-01', 440),
       (2, '2020-01-01', 1000), 
       (2, '2020-02-01', 2000),
       (2, '2020-03-01', 3000);
SELECT * FROM time_series;