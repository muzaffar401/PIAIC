# BMI Calculator with Visualization

A Streamlit web application that calculates Body Mass Index (BMI) and displays interactive visualizations to help users understand their weight status and trends.

## Features

- **BMI Calculation**: Computes BMI based on user-provided weight and height
- **Category Classification**: Identifies if the result is Underweight, Normal, Overweight, or Obese
- **Trend Visualization**: Shows how BMI changes across different heights for the given weight
- **Personalized Markers**: Highlights the user's specific position on the trend line
- **Health Recommendations**: Provides tailored advice based on BMI category

## Technical Components

- **Frontend**: Built with Streamlit for easy web deployment
- **Visualizations**: Created using Matplotlib for clear data representation
- **BMI Logic**: Implements standard WHO classification categories
- **Responsive Design**: Works on both desktop and mobile devices

## How to Use

1. Enter your weight in kilograms
2. Enter your height in centimeters
3. Click "Calculate BMI"
4. View your BMI result and category
5. Examine the trend visualization showing how BMI changes with height
6. Expand the health recommendations section for personalized advice

## Requirements

- Python 3.7+
- Streamlit
- Matplotlib
- NumPy

## Project Structure

```
bmi-calculator/
├── main.py                # Main application file
├── README.md             # This documentation file
├── requirements.txt      # Python dependencies
```

## Visualization Features

The application generates a line chart that:
- Plots BMI values across a range of heights (140-200cm)
- Marks WHO standard BMI category thresholds
- Highlights your specific BMI with a colored dot
- Shows your exact BMI value with an annotation

## Health Information

The app provides expandable health recommendations for each BMI category, including:
- Dietary suggestions
- Exercise advice
- When to consult healthcare professionals

# URL : https://bmi-calculator-app-streammlit.streamlit.app/

## Note

BMI is a screening tool but not a diagnostic measure of body fatness or health. Always consult with a healthcare provider for personalized health advice.
```


