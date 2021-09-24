CREATE TABLE `stores` (
  `uuid` varchar(128) NOT NULL,
  `name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `cif` varchar(9) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `userUuid` varchar(128) NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `cif` (`cif`),
  KEY `userUuid` (`userUuid`),
  CONSTRAINT `stores_ibfk_1` FOREIGN KEY (`userUuid`) REFERENCES `users` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci