import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException


class BusDetails:
    # Class to scrape bus details for a given state
    
    def __init__(self, state, state_link):
        # Initialize the object with state name and state-specific link

        self.state = state
        self.state_link = state_link
        self.driver = None

    def get_driver(self,page_link):
        # Set up the Selenium WebDriver and navigate to the provided page

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(page_link)
        
    def get_bus_details(self,df):
        # Extract bus details from the website

        # Initialize empty lists to store extracted data
        State_Names = []
        Route_name = []
        Bus_name = []
        Bus_type = []
        Departure_time = []
        Arrival_time = []
        Ratings = []
        Travel_duration = []
        Price = []
        Seats_available = []
        Route_link = []

        # Loop through the DataFrame containing routes and links
        for i,r in df.iterrows():
            cur_state = r["State"] # Extract state name
            route=r["Route_name"] # Extract route name
            link=r["Route_link"] # Extract route link
            
            # Launch the driver for the specific route link
            self.get_driver(page_link=link)
            time.sleep(3)

            # Click each relevant element on the page
            elements = self.driver.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")  
            for element in elements: 
                element.click()   
                time.sleep(2)   
                
            # Handle optional elements, such as a "button" for expanding details
            try:
                clicks = self.driver.find_element(By.XPATH, "//div[@class='button']")  
                clicks.click()  
            except:
                continue  

            time.sleep(2)

            # Implement infinite scrolling logic to load all data
            scrolling = True
            while scrolling:
                current_page = self.driver.page_source  # Capture the current page content  
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()  # Scroll down
                time.sleep(5)  
                next_page = self.driver.page_source   # Capture the new page content
                if next_page == current_page:
                    scrolling = False  # Stop scrolling if no new content is loaded               

            # Extract specific bus details from the page
            bus_name = self.driver.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']") 
            bus_type = self.driver.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")  
            start_time = self.driver.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
            end_time = self.driver.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
            total_duration = self.driver.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
            price = self.driver.find_elements(By.XPATH, '//div[@class="fare d-block"]//span')
            seats = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

            try:
                rating = self.driver.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
            except:
                continue

            # Append the extracted details to respective lists
            for bus in bus_name:
                Bus_name.append(bus.text)
                Route_link.append(link)
                Route_name.append(route)
                State_Names.append(cur_state)
            for bus_type_elem in bus_type:
                Bus_type.append(bus_type_elem.text)
            for start_time_elem in start_time:
                Departure_time.append(start_time_elem.text)
            for end_time_elem in end_time:
                Arrival_time.append(end_time_elem.text)
            for total_duration_elem in total_duration:
                Travel_duration.append(total_duration_elem.text)
            for ratings in rating:
                Ratings.append(ratings.text)
            for price_elem in price:
                Price.append(price_elem.text)
            for seats_elem in seats:
                Seats_available.append(seats_elem.text)

        # Close the WebDriver after processing
        self.driver.quit()

        # Create a DataFrame with the extracted data
        data_df = pd.DataFrame(
            {
                "State" : State_Names,
                "Bus_name" : Bus_name,
                "Bus_type" : Bus_type,
                "Departure_time" : Departure_time,
                "Arrival_time" : Arrival_time,
                "Total_duration" : Travel_duration,
                "Price" : Price,
                "Seats_available" : Seats_available,
                "Ratings" : Ratings,
                "Route_name" : Route_name,
                "Route_link" : Route_link
            }
        )

        return data_df


    def get_route_and_link(self):
        # Extract routes and corresponding links for a specific state

        self.get_driver(page_link=self.state_link)
        time.sleep(3)

        links = [] # To store route links
        routes = [] # To store route names
        
        # Use WebDriverWait for dynamic content loading
        wait = WebDriverWait(self.driver, 20)
        
        # Retrieve route links from multiple pages
        while True:
            try:
                # Extract route names and links
                path = self.driver.find_elements(By.XPATH, "//a[@class='route']")   
                for link in path:  
                    links.append(link.get_attribute("href"))
                
                for route in path:
                    routes.append(route.text)  
                
                # Handle pagination logic to navigate through pages
                try:
                    # Get the active page number
                    active_page_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='DC_117_pageTabs DC_117_pageActive']")))
                    active_page_number = active_page_element.text #the pagination has numbers in it...that number is stored by using .text in active_page_number 
                    next_page_number = str(int(active_page_number) + 1)  #converting the page number str to int +1 then converting to str
                    
                    # Locate the next page button
                    next_page_button_xpath = f"//div[@class='DC_117_paginationTable']//div[text()='{next_page_number}']"  
                    next_page_button = self.driver.find_element(By.XPATH, next_page_button_xpath) 
                    
                    # Scroll into view and click
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)  
                    time.sleep(2)  
                    
                    try:
                        next_page_button.click()
                    except ElementNotInteractableException:
                        self.driver.execute_script("arguments[0].click();", next_page_button)  
                    
                    print(f"Navigating to page {next_page_number}")
                    time.sleep(10) 
                except (NoSuchElementException, TimeoutException):
                    print("No more pages to paginate") 
                    break
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                break
        
        # Close the WebDriver after extracting all routes
        self.driver.quit()

        # Create a DataFrame with the extracted routes and links
        route_df = pd.DataFrame({
            "State":self.state,
            "Route_name":routes,
            "Route_link":links
        })
        return self.get_bus_details(route_df)

# Dictionary containing state names and their corresponding links
bus_detail_list = {
    "Andhra":"https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile",
    "Kerala":"https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile",
    "Telangana":"https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile",
    "Bihar":"https://www.redbus.in/online-booking/bihar-state-road-transport-corporation-bsrtc/?utm_source=rtchometile",
    "South Bengal":"https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile",
    "Himachal Pradesh":"https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile",
    "Assam":"https://www.redbus.in/online-booking/astc/?utm_source=rtchometile",
    "West Bengal":"https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile",
    "Uttar Pradesh":"https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile",
    "Punjab":"https://www.redbus.in/online-booking/pepsu/?utm_source=rtchometile",
    "Goa":"https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile",
    "Rajasthan":"https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile",
    "Chandigarh":"https://www.redbus.in/online-booking/chandigarh-transport-undertaking-ctu/?utm_source=rtchometile",
    "Jammu and Kashmir":"https://www.redbus.in/online-booking/jksrtc/?utm_source=rtchometile"
    }

objects={} # Dictionary to store BusDetails objects for each state
all_df = [] # List to store DataFrames for all states

# Iterate through the states and retrieve bus details
for state_name,link in bus_detail_list.items():
    objects[state_name] = BusDetails(state=state_name,state_link=link)
    state_df = objects[state_name].get_route_and_link()
    all_df.append(state_df)

# Combine all state DataFrames into one
dataframe = pd.concat(all_df,ignore_index=True)
dataframe.to_csv(f"D:\\Kishanth\\Redbus_Project\\scraped_data.csv",index=False)

