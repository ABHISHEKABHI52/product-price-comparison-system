"""
Product Price Comparison System - Web Application

A Streamlit web application for comparing product prices across multiple shops.
"""

import streamlit as st
import pandas as pd
from price_comparison_system import PriceComparisonSystem, create_sample_data
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Product Price Comparison System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful and attractive styling
st.markdown("""
    <style>
    /* Main header with gradient */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Gradient background for the page */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: white !important;
    }
    
    /* Metric cards with colorful backgrounds */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        color: white;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Colorful info boxes */
    .stInfo {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-left: 5px solid #667eea;
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Success messages */
    .stSuccess {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        border-radius: 10px;
    }
    
    /* Warning messages */
    .stWarning {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-radius: 10px;
    }
    
    /* Buttons with gradient */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Selectbox and input styling */
    .stSelectbox label, .stSlider label {
        color: #667eea;
        font-weight: bold;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    h2, h3 {
        color: #667eea !important;
        font-weight: 700 !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    /* Welcome card */
    .welcome-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        margin: 2rem 0;
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateX(10px);
    }
    
    /* Animated gradient text */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .gradient-text {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'system' not in st.session_state:
    st.session_state.system = None
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'comparison_df' not in st.session_state:
    st.session_state.comparison_df = None


def load_data_from_csv(uploaded_file):
    """Load data from uploaded CSV file."""
    try:
        df = pd.read_csv(uploaded_file)
        return PriceComparisonSystem(df=df)
    except Exception as e:
        st.error(f"Error loading CSV file: {str(e)}")
        return None


def load_sample_data():
    """Load sample data."""
    try:
        sample_data = create_sample_data()
        return PriceComparisonSystem(df=sample_data)
    except Exception as e:
        st.error(f"Error creating sample data: {str(e)}")
        return None


def main():
    """Main application function."""
    
    # Header with gradient
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 class="main-header gradient-text">💰 Product Price Comparison System</h1>
        <p style="font-size: 1.2rem; color: #667eea; font-weight: 600;">Compare prices across shops and find the best deals!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Sidebar for data loading and filters
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: white; font-size: 2rem; margin: 0;">💰</h1>
            <h2 style="color: white; font-size: 1.5rem; margin: 0.5rem 0;">Price Comparison</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <h3 style="color: white; margin: 0;">📊 Data Management</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Data loading options
        st.markdown('<p style="color: white; font-weight: 600;">📁 Load Data</p>', unsafe_allow_html=True)
        data_option = st.radio(
            "Choose data source:",
            ["Upload CSV", "Use Sample Data"],
            key="data_source"
        )
        
        if data_option == "Upload CSV":
            uploaded_file = st.file_uploader(
                "Upload CSV file",
                type=['csv'],
                help="CSV should have columns: product_id, product_name, shop_name, price"
            )
            
            if uploaded_file is not None:
                if st.button("Load CSV Data", type="primary"):
                    with st.spinner("Loading and cleaning data..."):
                        system = load_data_from_csv(uploaded_file)
                        if system is not None:
                            st.session_state.system = system
                            st.session_state.data_loaded = True
                            st.session_state.comparison_df = system.compare_prices()
                            st.success("Data loaded successfully!")
                            st.rerun()
        
        else:  # Use Sample Data
            if st.button("Load Sample Data", type="primary"):
                with st.spinner("Generating sample data..."):
                    system = load_sample_data()
                    if system is not None:
                        st.session_state.system = system
                        st.session_state.data_loaded = True
                        st.session_state.comparison_df = system.compare_prices()
                        st.success("Sample data loaded successfully!")
                        st.rerun()
        
        # Filters section
        if st.session_state.data_loaded:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                <h3 style="color: white; margin: 0;">🔍 Filters</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Get unique values for filters
            unique_products = ['All'] + sorted(st.session_state.system.df['product_name'].unique().tolist())
            unique_shops = ['All'] + sorted(st.session_state.system.df['shop_name'].unique().tolist())
            
            # Product filter
            selected_product = st.selectbox(
                "Filter by Product:",
                unique_products,
                key="filter_product"
            )
            
            # Shop filter
            selected_shop = st.selectbox(
                "Filter by Shop:",
                unique_shops,
                key="filter_shop"
            )
            
            # Price range filter
            price_min = st.session_state.system.df['price'].min()
            price_max = st.session_state.system.df['price'].max()
            
            st.subheader("Price Range")
            price_range = st.slider(
                "Select price range:",
                min_value=float(price_min),
                max_value=float(price_max),
                value=(float(price_min), float(price_max)),
                key="price_range"
            )
            
            # Apply filters button
            if st.button("Apply Filters", type="primary"):
                st.rerun()
    
    # Main content area
    if not st.session_state.data_loaded:
        # Welcome screen with colorful cards
        st.markdown("""
        <div class="welcome-card">
            <h2 style="color: white; text-align: center; margin-bottom: 1rem;">👋 Welcome to Price Comparison System!</h2>
            <p style="color: white; text-align: center; font-size: 1.1rem;">👈 Please load data from the sidebar to get started!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature cards in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <h3 style="color: #667eea;">📋 How to Use</h3>
                <ul style="line-height: 2;">
                    <li><strong>Upload CSV:</strong> Upload your own CSV file with product price data</li>
                    <li><strong>Use Sample Data:</strong> Load pre-generated sample data for testing</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
                <h3 style="color: #667eea;">✨ Features</h3>
                <ul style="line-height: 2;">
                    <li>🔍 Filter by product, shop, and price range</li>
                    <li>📈 Compare prices across shops</li>
                    <li>📊 View detailed statistics</li>
                    <li>📉 Interactive visualizations</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <h3 style="color: #667eea;">📊 Required CSV Format</h3>
                <p>Your CSV file should contain these columns:</p>
                <ul style="line-height: 2;">
                    <li><code>product_id</code>: Unique identifier</li>
                    <li><code>product_name</code>: Name of the product</li>
                    <li><code>shop_name</code>: Name of the shop/store</li>
                    <li><code>price</code>: Price (numeric)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Show sample data structure with colorful styling
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📝 View Sample Data Structure", expanded=False):
            sample_df = pd.DataFrame({
                'product_id': ['P001', 'P001', 'P002'],
                'product_name': ['Laptop Pro 15', 'Laptop Pro 15', 'Wireless Mouse'],
                'shop_name': ['TechMart', 'ElectroWorld', 'TechMart'],
                'price': [1199.99, 1249.50, 24.99]
            })
            st.dataframe(sample_df, use_container_width=True, height=150)
    
    else:
        # Apply filters - combine all filters at once
        filter_params = {}
        
        if selected_product != 'All':
            filter_params['product_name'] = selected_product
        
        if selected_shop != 'All':
            filter_params['shop_name'] = selected_shop
        
        filter_params['price_min'] = price_range[0]
        filter_params['price_max'] = price_range[1]
        
        # Apply all filters
        filtered_df = st.session_state.system.filter_data(**filter_params)
        
        # Update comparison with filtered data
        if len(filtered_df) > 0:
            comparison_df = st.session_state.system.compare_prices(filtered_df)
        else:
            comparison_df = pd.DataFrame()
            st.warning("No data matches the selected filters. Please adjust your filters.")
        
        # Statistics Section with colorful styling
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
            <h2 style="color: white; text-align: center; margin: 0;">📊 Overall Statistics</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if len(filtered_df) > 0:
            stats = st.session_state.system.get_statistics(filtered_df)
            
            # Display metrics in columns with colorful backgrounds
            col1, col2, col3, col4 = st.columns(4)
            
            metric_colors = [
                "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
                "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
                "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
            ]
            
            metrics_data = [
                ("Mean Price", f"${stats['mean']:.2f}", "Average price across all products", metric_colors[0]),
                ("Min Price", f"${stats['min']:.2f}", "Lowest price in dataset", metric_colors[1]),
                ("Max Price", f"${stats['max']:.2f}", "Highest price in dataset", metric_colors[2]),
                ("Std Deviation", f"${stats['std']:.2f}", "Price variability measure", metric_colors[3])
            ]
            
            for i, (col, (label, value, caption, color)) in enumerate(zip([col1, col2, col3, col4], metrics_data)):
                with col:
                    st.markdown(f"""
                    <div style="background: {color}; padding: 1.5rem; border-radius: 15px; text-align: center; 
                                box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-bottom: 1rem;">
                        <h3 style="color: white; margin: 0; font-size: 0.9rem; font-weight: 600;">{label}</h3>
                        <h2 style="color: white; margin: 0.5rem 0; font-size: 2rem; font-weight: 900;">{value}</h2>
                        <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.8rem;">{caption}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Additional metrics
            col5, col6, col7 = st.columns(3)
            
            additional_colors = [
                "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
                "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
                "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"
            ]
            
            additional_metrics = [
                ("Total Products", stats['total_products'], additional_colors[0]),
                ("Total Shops", stats['total_shops'], additional_colors[1]),
                ("Total Records", stats['total_records'], additional_colors[2])
            ]
            
            for col, (label, value, color) in zip([col5, col6, col7], additional_metrics):
                with col:
                    st.markdown(f"""
                    <div style="background: {color}; padding: 1.5rem; border-radius: 15px; text-align: center; 
                                box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-top: 1rem;">
                        <h3 style="color: white; margin: 0; font-size: 0.9rem; font-weight: 600;">{label}</h3>
                        <h2 style="color: white; margin: 0.5rem 0; font-size: 2.5rem; font-weight: 900;">{value}</h2>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Price Comparison Section
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
            <h2 style="color: white; text-align: center; margin: 0;">🔍 Price Comparison by Product</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if len(comparison_df) > 0:
            # Display comparison table
            display_df = comparison_df[[
                'product_name', 'cheapest_shop', 'cheapest_price',
                'most_expensive_shop', 'most_expensive_price',
                'price_difference', 'avg_price', 'shop_count'
            ]].copy()
            
            # Format prices for display
            display_df['cheapest_price'] = display_df['cheapest_price'].apply(lambda x: f"${x:.2f}")
            display_df['most_expensive_price'] = display_df['most_expensive_price'].apply(lambda x: f"${x:.2f}")
            display_df['price_difference'] = display_df['price_difference'].apply(lambda x: f"${x:.2f}")
            display_df['avg_price'] = display_df['avg_price'].apply(lambda x: f"${x:.2f}")
            
            # Rename columns for better display
            display_df.columns = [
                'Product Name', 'Cheapest Shop', 'Cheapest Price',
                'Most Expensive Shop', 'Most Expensive Price',
                'Price Difference', 'Average Price', 'Available Shops'
            ]
            
            # Styled dataframe with colorful background
            st.markdown("""
            <style>
            .stDataFrame {
                border-radius: 15px;
                overflow: hidden;
            }
            </style>
            """, unsafe_allow_html=True)
            st.dataframe(
                display_df, 
                use_container_width=True, 
                hide_index=True,
                height=400
            )
            
            # Detailed view for each product
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 1rem; border-radius: 15px; margin: 2rem 0;">
                <h3 style="color: white; text-align: center; margin: 0;">📈 Product Details</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Product selector
            product_options = comparison_df['product_name'].unique()
            selected_product_detail = st.selectbox(
                "🎯 Select a product to view details:",
                product_options,
                key="product_detail"
            )
            
            if selected_product_detail:
                product_row = comparison_df[comparison_df['product_name'] == selected_product_detail].iloc[0]
                product_id = product_row['product_id']
                
                # Display product statistics with colorful cards
                col1, col2, col3, col4 = st.columns(4)
                
                product_metric_colors = [
                    "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",  # Green for cheapest
                    "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",  # Red for expensive
                    "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",  # Yellow for difference
                    "linear-gradient(135deg, #30cfd0 0%, #330867 100%)"   # Blue for average
                ]
                
                product_metrics = [
                    ("Cheapest", f"${product_row['cheapest_price']:.2f}", f"at {product_row['cheapest_shop']}", product_metric_colors[0]),
                    ("Most Expensive", f"${product_row['most_expensive_price']:.2f}", f"at {product_row['most_expensive_shop']}", product_metric_colors[1]),
                    ("Price Difference", f"${product_row['price_difference']:.2f}", "Max - Min", product_metric_colors[2]),
                    ("Average Price", f"${product_row['avg_price']:.2f}", "Mean price", product_metric_colors[3])
                ]
                
                for col, (label, value, subtitle, color) in zip([col1, col2, col3, col4], product_metrics):
                    with col:
                        st.markdown(f"""
                        <div style="background: {color}; padding: 1.2rem; border-radius: 15px; text-align: center; 
                                    box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-bottom: 1rem;">
                            <h4 style="color: white; margin: 0; font-size: 0.85rem; font-weight: 600;">{label}</h4>
                            <h2 style="color: white; margin: 0.5rem 0; font-size: 1.8rem; font-weight: 900;">{value}</h2>
                            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.75rem;">{subtitle}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Visualization
                st.markdown("""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 15px; margin: 2rem 0;">
                    <h3 style="color: white; text-align: center; margin: 0;">📊 Price Comparison Chart</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Create visualization for Streamlit
                product_data = filtered_df[filtered_df['product_id'] == product_id].sort_values('price')
                
                fig, ax = plt.subplots(figsize=(12, 6))
                
                # Get colors for bars - more vibrant colors
                colors = []
                min_price = product_data['price'].min()
                max_price = product_data['price'].max()
                
                # Colorful gradient palette
                for price in product_data['price']:
                    if price == min_price:
                        colors.append('#43e97b')  # Bright green
                    elif price == max_price:
                        colors.append('#f5576c')  # Bright red
                    else:
                        # Use gradient colors for other bars
                        price_ratio = (price - min_price) / (max_price - min_price) if max_price != min_price else 0.5
                        if price_ratio < 0.33:
                            colors.append('#4facfe')  # Blue
                        elif price_ratio < 0.66:
                            colors.append('#667eea')  # Purple
                        else:
                            colors.append('#f093fb')  # Pink
                
                bars = ax.bar(range(len(product_data)), product_data['price'], color=colors, alpha=0.7)
                
                ax.set_xlabel('Shop', fontsize=12, fontweight='bold')
                ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
                ax.set_title(f'Price Comparison: {selected_product_detail}', 
                            fontsize=14, fontweight='bold')
                ax.set_xticks(range(len(product_data)))
                ax.set_xticklabels(product_data['shop_name'], rotation=45, ha='right')
                
                # Add value labels
                for bar, price in zip(bars, product_data['price']):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'${price:.2f}',
                           ha='center', va='bottom', fontweight='bold')
                
                # Add legend with vibrant colors
                from matplotlib.patches import Patch
                legend_elements = [
                    Patch(facecolor='#43e97b', alpha=0.8, label='Cheapest'),
                    Patch(facecolor='#f5576c', alpha=0.8, label='Most Expensive'),
                    Patch(facecolor='#667eea', alpha=0.8, label='Other Shops')
                ]
                ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9, fontsize=10)
                ax.grid(axis='y', alpha=0.3, linestyle='--', color='#667eea')
                ax.set_facecolor('#f8f9fa')
                
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()
                
                # Boxplot for price distribution
                if len(comparison_df) > 1:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 1rem; border-radius: 15px; margin: 2rem 0;">
                        <h3 style="color: #667eea; text-align: center; margin: 0;">📦 Price Distribution Across Products</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    fig2, ax2 = plt.subplots(figsize=(14, 6))
                    
                    product_names = []
                    prices_list = []
                    
                    for pid in comparison_df['product_id'].unique():
                        product_data = filtered_df[filtered_df['product_id'] == pid]
                        product_names.append(f"{product_data['product_name'].iloc[0]}\n(ID: {pid})")
                        prices_list.append(product_data['price'].values)
                    
                    bp = ax2.boxplot(prices_list, labels=product_names, patch_artist=True)
                    
                    # Use vibrant color palette
                    vibrant_colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', 
                                     '#43e97b', '#fa709a', '#fee140', '#30cfd0', '#a8edea']
                    colors = [vibrant_colors[i % len(vibrant_colors)] for i in range(len(prices_list))]
                    for patch, color in zip(bp['boxes'], colors):
                        patch.set_facecolor(color)
                        patch.set_alpha(0.8)
                    
                    ax2.set_facecolor('#f8f9fa')
                    
                    ax2.set_xlabel('Product', fontsize=12, fontweight='bold')
                    ax2.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
                    ax2.set_title('Price Distribution Across Products', fontsize=14, fontweight='bold')
                    ax2.grid(axis='y', alpha=0.3, linestyle='--')
                    
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    st.pyplot(fig2)
                    plt.close()
        
        else:
            st.info("No comparison data available. Please check your filters or load data.")
        
        # Raw Data View
        with st.expander("📋 View Raw Data"):
            st.dataframe(filtered_df, use_container_width=True)
            
            # Download button
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Filtered Data as CSV",
                data=csv,
                file_name="filtered_product_prices.csv",
                mime="text/csv"
            )


if __name__ == "__main__":
    main()

