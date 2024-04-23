#test pricing in each city ascending order
import pandas as pd
import matplotlib.pyplot as plt

def analyze_blood_test_dataset(file_path):
    data = pd.read_csv(file_path)

    grouped_data = data.groupby('Test Name')

    for test_name, test_data in grouped_data:
        city_data = test_data.groupby('Location')

        cities = []
        costs = []

        for city, city_test_data in city_data:
            cities.append(city)
            max_cost = city_test_data['Price ($)'].max()
            costs.append(max_cost)

        sorted_data = sorted(zip(cities, costs), key=lambda x: x[1])
        cities, costs = zip(*sorted_data)

        most_expensive_index = costs.index(max(costs))

        colors = ['lightskyblue'] * len(cities)
        colors[most_expensive_index] = 'lightcoral'

        plt.figure(figsize=(4, 3))
        plt.bar(cities, costs, color=colors)
        plt.title(f"Relative test pricing in different cities - {test_name}")
        plt.xlabel("City")
        plt.ylabel("Price ($)")
        plt.xticks(rotation=90)
        plt.show()

file_path = "/content/blood test data.csv"
analyze_blood_test_dataset(file_path)
