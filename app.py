import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title= 'Excel Plotter')
st.title('Excel Plotter :satisfied:')
st.subheader('Feed me with your excel file')

uploaded_file = st.file_uploader('Choose an XLSX file')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'What would you like to analyse ?',
        ('Ship Mode', 'Segment', 'Sub-Category'),
    )
    output_columns = ['Sales','Profit']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
    st.dataframe(df_grouped)

    fig = px.bar(
    df_grouped,
    x=groupby_column,
    y='Sales',
    color='Profit',
    color_continuous_scale=['red','yellow','green'],
    template='plotly_white',
    title=f'<b>Sales & Profit by {groupby_column}<b>'
    )
    st.plotly_chart(fig)



