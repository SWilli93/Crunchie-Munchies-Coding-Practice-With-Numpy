import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
# print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
# print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
# print(median_calories)

first_quarter = np.percentile(calorie_stats, 25)
# print(first_quarter)
third_quarter = np.percentile(calorie_stats, 75)
# print(third_quarter)

more_calories = np.mean(calorie_stats > 60)
# print(more_calories)
calorie_std = np.std(calorie_stats)
# print(calorie_stats)