-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 27, 2022 at 03:57 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stutter`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio_data`
--

CREATE TABLE `audio_data` (
  `id` int(11) NOT NULL,
  `audio_path` tinytext NOT NULL,
  `timestamps` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `score` decimal(6,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `audio_data`
--

INSERT INTO `audio_data` (`id`, `audio_path`, `timestamps`, `created_at`, `score`) VALUES
(4, 'static/audio/4_0_08-03-2022_20:53.wav', NULL, '2022-03-09 12:29:52', '56.10'),
(4, 'static/audio/4_1_09-03-2022_00:14:1646765097.wav', NULL, '2022-03-09 00:14:57', NULL),
(5, 'static/audio/5_0_09-03-2022_10:57:1646803626.wav', NULL, '2022-03-09 10:57:06', NULL),
(4, 'static/audio/4_2_09-03-2022_11:03:1646804005.wav', NULL, '2022-03-09 12:23:59', NULL),
(4, 'static/audio/4_3_09-03-2022_11:10:1646804404.wav', NULL, '2022-03-09 11:10:04', NULL),
(4, 'static/audio/4_4_09-03-2022_11:13:1646804627.wav', NULL, '2022-03-09 11:13:47', NULL),
(4, 'static/audio/4_5_09-03-2022_11:17:1646804857.wav', NULL, '2022-03-09 11:17:37', NULL),
(4, 'static/audio/4_6_09-03-2022_11:19:1646804955.wav', NULL, '2022-03-09 11:19:15', NULL),
(4, 'static/audio/4_7_09-03-2022_11:22:1646805155.wav', NULL, '2022-03-09 11:22:35', NULL),
(4, 'static/audio/4_8_09-03-2022_11:24:1646805277.wav', NULL, '2022-03-09 12:16:15', NULL),
(4, 'qqqq', NULL, '2022-03-09 12:51:40', '63.45'),
(4, 'aa', NULL, '2022-03-09 12:51:52', '6.45'),
(4, 'xaa', NULL, '2022-03-09 12:52:04', '67.45'),
(4, 'xa', NULL, '2022-03-09 12:52:12', '47.45'),
(4, 'xa', NULL, '2022-03-11 11:05:22', '47.45'),
(4, 'gjhg', NULL, '2022-03-10 11:05:20', '63.45'),
(6, 'static/audio/6_0_10-03-2022_15:37:1646906830.wav', NULL, '2022-03-10 15:37:10', '51.22'),
(4, 'static/audio/4_15_15-03-2022_09:32:1647316952.wav', NULL, '2022-03-15 09:32:32', '51.22'),
(4, 'static/audio/4_16_15-03-2022_09:32:1647316957.wav', NULL, '2022-03-15 09:32:37', NULL),
(4, 'static/audio/4_17_15-03-2022_09:33:1647316981.wav', NULL, '2022-03-15 09:33:01', '51.22'),
(4, 'static/audio/4_18_15-03-2022_10:02:1647318721.wav', NULL, '2022-03-15 10:02:01', '37.50'),
(4, 'static/audio/4_19_15-03-2022_10:07:1647319027.wav', NULL, '2022-03-15 10:07:07', '42.69'),
(4, 'static/audio/4_20_15-03-2022_10:56:1647321993.wav', NULL, '2022-03-15 10:56:33', NULL),
(4, 'static/audio/4_21_15-03-2022_11:02:1647322333.wav', NULL, '2022-03-15 11:02:13', NULL),
(4, 'static/audio/4_22_15-03-2022_11:04:1647322497.wav', NULL, '2022-03-15 11:04:57', NULL),
(4, 'static/audio/4_23_15-03-2022_11:05:1647322511.wav', NULL, '2022-03-15 11:05:11', NULL),
(4, 'static/audio/4_24_15-03-2022_11:05:1647322550.wav', NULL, '2022-03-15 11:05:50', NULL),
(5, 'static/audio/5_1_21-03-2022_19:34:1647871458.wav', NULL, '2022-03-21 19:34:18', '14.00'),
(5, 'static/audio/5_2_21-03-2022_19:38:1647871709.wav', NULL, '2022-03-21 19:38:29', '22.75'),
(5, 'static/audio/5_3_21-03-2022_19:39:1647871783.wav', NULL, '2022-03-21 19:39:43', '50.00'),
(5, 'static/audio/5_4_21-03-2022_19:40:1647871851.wav', NULL, '2022-03-21 19:40:51', '32.44'),
(5, 'static/audio/5_5_21-03-2022_19:45:1647872139.wav', NULL, '2022-03-21 19:45:39', '51.22'),
(5, 'static/audio/5_6_21-03-2022_19:47:1647872253.wav', NULL, '2022-03-21 19:47:33', '51.22'),
(5, 'static/audio/5_7_21-03-2022_19:50:1647872405.wav', NULL, '2022-03-21 19:50:05', '51.22'),
(5, 'static/audio/5_8_21-03-2022_19:55:1647872741.wav', NULL, '2022-03-21 19:55:41', '57.45'),
(4, 'static/audio/4_25_21-03-2022_19:56:1647872771.wav', NULL, '2022-03-21 19:56:11', '51.22'),
(4, 'static/audio/4_26_21-03-2022_19:56:1647872788.wav', NULL, '2022-03-21 19:56:28', NULL),
(5, 'static/audio/5_9_21-03-2022_19:59:1647872971.wav', NULL, '2022-03-21 19:59:31', '65.83'),
(4, 'static/audio/4_27_21-03-2022_20:00:1647873003.wav', NULL, '2022-03-21 20:00:03', '51.22'),
(12, 'static/audio/12_0_22-03-2022_16:26:1647946609.wav', NULL, '2022-03-22 16:26:49', '44.00'),
(4, 'static/audio/4_28_22-03-2022_16:40:1647947426.wav', NULL, '2022-03-22 16:40:26', '51.22');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--


--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio_data`
--
ALTER TABLE `audio_data`
  ADD KEY `id` (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `audio_data`
--
ALTER TABLE `audio_data`
  ADD CONSTRAINT `audio_data_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
