# RedBus-Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit
## Introduction
  * The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

## Domain 
  * TRANSPORTATION

## Project Scope

**Data Extraction**
  * Scrape bus route information including bus name, type, departure time, duration, arrival time, rating, price, and seat availability.Automate navigation through multiple pages and states on the Redbus website.

**Automation**

  * Utilize Selenium for automated web scraping, handling multi-page navigation and state-wise data retrieval.

**Data Storage**

  * Store all extracted data in a structured SQL database to ensure scalability and easy retrieval.

**Visualization**

  * Implement a Streamlit application to allow users to explore and visualize bus route data, filter by attributes like price, star rating, and bus name, and provide analytical insights.

## SKILL-TAKEAWAY
* Python scripting,Selenium,Data Collection,Data Management using SQL,Streamlit
  
## TECHNOLOGY USED
* Python 3.9.I
* MySQL 8.0
* Streamlit
* Selenium

# Solution Overview
The project consists of four key components:

**OOPs**
  * Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions or logic. These objects are instances of classes, which encapsulate data and methods to manipulate that data. OOP promotes modularity, reusability, and scalability.

**Web Scraping**
  * Selenium is a powerful tool for automating web browsers, which is especially useful for web scraping tasks. If you want to retrieve bus details from RedBus, you can use Selenium to automate the process of searching for buses and extracting the relevant information. This involves interacting with web elements like input fields and buttons, waiting for the page to load, and extracting the desired details from the search results.

**SQL Database Integration**
  * The scraped data transformed into pandas dataframes and stored in an MySQL database by creating a table. With the help of MySQL, the data was inserted into the respective tables. The database could be accessed and managed in the MySQL environment. Data integrity is ensured by handling duplicates and database schema design tailored for efficient query performance.

**Streamlit App Development**
  * With the help of Streamlit, you can create an interactive user-friendly application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices.

# OOPs

1.**Design**
  * Each component of the project (web scraping, database interaction, application logic) can be encapsulated in separate classes, making the code more organized.

2.**Code Reusability**
  * By using Class, Common methods like connecting to the database or handling browser interactions can be reused across various objects.

3.**Ease of Maintenance**
  * Encapsulation ensures that changes to one part of the code (e.g., web scraping logic) do not impact other parts.

# Web Scraping Process

1.**Initialize Web Driver**
  * Open the browser using Selenium and navigate to the Redbus website, maximizing the window for efficient interaction.

2.**Load Target Web Page**
  * Navigate to the specific state or route page, managing page loading delays dynamically.

3.**Scrape Bus Routes**
  * Extract all bus route links and names, managing pagination to capture data from all available routes.

4.**Scrape Bus Details**
  * For each bus route, extract detailed information such as bus name, type, departure time, duration, arrival time, star rating, price, and seat availability.

5.**Error Handling**
  * Implement robust error handling for missing elements, page loading failures, and logging errors for debugging.

# SQL Database Integration

1.**Database Setup**
  * Create a structured SQL database with appropriate tables to store bus route and schedule information.

2.**Data Insertion**
  * Insert the scraped data into the SQL database, ensuring data integrity and handling duplicates or errors.

# Streamlit App Development

1.**Database Connection**
  * Establish a secure connection between the Streamlit app and the SQL database.

2.**Data Querying**
  * Efficiently query the database to fetch bus route information for visualization and analysis.

3.**Data Filtering**
  * Allow users to filter bus routes based on price, rating, and bus name using Streamlit’s interactive components.

# Conclusion
The "Redbus Data Scraping and Filtering with Streamlit Application" project offers a robust and scalable solution for automating the extraction, storage, and analysis of bus route data. By leveraging web scraping and visualization technologies, this project enables streamlined travel planning, market analysis, and data-driven decision-making within the transportation industry. The Streamlit app further enhances user experience, providing interactive and customizable data exploration tools.
