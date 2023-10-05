def manhattan_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += abs(point1[i] - point2[i])
    return distance

# Өрнектер
point1 = [1, 2, 3]
point2 = [4, 5, 6]

# Манхэттен қашықтығын есептеу
distance = manhattan_distance(point1, point2)
print(f"Манхэттен қашықтығы: {distance}")