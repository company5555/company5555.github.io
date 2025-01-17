import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = 'Preprocessed_Dataset2.xlsx'  # Replace with your file's actual path
df_viz = pd.read_excel(file_path, sheet_name='Sheet2')  # Adjust sheet_name if needed


# Create a figure to display two separate horizontal bar charts with adjusted width and height
fig, (ax1, ax2) = plt.subplots(
    1, 2, 
    figsize=(10, len(df_viz) * 1.5),  # Adjusted dimensions
    gridspec_kw={'width_ratios': [1.5, 1], 'wspace': 0.3}
)

# Plot Median Annual Earnings ($)
ax1.barh(df_viz['Educational attainment'], df_viz['Median usual annual earnings ($)'], color='#FF7F7F', alpha=0.8)
for i, value in enumerate(df_viz['Median usual annual earnings ($)']):
    ax1.text(value, i, f"${int(value):,}", va='center', ha='left', fontsize=10, color='darkred')

# Format the first chart
ax1.set_yticks(range(len(df_viz['Educational attainment'])))
ax1.set_yticklabels(df_viz['Educational attainment'], fontsize=12)
ax1.invert_yaxis()
ax1.set_xticks([])  # Remove x-axis ticks
ax1.set_title('Median Annual Earnings', fontsize=14, pad=20)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

# Plot Unemployment Rate (%)
ax2.barh(df_viz['Educational attainment'], df_viz['Unemployment rate (%)'], color='#FFB266', alpha=0.8)
for i, value in enumerate(df_viz['Unemployment rate (%)']):
    ax2.text(value, i, f"{value:.1f}%", va='center', ha='left', fontsize=10, color='darkorange')

# Format the second chart
ax2.set_yticks([])  # Remove y-axis ticks and labels
ax2.invert_yaxis()
ax2.set_xticks([])  # Remove x-axis ticks
ax2.set_title('Unemployment Rate', fontsize=14, pad=20)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

# Save the chart as an image
plt.tight_layout()
plt.savefig('chart_output.png', dpi=300, bbox_inches='tight')
print("Chart saved as chart2_output.png")