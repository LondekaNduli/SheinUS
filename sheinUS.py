#Import all needed libraries
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import altair as alt
import plotly.express as px

# Load the image
image = Image.open('sheinlogo.png')  # Update with your image path

# Create two columns
col1, col2 = st.columns([1, 2])  # The ratio [1, 2] controls the width of the columns

# Place the image in the left column
with col1:
    st.image(image)

# Place some text in the right column
with col2:
    st.write("""
    ## SHEIN ANALYTICS
     Make the beauty of fashion accessible to all,
     reimagining fashion by leveraging our small-batch on-demand production model.
    """)

#upload and read file as a table
df = pd.read_csv("shein_data.csv")
df

#create header
st.header("Let's Analyse")

# Create two columns
col1, col2 = st.columns([1, 2])  # The ratio [1, 2] controls the width of the columns

# Place the image in the left column
with col1:
    #unique values count
    st.write("Unique Value Counts")
    shein=df['product_title'].value_counts()
    shein

# Place some text in the right column
with col2:
    #group by column and get the price mean of each category
    st.write("Mean Price by Category")
    shein1=df.groupby('product_category')['price_usd'].mean()
    shein1

#create another header
st.header("Data Visualisation")
data = pd.read_csv('shein_data.csv')

# Group by category and calculate the mean price
category_price = data.groupby('product_category')['price_usd'].mean().reset_index()

# Create a bar chart using Plotly
fig = px.bar(
    category_price,
    x='product_category',
    y='price_usd',
    title='Mean Price by Category',
    labels={'product_category': 'Category', 'price_usd': 'Mean Price (USD)'},
    hover_data=['price_usd']
)

# Update the layout to ensure the category labels are readable
fig.update_layout(
    xaxis_tickangle=-45,  # Rotate category labels for better readability
    width=800,            # Set the width of the chart
    height=600            # Set the height of the chart
)

# Display the chart in Streamlit
st.plotly_chart(fig)


# Correlation matrix
corr_matrix =data[['price_usd', 'discount_%', 'blackfriday', 'rank_title_numeric']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")

# Regression Analysis
X =data[['discount_%', 'blackfriday', 'rank_title_numeric']]
y =data['price_usd']

# Add a constant to the model 
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Display the heatmap in Streamlit
st.pyplot(plt)

#Create sidebar
st.sidebar.markdown("<h3 style='display:inline-block'>Shein US purchase trends, counts of products being sold as per price, discounts and blackfriday promotions.</h3>", unsafe_allow_html=True)
st.sidebar.markdown("About Page<ol><li>Explore data</li><li>Data analysis</li><li>Visual data</li></ol>", unsafe_allow_html=True)

