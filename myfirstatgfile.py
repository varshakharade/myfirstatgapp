import streamlit
streamlit.title('Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Boiled Eggs')
streamlit.text('Bread & Peanutbutter')
streamlit.text('🥑🍞Milk')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
streamlit.dataframe(my_fruit_list)

