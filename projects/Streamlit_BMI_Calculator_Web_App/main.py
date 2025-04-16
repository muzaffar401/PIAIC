import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# BMI calculation functions
def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db"  # Blue
    elif 18.5 <= bmi < 25:
        return "Normal weight", "#2ecc71"  # Green
    elif 25 <= bmi < 30:
        return "Overweight", "#f39c12"  # Orange
    else:
        return "Obese", "#e74c3c"  # Red

# Page setup
st.set_page_config(page_title="BMI Calculator with Trends", layout="centered")
st.title("BMI Calculator with Height Trend")

# Inputs
with st.form("bmi_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
    
    with col2:
        height = st.number_input("Height (cm)", min_value=120.0, max_value=250.0, value=170.0, step=0.1)
    
    submitted = st.form_submit_button("Calculate BMI")

# Calculations and results
if submitted:
    bmi = calculate_bmi(weight, height)
    category, color = get_bmi_category(bmi)
    
    # Display BMI result
    st.markdown(f"""
    <div style='border-radius: 10px; padding: 15px; background-color: #f8f9fa; 
                border-left: 5px solid {color}; margin-bottom: 20px;'>
        <h3 style='margin-top: 0;'>Your BMI: <span style='color: {color};'>{bmi:.1f}</span></h3>
        <p style='margin-bottom: 0;'>Category: {category}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create line chart showing BMI across different heights
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Generate height range (140cm to 200cm)
    heights = np.linspace(140, 200, 100)
    bmis = [calculate_bmi(weight, h) for h in heights]
    
    # Plot the line
    ax.plot(heights, bmis, color='#3498db', linewidth=2.5, label='BMI Trend')
    
    # Add horizontal lines for BMI categories
    ax.axhline(y=18.5, color='#2ecc71', linestyle='--', alpha=0.5, label='Underweight/Normal')
    ax.axhline(y=25, color='#f39c12', linestyle='--', alpha=0.5, label='Normal/Overweight')
    ax.axhline(y=30, color='#e74c3c', linestyle='--', alpha=0.5, label='Overweight/Obese')
    
    # Highlight current position
    ax.scatter(height, bmi, color=color, s=100, zorder=5, label='Your Position')
    ax.annotate(f'Your BMI: {bmi:.1f}', 
                (height, bmi),
                textcoords="offset points",
                xytext=(10,10),
                ha='left')
    
    # Style the chart
    ax.set_title(f'BMI Trend for {weight}kg Across Different Heights')
    ax.set_xlabel('Height (cm)')
    ax.set_ylabel('BMI')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    
    # Display the chart
    st.pyplot(fig)
    
    # Health information
    with st.expander("Health Information"):
        if bmi < 18.5:
            st.write("""
            **Underweight Recommendations:**
            - Eat more nutrient-dense foods
            - Include strength training in your exercise routine
            - Consult a doctor if unintentional weight loss occurs
            """)
        elif bmi < 25:
            st.write("""
            **Healthy Weight Recommendations:**
            - Maintain balanced diet
            - Get regular physical activity
            - Monitor your weight periodically
            """)
        elif bmi < 30:
            st.write("""
            **Overweight Recommendations:**
            - Focus on portion control
            - Increase physical activity
            - Reduce processed foods and sugary drinks
            """)
        else:
            st.write("""
            **Obese Recommendations:**
            - Consult with a healthcare provider
            - Consider professional nutrition guidance
            - Start with low-impact exercises
            """)

# Footer
st.markdown("---")
st.caption("Note: BMI is a screening tool but not a diagnostic of body fatness or health.")