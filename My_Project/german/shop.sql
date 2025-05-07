-- MySQL dump 10.13  Distrib 9.0.1, for macos15.1 (arm64)
--
-- Host: localhost    Database: shop
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `cap_color` varchar(50) DEFAULT NULL,
  `order_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'Ананасы',3,'Иван Иванов','ivan@example.com','1234567890','ул. Ленина, 1',NULL,'2024-10-26 09:20:19'),(2,'Яблоки',5,'Петр Петров','petr@example.com','0987654321','ул. Красная, 2',NULL,'2024-10-26 09:20:19'),(3,'Ананасы',1,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd',NULL,'2024-10-26 09:28:28'),(4,'Ананасы',1,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd',NULL,'2024-10-26 09:36:30'),(5,'Ананасы',1,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd',NULL,'2024-10-26 09:37:24'),(6,'Ананасы',1,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd',NULL,'2024-10-29 21:04:33'),(7,'Ананасы',1,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd','rh','2024-10-29 21:32:46'),(8,'Ананасы',2,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd','Желтый','2024-10-29 21:36:04'),(9,'Ананасы',4,'Bogdan','bogdan.speaker@gmail.com','+38 (067) 110 26 26','dd','Красный','2024-10-30 09:03:54');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-06 14:30:18
