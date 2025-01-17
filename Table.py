import pandas as pd
import plotly.express as px

# Dosyayı yükle
file_path = 'Table_DataSet_3'
data = pd.ExcelFile(file_path).parse('Sheet1')

# Her sektörün normalize edilmiş maaş oranını hesapla
data['Normalized_Wages'] = data['Wages'] / data['Wages'].sum()

# Pinkyl paletinden beyaz renkleri hariç tut
color_palette = px.colors.sequential.Pinkyl[2:]  # İlk birkaç beyaz tona karşılık gelen renkleri çıkar

# Pie chart oluştur
fig = px.pie(
    data,
    values='Normalized_Wages',
    names='Sectors',
    title='',  # Başlık kaldırıldı
    hover_data={'Wages': ':,.0f'},  # Hover'da maaş bilgisini formatla
    color_discrete_sequence=color_palette  # Beyazsız Pinkyl renk paleti
)

# Dilim oranlarını göster ve hover formatını düzenle
fig.update_traces(
    textinfo='percent',  # Dilimlerin üzerinde sadece oranları göster
    hovertemplate='Sector: %{label}<br>Wages: %{customdata[0]:,}<br>Percentage: %{percent}'
)

# Legend ayarlarını düzenle
fig.update_layout(
    legend=dict(
        title='Sectors',
        orientation='v',  # Dikey legend
        x=1,              # Legend'i grafiğin sağına hizala
        y=0.5,
        xanchor='left',
        yanchor='middle'
    ),
    margin=dict(t=10, b=10, l=10, r=150)  # Sağda legend için yer bırak
)

# Grafiği göster
fig.show()
