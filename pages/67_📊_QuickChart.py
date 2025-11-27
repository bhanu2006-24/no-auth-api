import streamlit as st
import requests
from io import BytesIO

st.set_page_config(page_title="QuickChart", page_icon="📊")

st.title("📊 QuickChart Generator")
st.markdown("Generate charts on the fly using [QuickChart](https://quickchart.io/).")

chart_type = st.selectbox("Chart Type", ["bar", "line", "pie", "doughnut", "radar"])
labels = st.text_input("Labels (comma separated)", "January, February, March, April, May")
data_points = st.text_input("Data (comma separated)", "50, 60, 70, 180, 190")
label_name = st.text_input("Dataset Label", "Sales")

if st.button("Generate Chart"):
    try:
        labels_list = [l.strip() for l in labels.split(",")]
        data_list = [int(d.strip()) for d in data_points.split(",")]
        
        # Construct the chart config
        chart_config = {
            "type": chart_type,
            "data": {
                "labels": labels_list,
                "datasets": [{
                    "label": label_name,
                    "data": data_list
                }]
            }
        }
        
        # QuickChart URL
        # We can send the config as JSON in the URL or POST request.
        # For simple usage, we can use the python-quickchart wrapper logic or just construct the URL.
        # But requests post is cleaner for larger configs.
        
        response = requests.post('https://quickchart.io/chart/create', json={
            'chart': chart_config,
            'width': 500,
            'height': 300,
            'backgroundColor': 'white'
        })
        
        if response.status_code == 200:
            chart_data = response.json()
            if chart_data['success']:
                st.image(chart_data['url'], caption="Generated Chart", use_column_width=True)
            else:
                st.error("API returned error.")
        else:
            st.error("Failed to generate chart.")
            
    except ValueError:
        st.error("Please ensure data points are numbers.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
