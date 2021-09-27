DROP TABLE IF EXISTS `time_series`;

CREATE TABLE `time_series` (
  `id` int AUTO_INCREMENT,
  `time_series_id` int NOT NULL,
  `date` date NOT NULL,
  `value` int NOT NULL,
  `created_at` DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
   PRIMARY KEY(`id`),
   UNIQUE `idx_ts_date` (time_series_id, date) -- UNIQUE KEY to use upsert
) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8mb4;

show index from time_series;