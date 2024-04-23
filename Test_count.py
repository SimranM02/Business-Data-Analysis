#Test count in each city printed test-wise
import pandas as pd
import matplotlib.pyplot as plt

def analyze_blood_test_dataset(file_path):
    data = pd.read_csv(file_path)

    grouped_data = data.groupby('Test Name')

    for test_name, test_data in grouped_data:
        location_data = test_data.groupby('Location')

        cities = []
        test_counts = []

        for city, city_test_data in location_data:
            cities.append(city)
            test_counts.append(len(city_test_data))

        plt.figure(figsize=(4, 3))
        plt.bar(cities, test_counts)
        plt.title(f"Blood Test Distribution - {test_name}")
        plt.xlabel("City")
        plt.ylabel("Test Count")
        plt.xticks(rotation=90)
        plt.show()

file_path = "/content/blood test data.csv"
analyze_blood_test_dataset(file_path)
