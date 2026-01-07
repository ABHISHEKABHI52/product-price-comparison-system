# 💰 Product Price Comparison System

[![GitHub license](https://img.shields.io/github/license/ABHISHEKABHI52/product-price-comparison-system)](https://github.com/ABHISHEKABHI52/product-price-comparison-system/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-python-blue.svg)](https://www.python.org/)

## Overview

A comprehensive Python system to compare product prices across multiple shops, identify the cheapest and most expensive sellers, and visualize price differences clearly. This project includes both a powerful backend Python system and an interactive Streamlit web application for easy price comparison analysis.

### Key Features

✨ **Core Functionality:**
- 🛒 Compare prices for products across multiple shops
- 📊 Identify cheapest and most expensive sellers
- 📈 Calculate price statistics (mean, median, std deviation)
- 🔍 Filter by product name, shop name, and price range
- 💾 Support for CSV file uploads
- 📥 Download filtered results as CSV

✨ **Data Management:**
- 🧹 Automatic data cleaning and validation
- ❌ Remove duplicates and invalid prices
- ✅ Handle missing values gracefully
- 🏷️ Strip whitespace and normalize data

✨ **Visualizations:**
- 📊 Bar charts comparing prices by shop
- 📦 Boxplots showing price distributions
- 🎨 Color-coded pricing (green=cheapest, red=expensive)
- 📊 Interactive charts and statistics

✨ **Web Interface:**
- 🌐 Beautiful Streamlit web application
- 📱 Responsive design with intuitive UI
- ⚡ Real-time filtering and statistics
- 📥 Sample data for quick testing
- 🎯 Easy data upload functionality

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ABHISHEKABHI52/product-price-comparison-system.git
cd product-price-comparison-system
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**
```bash
streamlit run app.py
```

The application will open automatically at `http://localhost:8501`

## 📦 Project Structure

```
product-price-comparison-system/
├── price_comparison_system.py   # Main Python system
├── app.py                        # Streamlit web application
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
├── HOW_TO_RUN.md                # Installation & usage guide
└── LICENSE                       # MIT License
```

## 💻 System Requirements

- **Python:** 3.8 or higher
- **RAM:** 4GB minimum
- **Browser:** Chrome, Firefox, Edge, or Safari (modern version)
- **Operating System:** Windows, macOS, or Linux

## 📋 Dependencies

```
pandas>=1.3.0          # Data manipulation
numpy>=1.21.0          # Numerical operations
matplotlib>=3.4.0      # Data visualization
seaborn>=0.11.0        # Statistical visualizations
streamlit>=1.0.0       # Web application framework
```

## 🎯 Usage

### Web Application (Recommended)

1. Run `streamlit run app.py`
2. Choose data source (Upload CSV or Use Sample Data)
3. Apply filters (product, shop, price range)
4. View statistics and visualizations
5. Download filtered results

### Python Script

```python
from price_comparison_system import PriceComparisonSystem, create_sample_data

# Create system with sample data
sample_data = create_sample_data()
system = PriceComparisonSystem(df=sample_data)

# Get statistics
stats = system.get_statistics()
system.print_statistics(stats)

# Compare prices
comparison_df = system.compare_prices()
system.print_comparison_summary(comparison_df)

# Filter data
filtered = system.filter_data(productname='Laptop', price_max=1500)

# Visualize
system.plot_product_comparison('P001')
```

## 📊 CSV Format

Your CSV file should contain these columns:

| Column | Description | Example |
|--------|-------------|----------|
| productid | Unique product identifier | P001 |
| productname | Name of the product | Laptop Pro 15 |
| shopname | Name of the shop | TechMart |
| price | Product price (numeric) | 1199.99 |

**Example CSV:**
```csv
productid,productname,shopname,price
P001,Laptop Pro 15,TechMart,1199.99
P001,Laptop Pro 15,ElectroWorld,1249.50
P002,Wireless Mouse,TechMart,24.99
P002,Wireless Mouse,GadgetHub,26.50
P003,USB-C Cable,TechMart,9.99
P003,USB-C Cable,ElectroHub,11.50
```

## 📈 Features Explained

### Price Comparison
For each product, the system identifies:
- **Cheapest seller** and price
- **Most expensive seller** and price
- **Average price** across all shops
- **Price range** (min - max)
- **Standard deviation** (price variability)
- **Number of shops** selling the product

### Statistics
- **Mean:** Average price across all products
- **Median:** Middle value when prices are sorted
- **Min/Max:** Lowest and highest prices
- **Standard Deviation:** Price variability measure
- **Total Count:** Products, shops, and records

### Filtering
Filter data by:
- Product name (case-insensitive partial match)
- Shop name (case-insensitive partial match)
- Price range (min and max)
- Combine multiple filters

## 🎨 Visualizations

### Bar Charts
- Compare prices of a single product across shops
- Color-coded: Green (cheapest), Red (expensive), Blue (other)
- Value labels on each bar

### Boxplots
- Show price distribution per product
- Identify outliers and variations
- Compare across multiple products

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Abhishek Kumar**
- GitHub: [@ABHISHEKABHI52](https://github.com/ABHISHEKABHI52)
- Engineering Student | Full-Stack Developer | Data Science Enthusiast

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Uses [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data processing
- Visualizations powered by [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)

## 💡 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Historical price tracking
- [ ] Price alert notifications
- [ ] Multi-language support
- [ ] API integration for real-time prices
- [ ] Mobile app version
- [ ] Advanced analytics and ML predictions
- [ ] User authentication and profiles

## ❓ FAQ

**Q: How do I add my own data?**
A: Create a CSV file with the required columns (productid, productname, shopname, price) and upload it through the web app.

**Q: Can I use this for e-commerce?**
A: Yes! You can integrate this with web scraping to fetch real prices from online stores.

**Q: Is there a command-line interface?**
A: Yes! You can use the `price_comparison_system.py` directly in Python scripts.

**Q: How do I deploy this online?**
A: You can deploy the Streamlit app on Streamlit Cloud, Heroku, or AWS for free/cheap hosting.

## 📞 Support

For issues, questions, or suggestions, please:
1. Check the [HOW_TO_RUN.md](HOW_TO_RUN.md) file
2. Create an issue on [GitHub Issues](https://github.com/ABHISHEKABHI52/product-price-comparison-system/issues)
3. Contact via GitHub profile

## 📚 Documentation

For detailed setup and usage instructions, see [HOW_TO_RUN.md](HOW_TO_RUN.md)

---

**Made with ❤️ for price comparison and data analysis**
