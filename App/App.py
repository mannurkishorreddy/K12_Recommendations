import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .stApp {
        background-color: grey;
    }
    </style>
""", unsafe_allow_html=True)
# Define data
data = pd.read_csv('/Users/naman/Desktop/Kaggle/learning-equality-curriculum-recommendations/final_pred1.csv')
# Define sidebar
st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #FFFFE0;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title('Content Search')
selected_topic = st.sidebar.selectbox('Select a topic', data['topic_title'].unique())
st.sidebar.write("<p style='font-size:20px'>Description:</p>", unsafe_allow_html=True)
description = st.sidebar.write(data[data['topic_title'] == selected_topic]['topic_description'].iloc[0])

# Define search button
search_button = st.sidebar.button('Search')

	# Define main area
st.title('Search Results')
if search_button:
	filtered_data = data[data['topic_title'] == selected_topic]
	for i in range(len(filtered_data)):
		with st.expander(filtered_data.iloc[i,6]):
			st.write("Content Description:-",filtered_data.iloc[i,7])
			st.write("Type of content:-",filtered_data.iloc[i,12])
			with st.expander("See Full Text"):
				st.write("Content Description:-",filtered_data.iloc[i,8])

