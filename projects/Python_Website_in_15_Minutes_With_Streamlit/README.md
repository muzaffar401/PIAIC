# 📊 Data Visualization Dashboard

## Overview
A Streamlit-based web application for exploring and visualizing CSV data files. This interactive dashboard allows users to upload their datasets, apply filters, and generate various visualizations with just a few clicks.

## Features

### 🔍 Data Exploration
- View basic dataset information (row/column counts)
- Preview the first few rows of your data
- See comprehensive statistics for all columns

### 🔎 Data Filtering
- Filter data by any column
- Select specific values to focus your analysis
- View filtered results in an expandable table

### 📈 Visualization Tools
- **Multiple chart types**:
  - Line charts
  - Bar charts
  - Area charts
  - Scatter plots with customizable options
- **Trendline analysis** for scatter plots
- Interactive controls for axis selection
- Automatic handling of categorical/numeric data

### 💾 Data Export
- Download filtered datasets as CSV files
- Preserve your filtered views for further analysis

## Requirements
- Python 3.7+
- Required packages:
  ```
  pip install streamlit pandas matplotlib numpy scikit-learn
  ```

## How to Use
1. Upload your CSV file using the file uploader
2. Explore your data using the preview and statistics sections
3. Apply filters to focus on specific data subsets
4. Select visualization options (chart type, axes)
5. Generate and view your visualizations
6. Export filtered data if needed

## Supported Data Formats
- Standard CSV files with header row
- Both numeric and categorical data
- Date/time data (will be automatically parsed)

## Troubleshooting
- If visualizations fail to generate:
  - Check that your selected columns contain appropriate data types
  - Ensure numeric columns don't contain non-numeric values
  - Try with smaller data subsets if experiencing performance issues

## Sample Data Structure
For best results, your CSV should follow this format:
```csv
Date,Value,Category
2023-01-01,100,A
2023-01-02,150,B
2023-01-03,200,A
```

## Customization
The application can be easily modified to:
- Add additional chart types
- Include more advanced statistical analysis
- Support different file formats
- Change visual styling

## License
This project is open-source and available for free use and modification.