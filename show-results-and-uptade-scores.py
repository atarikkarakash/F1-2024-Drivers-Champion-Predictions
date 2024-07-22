# Her yarış sonrası puanları güncelle ve sonuçları göster
for race, race_predictions in race_results_predictions.items():
    print(f"Race: {race}")
    for i, (driver, points) in enumerate(race_predictions):
        if i < 10:  # İlk 10 sürücüye puanları dağıt
            driver_points[driver] += points_distribution[i]
        print(f"{i+1}. {driver} - Predicted Points: {points}")
    
    # Güncellenmiş puan durumu
    print("\nUpdated Points After", race)
    for driver, points in driver_points.items():
        print(f"Driver: {driver}, Points: {points}")
    print("\n-----------------------------\n")

# Sezon sonu puanlarını göster
print("Season End Points:")
for driver, points in driver_points.items():
    print(f"Driver: {driver}, Points: {points}")

# Şampiyonu belirle
champion = max(driver_points, key=driver_points.get)
print(f"Champion: {champion}, Points: {driver_points[champion]}")
