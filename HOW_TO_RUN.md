# 🚀 How to Run the Web Application

## Step-by-Step Instructions

### Step 1: Install Dependencies

Open your terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- pandas
- numpy
- matplotlib
- seaborn
- streamlit

**Note:** If you get permission errors, try:
```bash
pip install --user -r requirements.txt
```

### Step 2: Run the Application

#### Option A: Using Command Line (Recommended)

```bash
streamlit run app.py
```

#### Option B: Using the Batch File (Windows)

Simply double-click `run_app.bat` in Windows Explorer

#### Option C: Using Python Directly

```bash
python -m streamlit run app.py
```

### Step 3: Access the Web App

After running the command, you should see:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

The app will **automatically open** in your default web browser. If it doesn't, manually navigate to:
```
http://localhost:8501
```

## 🎯 Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Run `streamlit run app.py`
- [ ] Browser opens automatically at http://localhost:8501

## 🔧 Troubleshooting

### "streamlit: command not found"
**Solution:** Install streamlit:
```bash
pip install streamlit
```

### "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Make sure you're in the correct Python environment:
```bash
python -m pip install streamlit
python -m streamlit run app.py
```

### Port 8501 already in use
**Solution:** Use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Browser doesn't open automatically
**Solution:** Manually open your browser and go to `http://localhost:8501`

## 📱 Using the App

1. **Load Data:**
   - Click the sidebar (arrow on the left)
   - Choose "Upload CSV" or "Use Sample Data"
   - Click the load button

2. **Apply Filters (Optional):**
   - Select product, shop, or adjust price range
   - Click "Apply Filters"

3. **View Results:**
   - See statistics in the main area
   - Check price comparison table
   - Select a product for detailed visualizations

## 🛑 Stopping the App

Press `Ctrl + C` in the terminal/command prompt to stop the server.

## 💡 Tips

- The app runs in your browser - keep the terminal window open
- Changes to `app.py` require restarting the app
- Sample data is generated automatically if no CSV is uploaded
- All filters work in real-time

Enjoy using the Product Price Comparison System! 💰

