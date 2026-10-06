# Cryptocurrency Price Tracker

## Project Information

**Student Name:** R. L. Jayapriya  
**Roll Number:** 512223149018  
**Team:** Team 2  

---

## 1. Project Title

# Cryptocurrency Price Tracker

A Python-based web scraping project that collects real-time cryptocurrency information from CoinMarketCap and stores the collected data in a CSV file.

The project uses Selenium WebDriver to open CoinMarketCap, extract cryptocurrency information from the webpage, process the collected data, and save it for further analysis.

---

## 2. Problem Statement

Cryptocurrency prices change continuously and it can be difficult to manually monitor the prices and market information of multiple cryptocurrencies.

The purpose of this project is to develop an automated Cryptocurrency Price Tracker that can:

- Automatically access cryptocurrency market data.
- Collect cryptocurrency names.
- Extract current cryptocurrency prices.
- Extract 24-hour price changes.
- Collect market capitalization information.
- Record the timestamp when the data is collected.
- Store the collected information in a CSV file.
- Filter cryptocurrency data based on price changes.
- Display the collected information through the program output.

This reduces the need for manually checking cryptocurrency websites and provides a structured dataset that can be used for further analysis.

---

## 3. Objective

The main objective of this project is to build an automated cryptocurrency data collection system using Python and Selenium.

The project aims to:

1. Automate cryptocurrency data collection.
2. Retrieve cryptocurrency information from CoinMarketCap.
3. Extract the top cryptocurrencies from the webpage.
4. Capture cryptocurrency price information.
5. Capture 24-hour percentage changes.
6. Capture market capitalization information.
7. Add a timestamp to every collected record.
8. Store the collected data in CSV format.
9. Filter the collected cryptocurrency information.
10. Provide a simple and reusable project structure.

---

## 4. Features

### 4.1 Automated Web Scraping

The project uses Selenium WebDriver to automatically open CoinMarketCap and retrieve cryptocurrency information.

### 4.2 Cryptocurrency Data Collection

The scraper collects information such as:

- Cryptocurrency Name
- Price
- 24H Change
- Market Cap
- Timestamp

### 4.3 Top Cryptocurrency Tracking

The project is configured to collect a limited number of cryptocurrencies instead of processing the entire webpage.

The current configuration collects the top 10 cryptocurrency records.

### 4.4 Timestamp

Every scraped record is stored with the date and time at which the data was collected.

Example:

```text
2026-10-06 14
