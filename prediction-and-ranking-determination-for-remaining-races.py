# Kalan yarışlar ve tur sayıları
remaining_races = [
    'Belgium', 'Netherlands', 'Italy', 'Azerbaijan', 'Singapore',
    'United States', 'Mexico', 'Brazil', 'Las Vegas', 'Qatar', 'Abu Dhabi'
]

# Mevcut puan durumu
driver_points = live_standings.set_index('DRIVER')['PTS'].to_dict()

# Puanlama sistemi
points_distribution = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# Tahmin edilen puanları hesapla ve her yarışın sıralamasını belirle
race_results_predictions = {}

for race in remaining_races:
    drivers = live_standings['DRIVER'].unique()
    
    race_predictions = []
    for driver in drivers:
        # Sürücü ve takım bilgilerini hazırlayalım
        driver_team = live_standings[live_standings['DRIVER'] == driver]['TCAR'].values[0]
        
        # Modelimize uygun veri formatını hazırlayalım
        features = pd.DataFrame([[driver, driver_team]], columns=['DRIVER', 'CAR'])
        features_encoded = encoder.transform(features).toarray()
        
        # Puan tahminini yapalım
        predicted_points = model.predict(features_encoded)
        
        # Tahminleri saklayalım
        race_predictions.append((driver, predicted_points[0]))
    
    # Tahminleri puan sırasına göre sırala
    race_predictions.sort(key=lambda x: x[1], reverse=True)
    
    # Yarış sonuçlarını sakla
    race_results_predictions[race] = race_predictions
