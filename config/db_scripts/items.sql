CREATE TABLE `items` (
  `uuid` varchar(128) NOT NULL,
  `name` varchar(80) NOT NULL,
  `price` float NOT NULL,
  `imageURL` varchar(512) DEFAULT NULL,
  `description` text,
  `storeUuid` varchar(128) NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `name` (`name`),
  KEY `storeUuid` (`storeUuid`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`storeUuid`) REFERENCES `stores` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ciAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci