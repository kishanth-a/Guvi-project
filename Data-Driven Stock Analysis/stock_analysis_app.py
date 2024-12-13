import streamlit as st
import pandas as pd
import plotly.express as px


# Streamlit app configuration
st.set_page_config(page_title="Stock Market Analysis Dashboard", layout="wide")
st.title("Stock Market Analysis Dashboard")

# Load the dataset
df = pd.read_csv("D:\\Kishanth\\Guvi Project\\Data-Driven Stock Analysis\\data\\Extracted_data\\overall_data.csv")

# Define functions for different visualizations
def volatility_analysis():
    df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
    volatility = df.groupby('Ticker')['daily_return'].std().reset_index()
    volatility.columns = ['Ticker', 'Volatility']
    top_10_volatile = volatility.nlargest(10, 'Volatility')

    st.subheader("Volatility Analysis")
    fig = px.bar(
    top_10_volatile,
    x='Ticker',
    y='Volatility',
    labels={"Volatility":"Volatility", "Ticker": "Stock"},
    title="Top 10 Most Volatile Stocks",
    color='Volatility',
    color_continuous_scale='Reds'
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Volatility"),xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    if st.button("Back to Home"):
        st.session_state.page = "home"

def cumulative_return():
    df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return']).groupby(df['Ticker']).cumprod()

    top_5 = df.groupby('Ticker').cumulative_return.last().nlargest(5).index
    filtered_df = df[df['Ticker'].isin(top_5)]

    fig = px.line(
    filtered_df,
    x='date',
    y='cumulative_return',
    color='Ticker',
    title="Cumulative Return of Top 5 Stocks",
    labels={"cumulative_return":"Cumulative Return","date":"Date"}
    )
    st.plotly_chart(fig)

    if st.button("Back to Home"):
        st.session_state.page = "home"

def sector_performance():
    sector_data = pd.read_csv(f"D:\\Kishanth\\Guvi Project\\Data-Driven Stock Analysis\\data\\Sector_data - Sheet1.csv")

    # Splitting the column symbol and extract ticker
    sector_data["Ticker"] = sector_data["Symbol"].str.split(": ").str[1]

    # Taking Required columns
    sector_data = sector_data[["Ticker","COMPANY","sector"]]

    df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
    merged_df = pd.merge(df, sector_data, on="Ticker", how="left")
    merged_df['yearly_return'] = (1 + merged_df.groupby(['sector', 'Ticker'])['daily_return'].transform('mean')) - 1
    avg_performance = merged_df.groupby('sector')['yearly_return'].mean().reset_index()

    st.subheader("Sector-wise Performance")
    fig = px.bar(
    avg_performance,
    x='sector',
    y='yearly_return',
    labels={"yearly_return":"Yearly Return", "Ticker": "Stock"},
    color='yearly_return',
    color_continuous_scale='Greens'
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Yearly Return"),xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    if st.button("Back to Home"):
        st.session_state.page = "home"

def stock_correlation():
    pivot_df = df.pivot(index='date', columns='Ticker', values='close')
    correlation_matrix = pivot_df.corr()

    st.subheader("Stock Price Correlation")
    fig = px.imshow(
    correlation_matrix,
    text_auto=False,  # Display correlation values on the heatmap
    color_continuous_scale='RdBu',  # Choose a color scale
    labels=dict(x="Stock", y="Stock", color="Correlation"),
    title="Correlation Matrix of Stock Prices"
    )

    # Update layout (optional for styling)
    fig.update_layout(
        width=1000,  # Adjust width (in pixels)
        height=650,  # Adjust height (in pixels)
        xaxis=dict(tickmode='array', tickangle=45),  # Rotate x-axis labels
        yaxis=dict(tickmode='array')
    )

    st.plotly_chart(fig)

    if st.button("Back to Home"):
        st.session_state.page = "home"

def gainers_losers():
    df['monthly_return'] = df.groupby(['Ticker', 'month'])['close'].pct_change()
    grouped = df.groupby(['month', 'Ticker'])['monthly_return'].mean().reset_index()

    st.subheader("Top 5 Gainers and Losers (Month-wise)")
    months = df['month'].unique()
    selected_month = st.selectbox("Select Month", months)

    month_data = grouped[grouped['month'] == selected_month]
    top_gainers = month_data.nlargest(5, 'monthly_return')
    top_losers = month_data.nsmallest(5, 'monthly_return')

    st.write("### Top 5 Gainers")
    fig = px.bar(
    top_gainers,
    x='Ticker',
    y='monthly_return',
    labels={"monthly_return":"Monthly Return", "Ticker": "Stock"},
    color='monthly_return',
    color_continuous_scale='Greens'
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Monthly Return"),xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    st.write("### Top 5 Losers")
    fig = px.bar(
    top_losers,
    x='Ticker',
    y='monthly_return',
    labels={"monthly_return":"Monthly Return", "Ticker": "Stock"},
    color='monthly_return',
    color_continuous_scale='Reds'
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Monthly Return"),xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    if st.button("Back to Home"):
        st.session_state.page = "home"

def powerbi_dashboard():
    st.subheader("Power BI Dashboard")
    url = f"https://app.powerbi.com/links/JUUxGPVWMq?ctid=c6e549b3-5f45-4032-aae9-d4244dc5b2c4&pbi_source=linkShare" # It won't be visible as I don't have subscription
    st.markdown(f"[Click here to view the Power BI Dashboard]({url})")

    if st.button("Back to Home"):
        st.session_state.page = "home"

# Define the home page
def home():
    st.header("Welcome to the Stock Market Analysis Dashboard")
    st.write("This dashboard provides insights into the stock market performance of various companies.")
    st.sidebar.header("Home Page")
    st.sidebar.write("Select a visualization to explore:")

    yearly_returns = (
    df.sort_values(by="date")  # Sort data by date
    .groupby("Ticker")  # Group by stock name (assumed column is named Ticker)
    .apply(lambda group: pd.Series(
        {
        "yearly_return": ((group.iloc[-1]["close"] - group.iloc[0]["open"]) / group.iloc[0]["open"]) * 100
        }
                                  )
          )
    .reset_index()  # Reset index to convert the groupby object back to a DataFrame
    )

    top_10_green_stocks = yearly_returns.sort_values(by="yearly_return", ascending=False).reset_index(drop=True).head(10)
    top_10_red_stocks = yearly_returns.sort_values(by="yearly_return", ascending=True).reset_index(drop=True).head(10)
    

    st.subheader("Top 10 Green Stocks (Best Performers)")
    fig_green = px.bar(
    top_10_green_stocks,
    x='Ticker', 
    y='yearly_return',
    title="Top 10 Green Stocks",
    labels={"yearly_return": "Yearly Return", "Ticker": "Stock"},
    color='yearly_return',
    color_continuous_scale='Greens'
    )
    fig_green.update_layout(coloraxis_colorbar=dict(title="Yearly Return"),xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig_green)

    st.subheader("Top 10 Red Stocks (Worst Performers)")
    fig_red = px.bar(
    top_10_red_stocks,
    x='Ticker', 
    y='yearly_return',
    title="Top 10 Red Stocks",
    labels={"yearly_return": "Yearly Return", "Ticker": "Stock"},
    color='yearly_return',
    color_continuous_scale='Reds'
    )
    fig_red.update_layout(coloraxis_colorbar=dict(title="Yearly Return"),xaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_red)

    # Buttons for each visualization
    if st.sidebar.button("Volatility Analysis"):
        st.session_state.page = "volatility"

    if st.sidebar.button("Cumulative Return Over Time"):
        st.session_state.page = "cumulative_return"

    if st.sidebar.button("Sector-wise Performance"):
        st.session_state.page = "sector_performance"

    if st.sidebar.button("Stock Price Correlation"):
        st.session_state.page = "stock_correlation"

    if st.sidebar.button("Top Gainers & Losers"):
        st.session_state.page = "gainers_losers"

    if st.sidebar.button("Power BI - Dashboard"):
        st.session_state.page = "powerbi_dashboard"

# Navigation logic
# Initialize session state
if "page" not in st.session_state or st.session_state.page == "home":
    home()
elif st.session_state.page == "volatility":
    volatility_analysis()
elif st.session_state.page == "cumulative_return":
    cumulative_return()
elif st.session_state.page == "sector_performance":
    sector_performance()
elif st.session_state.page == "stock_correlation":
    stock_correlation()
elif st.session_state.page == "gainers_losers":
    gainers_losers()
elif st.session_state.page == "powerbi_dashboard":
    powerbi_dashboard()