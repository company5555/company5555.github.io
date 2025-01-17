import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data
sector_data = {
    "Agriculture, forestry, fishing, and hunting": [53359, 54579, 55799, 57019, 58239, 59458, 60678, 61898, 63118, 64338],
    "Mining": [82052, 83988, 85925, 87861, 89798, 91734, 93671, 95607, 97544, 99480],
    "Utilities": [71410, 72884, 74358, 75832, 77306, 78781, 80255, 81729, 83203, 84677],
    "Construction": [544486, 557612, 570737, 583863, 596989, 610114, 623240, 636366, 649491, 662617],
    "Manufacturing": [955455, 968174, 980894, 993613, 1006332, 1019052, 1031771, 1044491, 1057210, 1069930],
    "Retail trade": [612271, 624474, 636677, 648880, 661082, 673285, 685488, 697691, 709893, 722096],
    "Transportation and warehousing": [376611, 386722, 396833, 406945, 417056, 427167, 437279, 447390, 457501, 467613],
    "Information": [395393, 405420, 415448, 425475, 435502, 445529, 455556, 465583, 475610, 485637],
    "Finance and insurance": [852483, 874607, 896730, 918853, 940976, 963099, 985223, 1007346, 1029469, 1051592],
    "Real estate and rental and leasing": [166855, 171309, 175762, 180215, 184669, 189122, 193575, 198029, 202482, 206935],
    "Management of companies and enterprises": [359203, 369895, 380587, 391279, 401971, 412663, 423355, 434047, 444739, 455431],
    "Educational services": [200831, 206628, 212425, 218221, 224018, 229815, 235611, 241408, 247204, 253001],
    "Health care and social assistance": [1271409, 1308362, 1345315, 1382269, 1419222, 1456175, 1493128, 1530081, 1567034, 1603988],
    "Arts, entertainment, and recreation": [117927, 121023, 124118, 127214, 130310, 133406, 136501, 139597, 142693, 145789],
    "Accommodation and food services": [409186, 420773, 432359, 443945, 455531, 467117, 478703, 490289, 501875, 513461],
    "Government": [1652224, 1687945, 1723667, 1759389, 1795110, 1830832, 1866553, 1902275, 1937997, 1973718]
}

years = list(range(2024, 2034))

# Function to render a line chart
def render_chart(selected_sectors):
    plt.figure(figsize=(12, 6))
    for sector in selected_sectors:
        plt.plot(years, sector_data[sector], label=sector)

    plt.title("Sector Predictions 2024-2033")
    plt.xlabel("Years")
    plt.ylabel("Values")
    plt.xticks(years)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.legend(title="Sectors", loc="upper left", bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.show()

# Example usage
selected_sectors = [
    "Agriculture, forestry, fishing, and hunting",
    "Mining",
    "Utilities",
    "Construction"
]  # Change this list to include desired sectors
render_chart(selected_sectors)
