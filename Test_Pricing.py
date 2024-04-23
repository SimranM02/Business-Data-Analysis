#costliest test in each city
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_blood_test_dataset(file_path):
    f = open(file_path);

    data = pd.read_csv(file_path)

    grouped_data = data.groupby('Location')

    locations = []
    test_names = []
    average_costs = []

    for location, location_data in grouped_data:
        locations.append(location)

        test_costs = location_data.groupby('Test Name')['Cost ($)'].mean()

        for test_name, cost in test_costs.items():
            test_names.append(test_name)
            average_costs.append(cost)

        plt.figure(figsize=(8, 6))
        plt.bar(test_names, average_costs)
        plt.title(f"Blood Test Costs in {location}")
        plt.xlabel("Test Name")
        plt.ylabel("Average Cost ($)")
        plt.xticks(rotation=90)
        plt.show()

        test_names.clear()
        average_costs.clear()

file_path = "/content/blood test data.csv"
analyze_blood_test_dataset(file_path)
