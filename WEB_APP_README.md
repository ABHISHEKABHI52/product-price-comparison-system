# Product Price Comparison System - Web Application

A modern, interactive web application built with Streamlit for comparing product prices across multiple shops.

## 🚀 Quick Start

### Installation

1. Install all required packages:
```bash
pip install -r requirements.txt
```

### Running the Web App

Simply run:
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## ✨ Features

### 📊 Data Management
- **Upload CSV**: Upload your own product price data
- **Sample Data**: Load pre-generated sample data for testing
- **Automatic Data Cleaning**: Handles missing values, invalid prices, and duplicates

### 🔍 Interactive Filtering
- Filter by **Product Name** (dropdown selection)
- Filter by **Shop Name** (dropdown selection)
- Filter by **Price Range** (slider)
- All filters work together seamlessly

### 📈 Real-time Statistics
- **Mean Price**: Average across all products
- **Min/Max Price**: Lowest and highest prices
- **Standard Deviation**: Price variability measure
- **Total Products, Shops, Records**: Dataset overview

### 📊 Visualizations
- **Bar Charts**: Compare prices for individual products
  - Green bars = Cheapest price
  - Red bars = Most expensive price
  - Blue bars = Other shops
- **Boxplots**: Price distribution across all products

### 💾 Data Export
- View raw filtered data
- Download filtered data as CSV

## 📋 CSV Format

Your CSV file should contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `product_id` | Unique product identifier | P001 |
| `product_name` | Name of the product | Laptop Pro 15 |
| `shop_name` | Name of the shop/store | TechMart |
| `price` | Product price (numeric) | 1199.99 |

### Example CSV:
```csv
product_id,product_name,shop_name,price
P001,Laptop Pro 15,TechMart,1199.99
P001,Laptop Pro 15,ElectroWorld,1249.50
P002,Wireless Mouse,TechMart,24.99
P002,Wireless Mouse,GadgetHub,26.50
```

## 🎯 Usage Guide

### Step 1: Load Data
1. Open the sidebar (click the arrow on the left)
2. Choose either:
   - **Upload CSV**: Click "Browse files" and select your CSV
   - **Use Sample Data**: Click "Load Sample Data"
3. Click the load button

### Step 2: Apply Filters (Optional)
- Select a product from the dropdown
- Select a shop from the dropdown
- Adjust the price range slider
- Click "Apply Filters"

### Step 3: Explore Results
- View overall statistics in the metrics cards
- Check the price comparison table
- Select a product to see detailed visualizations
- Expand "View Raw Data" to see the filtered dataset

### Step 4: Export Data (Optional)
- Click "View Raw Data" expander
- Click "Download Filtered Data as CSV"

## 🖥️ System Requirements

- Python 3.8 or higher
- 4GB RAM minimum
- Modern web browser (Chrome, Firefox, Edge, Safari)

## 📦 Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **matplotlib**: Plotting library
- **seaborn**: Statistical visualization

## 🔧 Troubleshooting

### App won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

### CSV upload fails
- Verify your CSV has the required columns: `product_id`, `product_name`, `shop_name`, `price`
- Check that price column contains numeric values
- Ensure CSV is properly formatted (no special characters in headers)

### No data showing after filtering
- Reset filters by selecting "All" for product and shop
- Adjust price range slider to include your data
- Check that your data matches the filter criteria

### Visualizations not displaying
- Make sure you have data loaded
- Select a product from the dropdown
- Check browser console for errors (F12)

## 🎨 Customization

The web app uses Streamlit's default theme. You can customize it by:

1. Creating a `.streamlit/config.toml` file
2. Adding theme settings:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## 📝 Notes

- The app automatically cleans data upon loading
- Filters are applied in real-time
- All visualizations are interactive
- Data is stored in session state (cleared on refresh)

## 🆘 Support

For issues or questions:
1. Check the console output for error messages
2. Verify your data format matches the requirements
3. Try loading sample data to test if the app works

## 🚀 Deployment

To deploy this app:

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Other Platforms
- **Heroku**: Use Procfile with `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **Docker**: Create Dockerfile with Streamlit
- **AWS/GCP/Azure**: Use container services

Enjoy comparing prices! 💰

