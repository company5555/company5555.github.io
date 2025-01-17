import plotly.graph_objects as go

# Original wage data
wages = [
    55689, 72886, 75770, 634697, 1083951, 659293, 448489, 465671, 911932, 187898,
    379764, 206505, 1377762, 135172, 477843, 1732777
]

# Normalize wages for "values"
total_wages = sum(wages)
normalized_values = [wage / total_wages for wage in wages]

# Labels for sectors
labels = [
    "Agriculture, forestry, fishing, and hunting",
    "Mining",
    "Utilities",
    "Construction",
    "Manufacturing",
    "Retail trade",
    "Transportation and warehousing",
    "Information",
    "Finance and insurance",
    "Real estate and rental and leasing",
    "Management of companies and enterprises",
    "Educational services",
    "Health care and social assistance",
    "Arts, entertainment, and recreation",
    "Accommodation and food services",
    "Government"
]

# Colors for the pie chart
colors = [
    "#FFEDA0", "#FED976", "#FEB24C", "#FD8D3C", "#F03B20", "#BD0026",
    "#800026", "#FF6600", "#FF8C00", "#FFB732", "#FFBA5C", "#FF9440",
    "#FF7043", "#FF3D2F", "#E60019", "#990000"
]

# Create the pie chart
data = go.Pie(
    labels=labels,
    values=normalized_values,
    textinfo="percent",
    hovertemplate="Sector: %{label}<br>Wages: $%{customdata:,}<br>Percentage: %{percent}",
    customdata=wages,
    marker=dict(colors=colors)
)

layout = go.Layout(
    title_text="Sector Wages Pie Chart",
    legend=dict(
        title=dict(text="Sectors"),
        orientation="v",
        x=1,
        y=0.5,
        xanchor="left",
        yanchor="middle"
    ),
    margin=dict(t=10, b=10, l=10, r=150)
)

fig = go.Figure(data=[data], layout=layout)

# Show the plot
fig.show()
