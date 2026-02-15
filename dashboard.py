import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv("sales_data.csv")

# Data cleaning
df.fillna(0, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Aggregations
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
product_sales = df.groupby("Product")["Total_Sales"].sum()
region_sales = df.groupby("Region")["Total_Sales"].sum()

# Static Plot (Seaborn)
plt.figure(figsize=(8,5))
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")
plt.savefig("visualizations/boxplot.png")
plt.close()

# Interactive Plot (Plotly)
fig = px.line(
    monthly_sales.reset_index(),
    x="Month",
    y="Total_Sales",
    title="Monthly Sales Trend"
)

fig.write_html("visualizations/interactive_dashboard.html")

print("Dashboard generated successfully.")