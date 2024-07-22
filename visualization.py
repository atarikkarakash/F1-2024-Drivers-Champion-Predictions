import matplotlib.pyplot as plt

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
all_driver_points_over_time = {driver: [points] for driver, points in driver_points.items()}

for race in remaining_races:
    drivers = live_standings['DRIVER'].unique()
    
    race_predictions = []
    for driver in drivers:
        # Sürücü ve takım bilgilerini hazırlayalım
        driver_team = live_standings[live_standings['DRIVER'] == driver]['CAR'].values[0]
        
        # Modelimize uygun veri formatını hazırlayalım
        features = pd.DataFrame([[driver, driver_team]], columns=['DRIVER', 'CAR'])
        features_encoded = encoder.transform(features).toarray()
        
        # Puan tahminini yapalım
        predicted_points = model.predict(features_encoded)
        
        # Tahminleri saklayalım
        race_predictions.append((driver, predicted_points[0]))
    
    # Tahminleri puan sırasına göre sırala
    race_predictions.sort(key=lambda x: x[1], reverse=True)
    
    # İlk 10 sürücüye puanları dağıt
    for i, (driver, _) in enumerate(race_predictions[:10]):
        driver_points[driver] += points_distribution[i]
    
    # Her yarış sonrası güncellenmiş puanları kaydet
    for driver in driver_points.keys():
        all_driver_points_over_time[driver].append(driver_points[driver])

# Sonuçları görselleştirelim
plt.figure(figsize=(14, 8))
for driver, points_over_time in all_driver_points_over_time.items():
    plt.plot(remaining_races, points_over_time[1:], marker='o', label=driver)

plt.xlabel('Races')
plt.ylabel('Points')
plt.title('Driver Points Over Remaining Races')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
