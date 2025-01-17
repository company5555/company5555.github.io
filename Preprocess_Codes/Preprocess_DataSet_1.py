import pandas as pd

# Excel dosyasını yükle
file_path = "Dataset1.xlsx"
sheet_name = "Sheet1"

# Excel dosyasını okuyarak DataFrame oluştur
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit()

# Sütun adlarını kontrol et
required_columns = ['Required Educational Attaintment', 'Related Indusrty']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"Missing columns: {missing_columns}. Available columns:", df.columns)
    exit()

# "Related Indusrty" sütununda "Yok" yazan satırları silme
df = df[df['Related Indusrty'] != "Yok"]

# Eğitim seviyelerini 4 türe indirgeme kurallarını uygulama
def map_educational_attainment(value):
    if value in [
        "No formal educational credential",
        "Postsecondary nondegree award",
        "Some college, no degree",
        "High school diploma or equivalent",
        "Associate's degree",
    ]:
        return "High school diploma or less"
    elif value in ["Bachelor's degree", "Associate's degree"]:
        return "Bachelor's degree"
    elif value == "Master's degree":
        return "Master's degree"
    elif value == "Doctoral or professional degree":
        return "Doctoral or professional degree"
    else:
        return "Unknown"

# Güncellenmiş değerleri yeni bir sütuna yazma
df['Fixed Required Educational Attaintment'] = df['Required Educational Attaintment'].apply(map_educational_attainment)

# Eğitim seviyesi istatistiklerini sektör başına hesaplama
industry_stats = df.groupby(['Related Indusrty', 'Fixed Required Educational Attaintment']).size().reset_index(name='Count')

# Değişiklikleri aynı dosyada güncelleme
try:
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        industry_stats.to_excel(writer, sheet_name="Industry Stats", index=False)
    print(f"Updated Excel file saved back to {file_path}")
except Exception as e:
    print(f"Error updating the Excel file: {e}")