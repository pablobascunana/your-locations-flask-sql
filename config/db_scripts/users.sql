CREATE TABLE `users` (
  `uuid` varchar(128) NOT NULL,
  `userName` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `loginAttempts` int NOT NULL,
  `registerDate` datetime NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `userName` (`userName`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci