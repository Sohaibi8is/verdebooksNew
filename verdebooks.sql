-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 30, 2022 at 01:51 AM
-- Server version: 5.7.38
-- PHP Version: 7.3.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `addatsco_verdebooks`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `jobTitle` varchar(1000) NOT NULL,
  `status` varchar(100) NOT NULL,
  `hireDate` varchar(200) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `workingLocation` varchar(1000) NOT NULL,
  `accountHolder` varchar(100) NOT NULL,
  `bankName` varchar(100) NOT NULL,
  `accountNumber` varchar(100) NOT NULL,
  `branchName` varchar(1000) NOT NULL,
  `bankLocation` varchar(1000) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `town` varchar(500) NOT NULL,
  `postalCode` varchar(100) NOT NULL,
  `phn` varchar(100) NOT NULL,
  `phn2` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `notes` varchar(1600) NOT NULL,
  `mi` varchar(1500) NOT NULL,
  `payRate` varchar(1000) NOT NULL,
  `payType` varchar(100) NOT NULL,
  `vacPolicy` varchar(100) NOT NULL,
  `deduction` varchar(500) NOT NULL,
  `paymentMethod` varchar(100) NOT NULL,
  `email` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `jobTitle`, `status`, `hireDate`, `dob`, `workingLocation`, `accountHolder`, `bankName`, `accountNumber`, `branchName`, `bankLocation`, `address`, `town`, `postalCode`, `phn`, `phn2`, `gender`, `notes`, `mi`, `payRate`, `payType`, `vacPolicy`, `deduction`, `paymentMethod`, `email`) VALUES
(7, 'Sohaib', 'Developer', 'Active', '2020-12-20', '2000-12-20', 'Karachi', 'Sohaib', 'BAHL', '8888', 'BAHL', 'Karachi', 'PECHS', 'Karachi', '74800', '3332140546', '3332140546', 'male', 'abc abc abc abc abc', '8888', '20', 'weekly', '0.04', '0', 'bank', 'sohaib@i8is.com'),
(8, 'Muslim', 'Developer', 'Active', '2020-12-20', '2000-12-20', 'Karachi', 'Sohaib', 'BAHL', '8888', 'BAHL', 'Karachi', 'GULSHAN', 'Karachi', '74800', '3332222141', '3332222141', 'male', 'abc abc abc abc abc', '8888', '20', 'weekly', '0.04', '0', 'bank', 'muslim@i8is.com'),
(11, 'Mansoor', 'Developer', 'Active', '2020-12-20', '2000-12-20', 'Karachi', 'Sohaib', 'BAHL', '8888', 'BAHL', 'Karachi', 'Karachi', 'Karachi', '74800', '3332222141', '3332222141', 'male', 'abc abc abc abc abc', '8888', '20', 'weekly', '0.04', '0', 'bank', 'muslim@i8is.com');

-- --------------------------------------------------------

--
-- Table structure for table `stubs`
--

CREATE TABLE `stubs` (
  `id` int(11) NOT NULL,
  `generateDate` varchar(100) DEFAULT NULL,
  `payDate` varchar(100) DEFAULT NULL,
  `name` varchar(1000) NOT NULL,
  `RegCurrent` varchar(100) NOT NULL DEFAULT '0',
  `YTD` varchar(100) NOT NULL DEFAULT '0',
  `OTHours` varchar(100) NOT NULL DEFAULT '0',
  `OTRate` varchar(100) NOT NULL DEFAULT '0',
  `OTCurrent` varchar(100) NOT NULL DEFAULT '0',
  `OTYTD` varchar(100) NOT NULL DEFAULT '0',
  `VACCurrent` varchar(100) NOT NULL DEFAULT '0',
  `VACYTD` varchar(100) NOT NULL DEFAULT '0',
  `StatHours` varchar(100) NOT NULL DEFAULT '0',
  `StatRate` varchar(100) NOT NULL DEFAULT '0',
  `StatYTD` varchar(100) NOT NULL DEFAULT '0',
  `IncomeTax` varchar(100) NOT NULL DEFAULT '0',
  `IncomeTaxYTD` varchar(100) NOT NULL DEFAULT '0',
  `EI` varchar(100) NOT NULL DEFAULT '0',
  `EIYTD` varchar(100) NOT NULL DEFAULT '0',
  `CPP` varchar(100) NOT NULL DEFAULT '0',
  `CPPYTD` varchar(100) NOT NULL DEFAULT '0',
  `TotalPayCurrent` varchar(100) NOT NULL DEFAULT '0',
  `TotalPayYTD` varchar(100) NOT NULL DEFAULT '0',
  `TotalTaxCurrent` varchar(100) NOT NULL DEFAULT '0',
  `TotalTaxYTD` varchar(100) NOT NULL DEFAULT '0',
  `NetPay` varchar(100) NOT NULL DEFAULT '0',
  `employeeId` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `weekStart` varchar(100) NOT NULL,
  `weekEnd` varchar(100) NOT NULL,
  `regHours` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stubs`
--

INSERT INTO `stubs` (`id`, `generateDate`, `payDate`, `name`, `RegCurrent`, `YTD`, `OTHours`, `OTRate`, `OTCurrent`, `OTYTD`, `VACCurrent`, `VACYTD`, `StatHours`, `StatRate`, `StatYTD`, `IncomeTax`, `IncomeTaxYTD`, `EI`, `EIYTD`, `CPP`, `CPPYTD`, `TotalPayCurrent`, `TotalPayYTD`, `TotalTaxCurrent`, `TotalTaxYTD`, `NetPay`, `employeeId`, `status`, `weekStart`, `weekEnd`, `regHours`) VALUES
(11, '2022-04-29', '2020-12-30', 'Sohaib', '300.0', '0.0', '0.0', '30.0', '0.0', '0.0', '12.0', '24.0', '0.0', '20.0', '40.0', '16.766000000000002', '33.532000000000004', '5.2456000000000005', '10.491200000000001', '10.491200000000001', '36.188', '332.0', '664.0', '40.1056', '80.2112', '291.8944', '7', 'original', '2020-12-21', '2020-12-27', 0),
(9, '2022-04-29', '0', 'Muslim', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1.5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', 'initial', '0', '0', 0),
(10, '2022-04-29', '2019-12-30', 'Muslim', '300.0', '0.0', '0.0', '30.0', '0.0', '0.0', '12.0', '12.0', '0.0', '20.0', '20.0', '16.766000000000002', '16.766000000000002', '5.2456000000000005', '5.2456000000000005', '5.2456000000000005', '18.094', '332.0', '332.0', '40.1056', '40.1056', '291.8944', '8', 'original', '2021-12-21', '2021-12-27', 0),
(7, '2022-04-28', '0', 'Sohaib', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', 'initial', '0', '0', 0),
(8, '2022-04-28', '2019-12-30', 'Sohaib', '300.0', '0.0', '0.0', '30.0', '0.0', '0.0', '12.0', '12.0', '0.0', '0', '20.0', '16.766000000000002', '16.766000000000002', '5.2456000000000005', '5.2456000000000005', '5.2456000000000005', '18.094', '332.0', '332.0', '40.1056', '40.1056', '291.8944', '7', 'original', '2021-12-21', '2021-12-27', 0),
(12, '2022-04-29', '2000-12-30', 'Sohaib', '300.0', '0.0', '0.0', '30.0', '0.0', '0.0', '12.0', '36.0', '0.0', '0.0', '60.0', '16.766000000000002', '50.298', '5.2456000000000005', '15.736800000000002', '15.736800000000002', '54.282000000000004', '332.0', '996.0', '40.1056', '120.3168', '291.8944', '7', 'original', '2000-12-21', '2000-12-27', 0),
(13, '2022-04-29', '2002-12-30', 'Sohaib', '300.0', '300.0', '0.0', '30.0', '0.0', '0.0', '12.0', '48.0', '0.0', '0.0', '80.0', '16.766000000000002', '67.06400000000001', '5.2456000000000005', '20.982400000000002', '20.982400000000002', '72.376', '332.0', '1328.0', '40.1056', '160.4224', '291.8944', '7', 'original', '2002-12-21', '2002-12-27', 15),
(14, '2022-04-29', '0', 'Mansoor', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1.5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '11', 'initial', '0', '0', 0),
(15, '2022-04-29', '2002-12-30', 'Mansoor', '300.0', '300.0', '0.0', '30.0', '0.0', '0.0', '12.0', '12.0', '0.0', '0.0', '20.0', '16.766000000000002', '16.766000000000002', '5.2456000000000005', '5.2456000000000005', '5.2456000000000005', '18.094', '332.0', '332.0', '40.1056', '40.1056', '291.8944', '11', 'original', '2002-12-21', '2002-12-27', 15),
(16, '2022-04-30', '2005-12-30', 'Mansoor', '300.0', '600.0', '0.0', '30.0', '0.0', '0.0', '12.0', '24.0', '0.0', '0.0', '40.0', '16.766000000000002', '33.532000000000004', '5.2456000000000005', '10.491200000000001', '10.491200000000001', '36.188', '332.0', '664.0', '40.1056', '80.2112', '291.8944', '11', 'original', '2005-12-21', '2005-12-27', 15),
(17, '2022-04-30', '2006-12-30', 'Sohaib', '400.0', '700.0', '0.0', '30.0', '0.0', '0.0', '16.0', '64.0', '0.0', '0.0', '100.0', '22.018', '89.08200000000001', '6.888800000000001', '27.8712', '27.8712', '96.138', '436.0', '1764.0', '52.668800000000005', '213.09120000000001', '383.33119999999997', '7', 'original', '2006-12-21', '2006-12-27', 20),
(18, '2022-04-30', '2006-12-30', 'Muslim', '200.0', '200.0', '0.0', '30.0', '0.0', '0.0', '8.0', '20.0', '0.0', '0.0', '40.0', '11.514000000000001', '28.28', '3.6024000000000003', '8.848', '8.848', '30.520000000000003', '228.0', '560.0', '27.5424', '67.648', '200.4576', '8', 'original', '2006-12-21', '2006-12-27', 10),
(19, '2022-04-30', '2006-12-30', 'Mansoor', '600.0', '1200.0', '0.0', '30.0', '0.0', '0.0', '24.0', '48.0', '0.0', '0.0', '60.0', '32.522000000000006', '66.054', '10.1752', '20.666400000000003', '20.666400000000003', '71.286', '644.0', '1308.0', '77.79520000000001', '158.0064', '566.2048', '11', 'original', '2006-12-21', '2006-12-27', 30);

-- --------------------------------------------------------

--
-- Table structure for table `usersData`
--

CREATE TABLE `usersData` (
  `id` int(11) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `password` varchar(15000) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usersData`
--

INSERT INTO `usersData` (`id`, `email`, `password`, `status`) VALUES
(1, 'sohaib@i8is.com', 'sohaib123', 'verified');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stubs`
--
ALTER TABLE `stubs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usersData`
--
ALTER TABLE `usersData`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `stubs`
--
ALTER TABLE `stubs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `usersData`
--
ALTER TABLE `usersData`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
