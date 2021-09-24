CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` float NOT NULL,
  `storeUuid` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `storeUuid` (`storeUuid`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`storeUuid`) REFERENCES `stores` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci