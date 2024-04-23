#Healthy vs Unhealthy Data
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/Test results citywise.csv')

test_names = data['Test Name'].unique()
cities = data['Location'].unique()

color_healthy = 'green'
color_unhealthy = 'coral'

bar_width = 0.4

for test in test_names:
    test_data = data[data['Test Name'] == test]

    plt.figure()
    plt.figure(figsize=(4, 3))

    city_indices = range(len(cities))
    healthy_bar_x = [index - bar_width/2 for index in city_indices]
    unhealthy_bar_x = [index + bar_width/2 for index in city_indices]

    for city, healthy_x, unhealthy_x in zip(cities, healthy_bar_x, unhealthy_bar_x):
        city_data = test_data[test_data['Location'] == city]

        if not city_data.empty:  # Check if city_data is not empty
            test_results = city_data['Test Result']
            healthy_range_left = city_data['Healthy Range Left'].iloc[0]
            healthy_range_right = city_data['Health Range Right'].iloc[0]

            is_healthy = (test_results >= healthy_range_left) & (test_results <= healthy_range_right)

            num_healthy = sum(is_healthy)
            num_unhealthy = len(is_healthy) - num_healthy

            plt.bar(healthy_x, num_healthy, width=bar_width, color=color_healthy)
            plt.bar(unhealthy_x, num_unhealthy, width=bar_width, color=color_unhealthy)

    plt.title(f'{test} - Test Results')
    plt.xlabel('City')
    plt.ylabel('Number of People')
    plt.xticks(rotation=90)
    plt.xticks(range(len(cities)), cities)
    plt.legend(['Healthy', 'Unhealthy'])
    plt.show()
