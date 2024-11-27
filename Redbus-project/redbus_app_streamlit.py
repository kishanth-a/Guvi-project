import pandas as pd
import streamlit as st
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kichoo@25",
    database="GUVI_PROJECT",
    autocommit=True
)
mycursor = mydb.cursor()

# Fetch bus routes data from MySQL
sql = "SELECT * FROM BUS_DETAILS"
mycursor.execute(sql)
data = mycursor.fetchall()

# Create a DataFrame with actual column names
columns = [desc[0] for desc in mycursor.description]
df = pd.DataFrame(data, columns=columns)

# Ensure numeric columns have correct data types
df["Seats_available"] = pd.to_numeric(df["Seats_available"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce").astype(float)
df["Star_ratings"] = pd.to_numeric(df["Star_ratings"], errors="coerce").astype(float)

# Convert timedelta to HH:MM format
df["Departure_time"] = df["Departure_time"].apply(lambda x: f"{int(x.total_seconds() // 3600):02d}:{int((x.total_seconds() % 3600) // 60):02d}")
df["Arrival_time"] = df["Arrival_time"].apply(lambda x: f"{int(x.total_seconds() // 3600):02d}:{int((x.total_seconds() % 3600) // 60):02d}")


# Drop rows with invalid (NaN) values in important columns
df = df.dropna(subset=["Seats_available", "Price", "Star_ratings"])


# Streamlit application
st.header("REDBUS - Application")

# Sidebar to navigate between pages
page = st.sidebar.radio("Select Page", ["Home", "Bus Details"])

# Home Page
if page == "Home":
    st.image(f"D:\\Kishanth\\Redbus_Project\\redbus_img.jpg", width=650)
    st.write(f"Click here to know more: [REDBUS](https://www.redbus.in//)")

# Bus Details Page
elif page == "Bus Details":
    st.header(" REDBUS - Bus Route and Details")

    # Sidebar filters
    st.sidebar.header("Filters")

    # Step 1: Select State
    state_names = df["State"].unique()  # Updated from "State_name" to "State"
    selected_state_name = st.sidebar.selectbox("Select State Name", options=state_names)

    # Step 2: Filter route names based on the selected state
    filter_routes_by_state = df[df["State"] == selected_state_name]  # Filter routes for the selected state
    

    # Step 3: Select Route Name
    route_names = filter_routes_by_state["Route_name"].unique()  # Get unique routes in the selected state
    selected_route_name = st.sidebar.selectbox("Select Route Name", options=[""]+route_names)

    # Step : Filter by Bus Type (in the main frame with an empty option)
    bus_types = filter_routes_by_state["Bus_type"].unique()  # Get unique bus types in the selected state
    selected_bus_type = st.sidebar.selectbox("Select Bus Type", options=[""] + list(bus_types), index=0)
    filter_routes_by_bus_type = filter_routes_by_state[filter_routes_by_state["Bus_type"] == selected_bus_type] if selected_bus_type else filter_routes_by_state

    # Step : Filter by Departing Time (Start_time) (in the main frame with an empty option)
    start_times = filter_routes_by_bus_type["Departure_time"].unique()    
    selected_start_time = st.sidebar.selectbox("Select Departure Time", options=[""] + list(start_times), index=0)

    # Step : Price range filter
    min_price, max_price = st.sidebar.slider("Price Range", 
                                              min_value=int(filter_routes_by_state["Price"].min()), 
                                              max_value=int(filter_routes_by_state["Price"].max()), 
                                              value=(int(filter_routes_by_state["Price"].min()), int(filter_routes_by_state["Price"].max())))


    # Step : Availability filter (Seats Available)
    min_seats, max_seats = st.sidebar.slider("Seats Available", 
                                              min_value=int(filter_routes_by_state["Seats_available"].min()), 
                                              max_value=int(filter_routes_by_state["Seats_available"].max()), 
                                              value=(int(filter_routes_by_state["Seats_available"].min()), int(filter_routes_by_state["Seats_available"].max())))

    # Step : Ratings range filter
    min_rating, max_rating = st.sidebar.slider("Ratings Range", 
                                                min_value=1.0, 
                                                max_value=5.0, 
                                                value=(1.0, 5.0), 
                                                step=0.1)

    # Display the filter data based on the sidebar inputs
    filter_data = filter_routes_by_state

    # Filter the data only if both Bus Type and Start Time are selected (non-empty)
    if selected_bus_type and selected_start_time:
        filter_data = filter_routes_by_bus_type[
            (filter_routes_by_bus_type["Route_name"] == selected_route_name) &
            (filter_routes_by_bus_type["Bus_type"] == selected_bus_type) &
            (filter_routes_by_bus_type["Departure_time"] == selected_start_time) &
            (filter_routes_by_bus_type["Price"].between(min_price, max_price)) &
            (filter_routes_by_bus_type["Star_ratings"].between(min_rating, max_rating)) &
            (filter_routes_by_bus_type["Seats_available"].between(min_seats, max_seats))
        ]

    elif selected_bus_type:
        filter_data = filter_routes_by_bus_type[
            (filter_routes_by_bus_type["Route_name"] == selected_route_name) &
            (filter_routes_by_bus_type["Bus_type"] == selected_bus_type) &
            (filter_routes_by_bus_type["Price"].between(min_price, max_price)) &
            (filter_routes_by_bus_type["Star_ratings"].between(min_rating, max_rating)) &
            (filter_routes_by_bus_type["Seats_available"].between(min_seats, max_seats))
        ]

    elif selected_start_time:
        filter_data = filter_routes_by_bus_type[
            (filter_routes_by_bus_type["Route_name"] == selected_route_name) &
            (filter_routes_by_bus_type["Departure_time"] == selected_start_time) &
            (filter_routes_by_bus_type["Price"].between(min_price, max_price)) &
            (filter_routes_by_bus_type["Star_ratings"].between(min_rating, max_rating)) &
            (filter_routes_by_bus_type["Seats_available"].between(min_seats, max_seats))
        ]
        
    else:
        filter_data = filter_routes_by_bus_type[
            (filter_routes_by_bus_type["Route_name"] == selected_route_name) &
            (filter_routes_by_bus_type["Price"].between(min_price, max_price)) &
            (filter_routes_by_bus_type["Star_ratings"].between(min_rating, max_rating)) &
            (filter_routes_by_bus_type["Seats_available"].between(min_seats, max_seats))
        ]

    # Display filter data if any results are found
    if not filter_data.empty:

        # Display the filter data
        st.dataframe(filter_data[["State","Bus_name","Bus_type","Departure_time","Arrival_time","Total_duration","Price","Seats_available","Star_ratings","Route_name","Route_link"]])
        st.write(f"Total results: {len(filter_data)}")

        # Adding text input fields for bus ID entry
        col1, col2 = st.columns(2)
        with col1:
            selected_bus_id_1 = st.text_input("Enter Bus ID 1 (row index)", value="")
        with col2:
            selected_bus_id_2 = st.text_input("Enter Bus ID 2 (row index)", value="")

        # Display comparison table if both IDs are entered
        if selected_bus_id_1 and selected_bus_id_2:
            try:
                bus_1 = filter_data.loc[int(selected_bus_id_1)]
                bus_2 = filter_data.loc[int(selected_bus_id_2)]

                # Create a comparison table
                comparison_data = {
                    "Attribute": ["Route Name", "Bus Name", "Bus Type", "Departure Time", "Arrival Time", "Price", "Ratings", "Seats Available"],
                    "Bus 1": [bus_1["Route_name"], bus_1["Bus_name"], bus_1["Bus_type"], bus_1["Departure_time"], bus_1["Arrival_time"], bus_1["Price"], bus_1["Star_ratings"], bus_1["Seats_available"]],
                    "Bus 2": [bus_2["Route_name"], bus_2["Bus_name"], bus_2["Bus_type"], bus_2["Departure_time"], bus_2["Arrival_time"], bus_2["Price"], bus_2["Star_ratings"], bus_2["Seats_available"]]
                }

                comparison_df = pd.DataFrame(comparison_data)

                # **COMPARISON TABLE**: Display the comparison table with a heading and increased size using st.table
                st.write("### COMPARISON TABLE")
                st.table(comparison_df)  # Display static table with full content
            except KeyError:
                st.write("Invalid Bus ID entered. Please enter valid IDs from the filter data.")
    else:
        st.write("### No results found for the selected filters.")

# Close the cursor and connection
mycursor.close()
mydb.close()

