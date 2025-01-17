import pandas as pd
import plotly.express as px


file_path = 'Preprocessed_DataSet_3.xlsx'
data = pd.ExcelFile(file_path).parse('Sheet1')


data['Normalized_Wages'] = data['Wages'] / data['Wages'].sum()


color_palette = px.colors.sequential.Pinkyl[2:]  

fig = px.pie(
    data,
    values='Normalized_Wages',
    names='Sectors',
    title='', 
    hover_data={'Wages': ':,.0f'},  
    color_discrete_sequence=color_palette 
)


fig.update_traces(
    textinfo='percent',  
    hovertemplate='Sector: %{label}<br>Wages: %{customdata[0]:,}<br>Percentage: %{percent}'
)

fig.update_layout(
    legend=dict(
        title='Sectors',
        orientation='v', 
        x=1,             
        y=0.5,
        xanchor='left',
        yanchor='middle'
    ),
    margin=dict(t=10, b=10, l=10, r=150) 
)


fig.show()
