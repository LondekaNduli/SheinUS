# Shein E-Commerce Data Analysis
##Overview

An in-depth analysis of e-commerce data from Shein, one of the largest online fashion retailers.The goal of the analysis is to gain insights into the relationship between product categories, pricing, discounts, and other variables that might influence customer purchasing behavior.

#Data Description

These are the datasets used in this analysis:

Product Category: The main category to which the product belongs (e.g., Clothing, Accessories).

Price: The price at which the product is listed.

Discount: The percentage discount offered on the product.

Rank: A numeric value representing the rank or popularity of the product.

Additional Features: Other features that might include product-specific details such as color, size, and promotional information.

##Analysis Performed

Data Cleaning and Preprocessing:

Handled missing values by filling them with 0 for numerical columns.

Fixed inconsistencies in product category names by standardizing them.

Merged and renamed columns for better clarity and analysis.

##Exploratory Data Analysis:

Correlation Analysis: A correlation matrix was created to explore the relationships between variables such as price, discount, and rank. This helped identify key variables that influence pricing strategies.

Mean Price Analysis by Category: An interactive bar chart was created to visualize the average price for each product category, revealing pricing trends across different categories.
Regression Analysis:

A regression model was built to explore the relationship between product price and other factors like discount percentage, participation in Black Friday sales, and product rank. This helped in understanding the pricing dynamics.

##Visualization:

Created interactive visualizations using Plotly to enable dynamic exploration of the data. This includes an interactive bar chart of mean prices by category and correlation matrix .

##The Key Findings

Pricing Strategies: The analysis showed significant correlations between discounts and product pricing, highlighting how discounts are used across different categories to drive sales.

Category Insights: Some categories have higher average prices, reflecting either a premium product offering or higher demand.

Regression Insights: The regression model indicated that discounts and product rankings have a measurable impact on pricing strategies.

##Applications used

Python: For data processing, analysis, and visualization.

Pandas: For data manipulation and analysis.

Seaborn & Plotly: For creating both static and interactive visualizations.

Streamlit: To create an interactive web app for displaying the analysis.
