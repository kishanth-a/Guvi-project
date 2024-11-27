from Redbus_data_scrapping_using_Selenium import dataframe
import pandas as pd
import mysql.connector

# Importing the DataFrame from the data scraping file
bus_df = dataframe


# --- Data Cleaning and Transformation ---

# Formatting the "Departure_time" and "Arrival_time" columns to a uniform time format (HH:MM)
bus_df["Departure_time"] = pd.to_datetime(bus_df["Departure_time"],format="%H:%M").dt.strftime("%H:%M")
bus_df["Arrival_time"] = pd.to_datetime(bus_df["Arrival_time"],format="%H:%M").dt.strftime("%H:%M")

# Cleaning and converting the "Ratings" column
# Splitting the string to extract the numeric rating and converting it to a float
bus_df['Ratings'] = bus_df['Ratings'].str.split('\n').str[0]
bus_df['Ratings'] = pd.to_numeric(bus_df['Ratings'], errors='coerce').fillna(0).astype(float)

# Extracting numeric value for "Seats_available" and converting it to an integer
bus_df['Seats_available'] = bus_df['Seats_available'].str.split().str[0].astype(int)


# Converting the "Price" column to float and rounding to two decimal places
bus_df['Price']=bus_df['Price'].astype(float).round(2)

# Converting DataFrame to CSV file
bus_df.to_csv(f"D:\\Kishanth\\Redbus_Project\\cleaned_data.csv",index=False)


# --- SQL Connection Setup ---

# Establishing a connection to the MySQL database
try:
    conn=mysql.connector.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password="Kichoo@25",  # Database password
        database="dummydb"     # Default database (optional here as the next command selects a specific one)
        )
    my_cursor = conn.cursor()

    print("Database Connection Established Successfully")

    # Create a database if it doesn't exist
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS GUVI_PROJECT")
    print("Database created successfully")

    # Use the created or existing database
    my_cursor.execute("USE GUVI_PROJECT")

    # Create the "bus_details" table if it doesn't exist
    my_cursor.execute('''CREATE TABLE IF NOT EXISTS bus_details(
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    State VARCHAR(255) NOT NULL,
                    Bus_name TEXT NOT NULL,
                    Bus_type TEXT NOT NULL,
                    Departure_time TIME NOT NULL,
                    Arrival_time TIME NOT NULL,
                    Total_duration TEXT NOT NULL,
                    Price DECIMAL(10,2) NULL,
                    Seats_available INT NOT NULL,
                    Star_ratings Float NULL,
                    Route_name TEXT NULL,
                    Route_link TEXT NULL
                    )''')
    
    print("Table Created successfully")

except mysql.connector.Error as err:
    # Catch any errors during the database connection or table creation process
    print(f"Error: {err}")

# --- Insert Data into the Table ---

# SQL query to insert data into the bus_details table
insert_query = '''INSERT INTO bus_details(
                    State,
                    Bus_name,
                    Bus_type,
                    Departure_time,
                    Arrival_time,
                    Total_duration,
                    Price,
                    Seats_available,
                    Star_ratings,
                    Route_name,
                    Route_link)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

# Convert the DataFrame values into a list of lists for batch insertion
load_data = bus_df.values.tolist()

# Execute the insertion query for all the rows in the DataFrame
my_cursor.executemany(insert_query,load_data)

# Commit the transaction to save the changes to the database
conn.commit()

print("Values are inserted successfully")
