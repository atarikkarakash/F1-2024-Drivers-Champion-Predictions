import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

# Dosya yolları
file_paths = {
    'austria_gp': 'austriagp.xlsx',
    'bahrain_gp': 'bahraingp.xlsx',
    'canada_gp': 'candagp.xlsx',
    'chinese_gp': 'chinesegp.xlsx',
    'australian_gp': 'australiangp.xlsx',
    'emilia_romagna_gp': 'emilia-romagnagp.xlsx',
    'fastest_laps': 'fastestlaps.xlsx',
    'great_britain_gp': 'greatbritaingp.xlsx',
    'hungary_gp': 'hungarygp.xlsx',
    'japanese_gp': 'japanesegp.xlsx',
    'live_standings': 'livestandings.xlsx',
    'miami_gp': 'miamigp.xlsx',
    'monaco_gp': 'monacogp.xlsx',
    'saudi_arabia_gp': 'saudiarabiagp.xlsx',
    'spain_gp': 'spaingp.xlsx'
}

# Dosyaları oku
dataframes = {name: pd.read_excel(path) for name, path in file_paths.items()}

# Canlı puan durumu verisini alalım
live_standings = dataframes['live_standings']

# Yarış sonuçlarını birleştirme (örnek olarak ilk birkaç dosyayı birleştirelim)
race_results = pd.concat([dataframes['austria_gp'], dataframes['bahrain_gp'], dataframes['canada_gp']])

# Sütun adlarını kontrol edelim
print("Race Results Columns:\n", race_results.columns)

# Sütun adlarını doğru belirleyelim
driver_column = 'DRIVER'
team_column = 'CAR'
points_column = 'PTS'

# Kategorik verileri one-hot encoding ile sayısal verilere dönüştürelim
encoder = OneHotEncoder()
X = encoder.fit_transform(race_results[[driver_column, team_column]]).toarray()

# Puanları hedef değişken olarak alalım
y = race_results[points_column]

# Veriyi eğitim ve test setlerine ayıralım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitelim
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
