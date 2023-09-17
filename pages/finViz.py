import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.header("FinViz : Numbers made easy")

# Upload Excel file
try:
    uploaded_file = st.file_uploader("Upload an Excel or csv file", type=["xlsx","csv"])
except Exception as e:
    st.error(f"An error occurred during file upload: {e}")
    uploaded_file = None

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"An error occurred while reading the Excel file: {e}")
        df = None

    # Show the DataFrame
    st.write("Data Preview:")
    st.write(df.head())

    # Show available columns and let user select two
    available_columns = df.columns.tolist()
    column1 = st.selectbox("Select the first variable", available_columns)
    column2 = st.selectbox("Select the second variable", available_columns)

    # Determine the data types
    is_numeric1 = pd.api.types.is_numeric_dtype(df[column1])
    is_numeric2 = pd.api.types.is_numeric_dtype(df[column2])

    # Allow user to select the type of plot
    if is_numeric1 and is_numeric2:
        chart_types = ['Scatter Plot', 'Line Chart', 'Histogram', 'Heatmap']
    elif is_numeric1 or is_numeric2:
        chart_types = ['Bar Chart', 'Box Plot', 'Violin Plot', 'Pie Chart']  # Added 'Pie Chart'
    else:
        chart_types = ['Pie Chart']

    chart_type = st.selectbox("Select the type of chart", chart_types)

    # Aggregation methods if a categorical variable is selected
    if not is_numeric1 or not is_numeric2:
        agg_method = st.selectbox("Select aggregation method", ['Mean', 'Sum', 'Count'])

    if st.button("Generate Plot"):
        try:
            fig, ax = plt.subplots()

            if chart_type == 'Scatter Plot':
                ax.scatter(df[column1], df[column2])
            elif chart_type == 'Line Chart':
                ax.plot(df[column1], df[column2])
            elif chart_type == 'Histogram':
                sns.histplot(df, x=column1, y=column2, ax=ax)
            elif chart_type == 'Heatmap':
                sns.heatmap(pd.crosstab(df[column1], df[column2]), annot=True, ax=ax)
            elif chart_type == 'Bar Chart':
                if agg_method == 'Mean':
                    sns.barplot(data=df, x=column1, y=column2, estimator=np.mean, ax=ax)
                elif agg_method == 'Sum':
                    sns.barplot(data=df, x=column1, y=column2, estimator=np.sum, ax=ax)
                else:  # Count
                    sns.countplot(data=df, x=column1, ax=ax)
            elif chart_type == 'Box Plot':
                sns.boxplot(data=df, x=column1, y=column2, ax=ax)
            elif chart_type == 'Violin Plot':
                sns.violinplot(data=df, x=column1, y=column2, ax=ax)
            elif chart_type == 'Pie Chart':
                if is_numeric2:  # Make sure the second variable is numeric
                    if agg_method == 'Mean':
                        pie_data = df.groupby(column1)[column2].mean()
                    elif agg_method == 'Sum':
                        pie_data = df.groupby(column1)[column2].sum()
                    else:  # Count
                        pie_data = df[column1].value_counts()
                    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')

            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.title(f'{column1} vs {column2}')
            st.pyplot(fig)
        except Exception as e:
            st.error(f"An error occurred while generating the plot: {e}")
