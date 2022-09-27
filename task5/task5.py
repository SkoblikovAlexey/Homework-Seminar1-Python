# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coord_list_a = input("Введите координаты точки А через запятую: ").split(",")
coord_list_b = input("Введите координаты точки B через запятую: ").split(",")
x1 = int(coord_list_a[0])
x2 = int(coord_list_b[0])
y1 = int(coord_list_a[1])
y2 = int(coord_list_b[1])
def dist(x1, x2, y1, y2):
    distance = (pow((x2 - x1), 2) + pow((y2 - y1), 2)) ** (0.5)
    return distance
distance = round(dist(x1, x2, y1, y2), 2)
print(f"Расстояние между точками А и В равно {distance}")