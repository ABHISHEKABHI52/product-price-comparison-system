# Product Price Comparison System

A comprehensive Python system to compare product prices across multiple shops, identify the cheapest and most expensive sellers, and visualize price differences clearly.

## Features

### Data Cleaning
- Handles missing prices automatically
- Converts prices to numeric values
- Removes invalid or duplicate records
- Validates required columns

### Filtering
- Filter by product name (case-insensitive partial match)
- Filter by shop name (case-insensitive partial match)
- Filter by price range (min/max)

### Price Comparison
For each product, the system identifies:
- **Cheapest seller** and price
- **Most expensive seller** and price
- **Minimum price**
- **Maximum price**
- **Average price**
- **Price difference** (max - min)
- **Standard deviation** of prices

### Statistics
Provides comprehensive statistics with clear explanations:
- Mean (average price)
- Minimum (lowest price)
- Maximum (highest price)
- Standard deviation (price variability)
- Median (middle value)
- Total products, shops, and records

### Visualization
- **Bar Chart**: Compares prices of a single product across shops
  - Highlights cheapest price in green
  - Highlights most expensive price in red
  - Shows all prices with value labels
- **Boxplot**: Shows price distribution per product (optional)

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from price_comparison_system import PriceComparisonSystem

# Load data from CSV
system = PriceComparisonSystem(data_path='product_prices.csv')

# Or use a DataFrame directly
system = PriceComparisonSystem(df=your_dataframe)

# Get overall statistics
stats = system.get_statistics()
system.print_statistics(stats)

# Compare prices for all products
comparison_df = system.compare_prices()
system.print_comparison_summary(comparison_df)

# Visualize a specific product
system.plot_product_comparison('P001')
```

### Filtering Examples

```python
# Filter by product name
filtered = system.filter_data(product_name='Laptop')

# Filter by shop name
filtered = system.filter_data(shop_name='TechMart')

# Filter by price range
filtered = system.filter_data(price_min=50, price_max=200)

# Combine filters
filtered = system.filter_data(
    product_name='Laptop',
    price_min=1000,
    price_max=1500
)

# Analyze filtered data
comparison_df = system.compare_prices(filtered)
```

### Running the Main Script

```bash
python price_comparison_system.py
```

This will:
1. Load data from `product_prices.csv` (or create sample data if not found)
2. Display overall statistics
3. Show price comparison summary for all products
4. Generate visualizations

## Input Data Format

The system expects a CSV file or DataFrame with the following columns:

- `product_id`: Unique identifier for each product
- `product_name`: Name of the product
- `shop_name`: Name of the shop/store
- `price`: Price of the product (numeric)

Example:
```csv
product_id,product_name,shop_name,price
P001,Laptop Pro 15,TechMart,1199.99
P001,Laptop Pro 15,ElectroWorld,1249.50
P002,Wireless Mouse,TechMart,24.99
```

## Output

### Console Output
- Data cleaning summary
- Overall statistics with explanations
- Price comparison summary for each product showing:
  - Cheapest shop and price
  - Most expensive shop and price
  - Price difference
  - Average price and standard deviation

### Visualizations
- Bar charts saved or displayed
- Boxplots showing price distributions

## Code Quality

- **Modular Design**: Clean separation of concerns with a class-based structure
- **Clear Variable Names**: Self-documenting code
- **Inline Comments**: Explains logic and functionality
- **Type Hints**: Improves code readability and IDE support
- **Error Handling**: Graceful handling of missing data and edge cases
- **Reproducible**: Uses random seeds for sample data generation

## Statistics Explained

- **Mean**: Average price across all products and shops
- **Minimum**: Lowest price found in the entire dataset
- **Maximum**: Highest price found in the entire dataset
- **Standard Deviation**: Measure of price variability (higher = more price variation)
- **Median**: Middle value when all prices are sorted
- **Price Difference**: Range between cheapest and most expensive price for a product

## Example Output

```
================================================================================
PRICE COMPARISON SUMMARY
================================================================================

Product: Laptop Pro 15 (ID: P001)
  Cheapest Shop: TechMart - $1150.00
  Most Expensive Shop: ElectroWorld - $1250.00
  Price Difference: $100.00
  Average Price: $1200.00
  Price Range: $1150.00 - $1250.00
  Standard Deviation: $50.00
  Available in 4 shop(s)
```

## License

This project is provided as-is for educational and commercial use.


