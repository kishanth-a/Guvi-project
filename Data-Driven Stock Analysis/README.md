# Data-Driven Stock Analysis

## Project Overview
The **Data-Driven Stock Analysis** project provides a comprehensive visualization and analysis of Nifty 50 stocks' performance over the past year. This end-to-end data analysis project involves extracting, cleaning, analyzing, and visualizing stock data using tools like Python, Power BI, and Streamlit. It is designed to help investors, analysts, and enthusiasts make informed decisions based on stock performance trends.

## Features
- **Stock Performance Ranking**: Identify the top 10 best-performing stocks (green stocks) and the top 10 worst-performing stocks (red stocks).
- **Market Overview**: Summarize the overall market performance, including green vs. red stock ratios and average metrics.
- **Volatility Analysis**: Evaluate stock risk by calculating the standard deviation of daily returns.
- **Cumulative Return**: Visualize overall performance growth with cumulative return trends.
- **Sector-Wise Analysis**: Analyze performance by sector to gauge market sentiment in industries like IT, Financials, and Energy.
- **Correlation Analysis**: Display relationships between stock prices with a correlation heatmap.
- **Monthly Insights**: Showcase top 5 gainers and losers on a monthly basis.

## Tools & Technologies
- **Languages**: Python
- **Database**: MySQL
- **Visualization Tools**: Streamlit, Power BI
- **Libraries**: Pandas, Matplotlib, Seaborn, MySQL Connector

## Project Workflow
1. **Data Extraction**: Extracted data in YAML format for daily stock performance.
2. **Data Transformation**: Converted YAML data into a structured CSV format for 50 stock symbols.
3. **Data Cleaning**: Processed and validated data to ensure accuracy and completeness.
4. **Data Analysis**: Used Python and SQL to compute key metrics:
   - Top 10 Green Stocks
   - Top 10 Red Stocks
   - Average stock performance and volume
   - Volatility and cumulative returns
5. **Visualization**:
   - Power BI dashboards for dynamic insights.
   - Streamlit app for interactive analysis.

## Key Visualizations
1. **Volatility Analysis**:
   - Objective: Identify and visualize the most volatile stocks.
   - Visualization: Bar chart of the top 10 most volatile stocks.

2. **Cumulative Return Over Time**:
   - Objective: Showcase overall stock performance growth.
   - Visualization: Line chart of cumulative returns for the top 5 performing stocks.

3. **Sector-Wise Performance**:
   - Objective: Break down stock performance by sector.
   - Visualization: Bar chart of average yearly returns by sector.

4. **Stock Price Correlation**:
   - Objective: Understand relationships between stock prices.
   - Visualization: Heatmap of stock price correlations.

5. **Top 5 Gainers and Losers (Month-Wise)**:
   - Objective: Highlight monthly top-performing and worst-performing stocks.
   - Visualization: Monthly bar charts for gainers and losers.

## Repository Structure
```
📁 Guvi-project
├── 📁 Data-Driven Stock Analysis
│   ├── 📁 Extracted_data # This Folder contains the CSV file of overall and individual stocks data
│   ├── stock_analysis.ipynb  # Python notebook for data processing and analysis
│   ├── stock_analysis_visualization.pbix  # Power BI dashboard file
│   ├── Application_and_Dashboard_Demo.ppt # Streamlit Application and Power BI Dashboard Demo File
│   ├── sectors.csv  # Sector data mapping
│   └── README.md  # Documentation (this file)
```

## Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kishanth-a/Guvi-project.git
   ```
2. **Install Dependencies**:
   - Python libraries:
     ```bash
     pip install pandas matplotlib seaborn streamlit
     ```
   - Set up MySQL/PostgreSQL for the database.
3. **Run Power BI Dashboard**:
   - Open `stock_analysis_visualization.pbix` in Power BI Desktop.
4. **Run Streamlit App**:
   ```bash
   streamlit run stock_analysis_app.py
   ```

## Results
- **Interactive Dashboards**: Comprehensive insights into stock performance trends.
- **Enhanced Decision Support**: Tools for identifying opportunities and risks in the market.
- **Actionable Insights**: Visualizations for volatility, cumulative returns, sector performance, and more.

## Demo
Screenshots of key visualizations: Attached as PPT File
- **Power BI Dashboard**
- **Streamlit App**

## Author
**Kishanth Arunachalam**  
[GitHub Profile](https://github.com/kishanth-a)

---
Feel free to contribute to this project by submitting issues or pull requests.

