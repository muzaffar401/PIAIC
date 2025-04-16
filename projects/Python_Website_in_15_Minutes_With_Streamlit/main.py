import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression  # More robust linear regression

# App title and description
st.title("📊 Data Visualization Dashboard")
st.markdown("Upload your CSV file to explore and visualize your data")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        # Show basic info
        st.subheader("📋 Data Information")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows", df.shape[0])
        with col2:
            st.metric("Total Columns", df.shape[1])

        # Data preview
        with st.expander("🔍 View Data Preview"):
            st.dataframe(df.head())

        # Data summary
        with st.expander("📊 View Data Statistics"):
            st.dataframe(df.describe(include='all'))

        # Filter section
        st.subheader("🔎 Filter Data")
        columns = df.columns.tolist()

        col1, col2 = st.columns(2)
        with col1:
            selected_column = st.selectbox("Select column to filter by", columns)
        with col2:
            unique_values = df[selected_column].unique()
            selected_value = st.selectbox(f"Select {selected_column}", unique_values)

        filtered_df = df[df[selected_column] == selected_value]

        with st.expander("🔍 View Filtered Data"):
            st.dataframe(filtered_df)

        # Visualization section
        st.subheader("📈 Visualize Data")

        if not filtered_df.empty:
            available_columns = filtered_df.columns.tolist()
            
            # Ensure we have at least 2 columns for visualization
            if len(available_columns) < 2:
                st.warning("Need at least 2 columns to create a visualization")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    x_column = st.selectbox("X-axis column", available_columns)
                with col2:
                    # Exclude x_column from y-axis options
                    y_options = [col for col in available_columns if col != x_column]
                    y_column = st.selectbox("Y-axis column", y_options)

                chart_type = st.radio("Select chart type",
                                    ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"])
                
                # Additional options for scatter plot
                if chart_type == "Scatter Plot":
                    point_size = st.slider("Point size", 1, 100, 20)
                    show_trendline = st.checkbox("Show trendline", True)

                if st.button("Generate Visualization"):
                    try:
                        # Convert x values to numeric indices if not numeric
                        if not pd.api.types.is_numeric_dtype(filtered_df[x_column]):
                            x_values = pd.factorize(filtered_df[x_column])[0]
                        else:
                            x_values = filtered_df[x_column].values
                        
                        y_values = filtered_df[y_column].values
                        
                        if chart_type == "Line Chart":
                            st.line_chart(filtered_df.set_index(x_column)[y_column])
                        elif chart_type == "Bar Chart":
                            st.bar_chart(filtered_df.set_index(x_column)[y_column])
                        elif chart_type == "Area Chart":
                            st.area_chart(filtered_df.set_index(x_column)[y_column])
                        elif chart_type == "Scatter Plot":
                            fig, ax = plt.subplots()
                            ax.scatter(filtered_df[x_column], filtered_df[y_column], s=point_size)
                            
                            if show_trendline and len(filtered_df) > 1:
                                try:
                                    # More robust linear regression using scikit-learn
                                    X = x_values.reshape(-1, 1)
                                    model = LinearRegression().fit(X, y_values)
                                    ax.plot(filtered_df[x_column], 
                                           model.predict(X), 
                                           "r--", 
                                           label='Trendline')
                                    ax.legend()
                                except Exception as e:
                                    st.warning(f"Could not calculate trendline: {str(e)}")
                            
                            ax.set_xlabel(x_column)
                            ax.set_ylabel(y_column)
                            plt.xticks(rotation=45)
                            st.pyplot(fig)
                    except Exception as e:
                        st.error(f"Error generating chart: {str(e)}")
                        st.error("Please check your column selections and data types")
        else:
            st.warning("No data available after filtering. Adjust your filters.")

        # Raw data download
        st.subheader("💾 Export Data")
        st.download_button(
            label="Download Filtered Data as CSV",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name='filtered_data.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please check your file format and try again.")
else:
    st.info("👆 Please upload a CSV file to get started")
    st.markdown("""
    ### Sample CSV Format:
    ```csv
    Date,Value,Category
    2023-01-01,100,A
    2023-01-02,150,B
    2023-01-03,200,A
    ```
    """)