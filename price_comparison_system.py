"""
Product Price Comparison System

A comprehensive system to compare product prices across multiple shops,
identify cheapest and most expensive sellers, and visualize price differences.

Author: Senior Data Engineer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, Dict, List
import warnings

warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class PriceComparisonSystem:
    """
    Main class for product price comparison system.
    Handles data loading, cleaning, filtering, analysis, and visualization.
    """
    
    def __init__(self, data_path: Optional[str] = None, df: Optional[pd.DataFrame] = None):
        """
        Initialize the Price Comparison System.
        
        Parameters:
        -----------
        data_path : str, optional
            Path to CSV file containing product price data
        df : pd.DataFrame, optional
            DataFrame with product price data
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Either data_path or df must be provided")
        
        # Clean data upon initialization
        self.df = self.clean_data(self.df)
        
        # Validate required columns
        required_columns = ['product_id', 'product_name', 'shop_name', 'price']
        missing_columns = [col for col in required_columns if col not in self.df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the input data by handling missing values, converting prices,
        and removing invalid or duplicate records.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Raw input dataframe
            
        Returns:
        --------
        pd.DataFrame
            Cleaned dataframe
        """
        df = df.copy()
        
        # Remove completely duplicate records
        initial_count = len(df)
        df = df.drop_duplicates()
        duplicates_removed = initial_count - len(df)
        if duplicates_removed > 0:
            print(f"Removed {duplicates_removed} duplicate record(s)")
        
        # Convert price to numeric, handling errors
        # This will convert non-numeric values to NaN
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        
        # Remove rows with missing prices
        missing_prices_before = df['price'].isna().sum()
        df = df.dropna(subset=['price'])
        if missing_prices_before > 0:
            print(f"Removed {missing_prices_before} record(s) with missing prices")
        
        # Remove rows with invalid prices (negative or zero)
        invalid_prices_before = len(df[df['price'] <= 0])
        df = df[df['price'] > 0]
        if invalid_prices_before > 0:
            print(f"Removed {invalid_prices_before} record(s) with invalid prices (<= 0)")
        
        # Remove rows with missing product_id, product_name, or shop_name
        required_fields = ['product_id', 'product_name', 'shop_name']
        for field in required_fields:
            missing_count = df[field].isna().sum()
            if missing_count > 0:
                df = df.dropna(subset=[field])
                print(f"Removed {missing_count} record(s) with missing {field}")
        
        # Convert product_id to string for consistency
        df['product_id'] = df['product_id'].astype(str)
        
        # Strip whitespace from string columns
        string_columns = ['product_name', 'shop_name']
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
        
        print(f"Data cleaning complete. Final dataset: {len(df)} records")
        return df.reset_index(drop=True)
    
    def filter_data(self, 
                   product_name: Optional[str] = None,
                   shop_name: Optional[str] = None,
                   price_min: Optional[float] = None,
                   price_max: Optional[float] = None) -> pd.DataFrame:
        """
        Filter the dataset based on product name, shop name, and price range.
        
        Parameters:
        -----------
        product_name : str, optional
            Filter by product name (case-insensitive partial match)
        shop_name : str, optional
            Filter by shop name (case-insensitive partial match)
        price_min : float, optional
            Minimum price threshold
        price_max : float, optional
            Maximum price threshold
            
        Returns:
        --------
        pd.DataFrame
            Filtered dataframe
        """
        filtered_df = self.df.copy()
        
        # Filter by product name (case-insensitive)
        if product_name:
            filtered_df = filtered_df[
                filtered_df['product_name'].str.contains(product_name, case=False, na=False)
            ]
        
        # Filter by shop name (case-insensitive)
        if shop_name:
            filtered_df = filtered_df[
                filtered_df['shop_name'].str.contains(shop_name, case=False, na=False)
            ]
        
        # Filter by price range
        if price_min is not None:
            filtered_df = filtered_df[filtered_df['price'] >= price_min]
        
        if price_max is not None:
            filtered_df = filtered_df[filtered_df['price'] <= price_max]
        
        return filtered_df.reset_index(drop=True)
    
    def compare_prices(self, filtered_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Compare prices for each product across shops.
        Identifies cheapest and most expensive sellers, calculates statistics.
        
        Parameters:
        -----------
        filtered_df : pd.DataFrame, optional
            Filtered dataframe to analyze. If None, uses full dataset.
            
        Returns:
        --------
        pd.DataFrame
            Comparison results with statistics for each product
        """
        if filtered_df is None:
            filtered_df = self.df
        
        # Group by product and calculate statistics
        comparison_results = []
        
        for product_id in filtered_df['product_id'].unique():
            product_data = filtered_df[filtered_df['product_id'] == product_id]
            product_name = product_data['product_name'].iloc[0]
            
            # Find cheapest and most expensive shops
            min_price_idx = product_data['price'].idxmin()
            max_price_idx = product_data['price'].idxmax()
            
            cheapest_shop = product_data.loc[min_price_idx, 'shop_name']
            cheapest_price = product_data.loc[min_price_idx, 'price']
            
            most_expensive_shop = product_data.loc[max_price_idx, 'shop_name']
            most_expensive_price = product_data.loc[max_price_idx, 'price']
            
            # Calculate statistics
            min_price = product_data['price'].min()
            max_price = product_data['price'].max()
            avg_price = product_data['price'].mean()
            price_diff = max_price - min_price
            std_price = product_data['price'].std()
            shop_count = len(product_data)
            
            comparison_results.append({
                'product_id': product_id,
                'product_name': product_name,
                'cheapest_shop': cheapest_shop,
                'cheapest_price': cheapest_price,
                'most_expensive_shop': most_expensive_shop,
                'most_expensive_price': most_expensive_price,
                'min_price': min_price,
                'max_price': max_price,
                'avg_price': avg_price,
                'price_difference': price_diff,
                'std_price': std_price,
                'shop_count': shop_count
            })
        
        return pd.DataFrame(comparison_results)
    
    def get_statistics(self, filtered_df: Optional[pd.DataFrame] = None) -> Dict:
        """
        Calculate overall statistics for the dataset.
        
        Parameters:
        -----------
        filtered_df : pd.DataFrame, optional
            Filtered dataframe to analyze. If None, uses full dataset.
            
        Returns:
        --------
        dict
            Dictionary containing statistical measures
        """
        if filtered_df is None:
            filtered_df = self.df
        
        prices = filtered_df['price']
        
        stats = {
            'mean': prices.mean(),
            'min': prices.min(),
            'max': prices.max(),
            'std': prices.std(),
            'median': prices.median(),
            'total_products': filtered_df['product_id'].nunique(),
            'total_shops': filtered_df['shop_name'].nunique(),
            'total_records': len(filtered_df)
        }
        
        return stats
    
    def print_comparison_summary(self, comparison_df: pd.DataFrame, 
                                product_id: Optional[str] = None):
        """
        Print a summary of price comparisons to console.
        
        Parameters:
        -----------
        comparison_df : pd.DataFrame
            DataFrame from compare_prices() method
        product_id : str, optional
            Specific product_id to summarize. If None, summarizes all products.
        """
        if product_id:
            comparison_df = comparison_df[comparison_df['product_id'] == product_id]
            if len(comparison_df) == 0:
                print(f"No data found for product_id: {product_id}")
                return
        
        print("\n" + "="*80)
        print("PRICE COMPARISON SUMMARY")
        print("="*80)
        
        for _, row in comparison_df.iterrows():
            print(f"\nProduct: {row['product_name']} (ID: {row['product_id']})")
            print(f"  Cheapest Shop: {row['cheapest_shop']} - ${row['cheapest_price']:.2f}")
            print(f"  Most Expensive Shop: {row['most_expensive_shop']} - ${row['most_expensive_price']:.2f}")
            print(f"  Price Difference: ${row['price_difference']:.2f}")
            print(f"  Average Price: ${row['avg_price']:.2f}")
            print(f"  Price Range: ${row['min_price']:.2f} - ${row['max_price']:.2f}")
            print(f"  Standard Deviation: ${row['std_price']:.2f}")
            print(f"  Available in {int(row['shop_count'])} shop(s)")
        
        print("\n" + "="*80)
    
    def print_statistics(self, stats: Dict):
        """
        Print statistical summary with explanations.
        
        Parameters:
        -----------
        stats : dict
            Dictionary from get_statistics() method
        """
        print("\n" + "="*80)
        print("OVERALL STATISTICS")
        print("="*80)
        print(f"\nMean Price: ${stats['mean']:.2f}")
        print("  → Average price across all products and shops")
        
        print(f"\nMinimum Price: ${stats['min']:.2f}")
        print("  → Lowest price found in the entire dataset")
        
        print(f"\nMaximum Price: ${stats['max']:.2f}")
        print("  → Highest price found in the entire dataset")
        
        print(f"\nStandard Deviation: ${stats['std']:.2f}")
        print("  → Measure of price variability (higher = more price variation)")
        
        print(f"\nMedian Price: ${stats['median']:.2f}")
        print("  → Middle value when all prices are sorted")
        
        print(f"\nTotal Products: {stats['total_products']}")
        print("  → Number of unique products in the dataset")
        
        print(f"\nTotal Shops: {stats['total_shops']}")
        print("  → Number of unique shops in the dataset")
        
        print(f"\nTotal Records: {stats['total_records']}")
        print("  → Total number of price records")
        
        print("\n" + "="*80)
    
    def plot_product_comparison(self, product_id: str, 
                               filtered_df: Optional[pd.DataFrame] = None,
                               save_path: Optional[str] = None):
        """
        Create a bar chart comparing prices of a single product across shops.
        Highlights cheapest and most expensive prices.
        
        Parameters:
        -----------
        product_id : str
            Product ID to visualize
        filtered_df : pd.DataFrame, optional
            Filtered dataframe to use. If None, uses full dataset.
        save_path : str, optional
            Path to save the plot. If None, displays the plot.
        """
        if filtered_df is None:
            filtered_df = self.df
        
        product_data = filtered_df[filtered_df['product_id'] == product_id]
        
        if len(product_data) == 0:
            print(f"No data found for product_id: {product_id}")
            return
        
        # Sort by price for better visualization
        product_data = product_data.sort_values('price')
        product_name = product_data['product_name'].iloc[0]
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Get colors for bars (green for cheapest, red for most expensive, blue for others)
        colors = []
        min_price = product_data['price'].min()
        max_price = product_data['price'].max()
        
        for price in product_data['price']:
            if price == min_price:
                colors.append('#2ecc71')  # Green for cheapest
            elif price == max_price:
                colors.append('#e74c3c')  # Red for most expensive
            else:
                colors.append('#3498db')  # Blue for others
        
        # Create bar chart
        bars = ax.bar(range(len(product_data)), product_data['price'], color=colors, alpha=0.7)
        
        # Customize the plot
        ax.set_xlabel('Shop', fontsize=12, fontweight='bold')
        ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
        ax.set_title(f'Price Comparison: {product_name}\n(Product ID: {product_id})', 
                    fontsize=14, fontweight='bold')
        ax.set_xticks(range(len(product_data)))
        ax.set_xticklabels(product_data['shop_name'], rotation=45, ha='right')
        
        # Add value labels on bars
        for i, (bar, price) in enumerate(zip(bars, product_data['price'])):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${price:.2f}',
                   ha='center', va='bottom', fontweight='bold')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#2ecc71', alpha=0.7, label='Cheapest'),
            Patch(facecolor='#e74c3c', alpha=0.7, label='Most Expensive'),
            Patch(facecolor='#3498db', alpha=0.7, label='Other Shops')
        ]
        ax.legend(handles=legend_elements, loc='upper right')
        
        # Add grid for better readability
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_price_distribution(self, product_id: Optional[str] = None,
                               filtered_df: Optional[pd.DataFrame] = None,
                               save_path: Optional[str] = None):
        """
        Create a boxplot showing price distribution per product.
        
        Parameters:
        -----------
        product_id : str, optional
            Specific product ID. If None, shows all products.
        filtered_df : pd.DataFrame, optional
            Filtered dataframe to use. If None, uses full dataset.
        save_path : str, optional
            Path to save the plot. If None, displays the plot.
        """
        if filtered_df is None:
            filtered_df = self.df
        
        if product_id:
            filtered_df = filtered_df[filtered_df['product_id'] == product_id]
            if len(filtered_df) == 0:
                print(f"No data found for product_id: {product_id}")
                return
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Prepare data for boxplot
        product_names = []
        prices_list = []
        
        for pid in filtered_df['product_id'].unique():
            product_data = filtered_df[filtered_df['product_id'] == pid]
            product_names.append(f"{product_data['product_name'].iloc[0]}\n(ID: {pid})")
            prices_list.append(product_data['price'].values)
        
        # Create boxplot
        bp = ax.boxplot(prices_list, labels=product_names, patch_artist=True)
        
        # Customize boxplot colors
        colors = sns.color_palette("husl", len(prices_list))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Customize the plot
        ax.set_xlabel('Product', fontsize=12, fontweight='bold')
        ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
        ax.set_title('Price Distribution Across Products', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
        
        plt.close()


def main():
    """
    Main execution function demonstrating the Price Comparison System.
    """
    # Example usage
    print("Product Price Comparison System")
    print("="*80)
    
    # Try to load from CSV, if not available, create sample data
    try:
        system = PriceComparisonSystem(data_path='product_prices.csv')
        print("Loaded data from product_prices.csv")
    except FileNotFoundError:
        print("CSV file not found. Creating sample data...")
        # Create sample data
        sample_data = create_sample_data()
        system = PriceComparisonSystem(df=sample_data)
        print("Sample data created successfully")
    
    # Get overall statistics
    stats = system.get_statistics()
    system.print_statistics(stats)
    
    # Compare prices for all products
    comparison_df = system.compare_prices()
    system.print_comparison_summary(comparison_df)
    
    # Example: Filter by product name
    print("\n\nFiltering by product name containing 'Laptop'...")
    filtered = system.filter_data(product_name='Laptop')
    if len(filtered) > 0:
        filtered_comparison = system.compare_prices(filtered)
        system.print_comparison_summary(filtered_comparison)
    
    # Visualize first product
    if len(comparison_df) > 0:
        first_product_id = comparison_df.iloc[0]['product_id']
        print(f"\n\nGenerating visualization for product: {comparison_df.iloc[0]['product_name']}")
        system.plot_product_comparison(first_product_id)
        
        # Generate boxplot
        print("\nGenerating price distribution boxplot...")
        system.plot_price_distribution()


def create_sample_data() -> pd.DataFrame:
    """
    Create sample product price data for testing.
    
    Returns:
    --------
    pd.DataFrame
        Sample dataframe with product price data
    """
    np.random.seed(42)  # For reproducibility
    
    products = [
        {'product_id': 'P001', 'product_name': 'Laptop Pro 15'},
        {'product_id': 'P002', 'product_name': 'Wireless Mouse'},
        {'product_id': 'P003', 'product_name': 'Mechanical Keyboard'},
        {'product_id': 'P004', 'product_name': 'USB-C Hub'},
        {'product_id': 'P005', 'product_name': 'Laptop Stand'},
    ]
    
    shops = ['TechMart', 'ElectroWorld', 'BestBuy Electronics', 'GadgetHub', 'DigitalStore']
    
    data = []
    for product in products:
        # Each product available in 3-5 random shops with varying prices
        num_shops = np.random.randint(3, 6)
        selected_shops = np.random.choice(shops, size=num_shops, replace=False)
        
        # Base price for each product
        base_prices = {
            'P001': 1200,  # Laptop
            'P002': 25,    # Mouse
            'P003': 80,    # Keyboard
            'P004': 35,    # USB-C Hub
            'P005': 45,    # Stand
        }
        
        base_price = base_prices[product['product_id']]
        
        for shop in selected_shops:
            # Add price variation (±20%)
            price_variation = np.random.uniform(-0.2, 0.2)
            price = base_price * (1 + price_variation)
            price = round(price, 2)
            
            data.append({
                'product_id': product['product_id'],
                'product_name': product['product_name'],
                'shop_name': shop,
                'price': price
            })
    
    return pd.DataFrame(data)


if __name__ == "__main__":
    main()


