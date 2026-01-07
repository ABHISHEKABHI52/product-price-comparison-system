"""
Example usage of the Price Comparison System.

This script demonstrates various features and use cases.
"""

from price_comparison_system import PriceComparisonSystem, create_sample_data
import pandas as pd

def example_basic_usage():
    """Basic usage example."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Usage")
    print("="*80)
    
    # Create sample data if CSV doesn't exist
    try:
        system = PriceComparisonSystem(data_path='product_prices.csv')
        print("✓ Loaded data from product_prices.csv")
    except FileNotFoundError:
        print("⚠ CSV not found. Creating sample data...")
        sample_data = create_sample_data()
        system = PriceComparisonSystem(df=sample_data)
        print("✓ Sample data created and loaded")
    
    # Get statistics
    stats = system.get_statistics()
    system.print_statistics(stats)
    
    # Compare all products
    comparison_df = system.compare_prices()
    system.print_comparison_summary(comparison_df)


def example_filtering():
    """Filtering examples."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Filtering")
    print("="*80)
    
    try:
        system = PriceComparisonSystem(data_path='product_prices.csv')
    except FileNotFoundError:
        sample_data = create_sample_data()
        system = PriceComparisonSystem(df=sample_data)
    
    # Filter by product name
    print("\n--- Filtering by product name containing 'Laptop' ---")
    filtered = system.filter_data(product_name='Laptop')
    print(f"Found {len(filtered)} records")
    if len(filtered) > 0:
        comparison = system.compare_prices(filtered)
        system.print_comparison_summary(comparison)
    
    # Filter by price range
    print("\n--- Filtering by price range ($30 - $100) ---")
    filtered = system.filter_data(price_min=30, price_max=100)
    print(f"Found {len(filtered)} records")
    if len(filtered) > 0:
        comparison = system.compare_prices(filtered)
        system.print_comparison_summary(comparison)


def example_visualization():
    """Visualization examples."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Visualization")
    print("="*80)
    
    try:
        system = PriceComparisonSystem(data_path='product_prices.csv')
    except FileNotFoundError:
        sample_data = create_sample_data()
        system = PriceComparisonSystem(df=sample_data)
    
    # Get first product for visualization
    comparison_df = system.compare_prices()
    if len(comparison_df) > 0:
        first_product_id = comparison_df.iloc[0]['product_id']
        first_product_name = comparison_df.iloc[0]['product_name']
        
        print(f"\nGenerating bar chart for: {first_product_name}")
        system.plot_product_comparison(first_product_id, save_path='product_comparison.png')
        
        print("\nGenerating price distribution boxplot...")
        system.plot_price_distribution(save_path='price_distribution.png')


def example_custom_data():
    """Example with custom data."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Custom Data")
    print("="*80)
    
    # Create custom DataFrame
    custom_data = pd.DataFrame({
        'product_id': ['P101', 'P101', 'P101', 'P102', 'P102', 'P102'],
        'product_name': ['Smartphone X', 'Smartphone X', 'Smartphone X', 
                        'Tablet Y', 'Tablet Y', 'Tablet Y'],
        'shop_name': ['Store A', 'Store B', 'Store C', 
                     'Store A', 'Store B', 'Store C'],
        'price': [599.99, 649.99, 579.99, 299.99, 319.99, 289.99]
    })
    
    system = PriceComparisonSystem(df=custom_data)
    print("✓ Custom data loaded")
    
    comparison_df = system.compare_prices()
    system.print_comparison_summary(comparison_df)
    
    # Visualize first product
    if len(comparison_df) > 0:
        system.plot_product_comparison(comparison_df.iloc[0]['product_id'])


if __name__ == "__main__":
    print("\n" + "="*80)
    print("PRODUCT PRICE COMPARISON SYSTEM - EXAMPLES")
    print("="*80)
    
    # Run examples
    example_basic_usage()
    example_filtering()
    example_visualization()
    example_custom_data()
    
    print("\n" + "="*80)
    print("All examples completed!")
    print("="*80)


