import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Stock Market Analysis Dashboard")
st.sidebar.header("Visualization Options")

# Load the dataset
df = pd.read_csv(f"D:\\Kishanth\\Guvi Project\\Data-Driven Stock Analysis\\data\\Extracted_data\\overall_data.csv")

def volatility_analysis():
    df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
    volatility = df.groupby('Ticker')['daily_return'].std().reset_index()
    volatility.columns = ['Ticker', 'Volatility']
    top_10_volatile = volatility.nlargest(10, 'Volatility')

    st.subheader("Volatility Analysis")
    st.bar_chart(data=top_10_volatile.set_index('Ticker')['Volatility'],x_label="Stock",y_label="Volatility")

def cumulative_return():
    df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return']).groupby(df['Ticker']).cumprod()

    top_5 = df.groupby('Ticker').cumulative_return.last().nlargest(5).index
    filtered_df = df[df['Ticker'].isin(top_5)]

    st.subheader("Cumulative Return Over Time")
    for ticker in top_5:
        ticker_data = filtered_df[filtered_df['Ticker'] == ticker]
        st.header(ticker)
        st.line_chart(data=ticker_data.set_index('date')['cumulative_return'], height=300,x_label="Date",y_label="Cumulative Returns")

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
    st.bar_chart(data=avg_performance.set_index('sector')['yearly_return'],x_label="Sector",y_label="Yearly Return")

def stock_correlation():
    pivot_df = df.pivot(index='date', columns='Ticker', values='close')
    correlation_matrix = pivot_df.corr()

    st.subheader("Stock Price Correlation")
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, cmap='coolwarm', cbar=True, square=True)
    st.pyplot(plt.gcf())

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
    st.bar_chart(data=top_gainers.set_index('Ticker')['monthly_return'],x_label="Stock",y_label="Monthly Returns")

    st.write("### Top 5 Losers")
    st.bar_chart(data=top_losers.set_index('Ticker')['monthly_return'],x_label="Stock",y_label="Monthly Returns")

def powerbi_dashboard():
    st.subheader("Power BI Dashboard")
    url = f"https://app.powerbi.com/groups/me/reports/cc63a53c-e16c-4171-8cc9-fba8965e0a5f?ctid=c6e549b3-5f45-4032-aae9-d4244dc5b2c4&pbi_source=linkShare&bookmarkGuid=cda1afc8-ced3-41db-88ab-08ccc16d34a0"
    st.markdown(f"[Click here to view the Power BI Dashboard]({url})")

# Sidebar options
visualization = st.sidebar.radio(
    "Select Visualization:",
    (
        "Volatility Analysis",
        "Cumulative Return Over Time",
        "Sector-wise Performance",
        "Stock Price Correlation",
        "Top 5 Gainers and Losers (Month-wise)",
        "Power BI - Dashboard"
    ),
)

# Display the selected visualization
if visualization == "Volatility Analysis":
    volatility_analysis()
elif visualization == "Cumulative Return Over Time":
    cumulative_return()
elif visualization == "Sector-wise Performance":
    sector_performance()
elif visualization == "Stock Price Correlation":
    stock_correlation()
elif visualization == "Top 5 Gainers and Losers (Month-wise)":
    gainers_losers()
elif visualization == "Power BI - Dashboard":
    powerbi_dashboard()
