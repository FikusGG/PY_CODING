# # # # import random
# # # # points = 1000000
# # # # inside= 0
# # # # for _ in range(points):
# # # #     x = random.random()
# # # #     y = random.random()
# # # #     if x**2+y**2<= 1:
# # # #         inside+=1
# # # # pi=4*inside/points
# # # # print(pi)
# # # # import numpy as np
# # # # def compute_alpha(u, v, w):
# # # #     return u + v + w
# # # # def generate_random_values(k, n):
# # # #     u = np.random.uniform(low=0, high=1, size=n)
# # # #     v = np.random.uniform(low=0, high=1, size=n)
# # # #     w = np.random.uniform(low=0, high=1, size=n)
# # # #     return k * compute_alpha(u, v, w)
# # # # def calculate_density(data, bins, n):
# # # #     frequencies, intervals = np.histogram(data, bins=bins, range=(min(data), max(data)))
# # # #     mid_intervals = (intervals[:-1] + intervals[1:]) / 2
# # # #     return mid_intervals, frequencies
# # # # k_value = float(input("Введите коэффициент k: "))
# # # # bins_count = int(input("Введите количество интервалов: "))
# # # # points_count = int(input("Введите количество случайных точек: "))
# # # # random_data = generate_random_values(k_value, points_count)
# # # # midpoints, counts = calculate_density(random_data, bins_count, points_count)
# # # # print("Центр интервала - количество точек")
# # # # for center, frequency in zip(midpoints, counts):
# # # #     print(f"{center:.4f} - {frequency}")

# # # import random

# # # def compute_alpha(u, v, w):
# # #     return u + v + w

# # # def generate_random_values(k, n):
# # #     u = [random.uniform(0, 1) for _ in range(n)]
# # #     v = [random.uniform(0, 1) for _ in range(n)]
# # #     w = [random.uniform(0, 1) for _ in range(n)]
# # #     return [k * compute_alpha(u[i], v[i], w[i]) for i in range(n)]

# # # def calculate_density(data, bins):
# # #     min_val = min(data)
# # #     max_val = max(data)
# # #     bin_width = (max_val - min_val) / bins
# # #     frequencies = [0] * bins
# # #     intervals = [min_val + i * bin_width for i in range(bins + 1)]
    
# # #     for value in data:
# # #         bin_index = int((value - min_val) // bin_width)
# # #         if bin_index >= bins:
# # #             bin_index = bins - 1
# # #         frequencies[bin_index] += 1
    
# # #     mid_intervals = [(intervals[i] + intervals[i + 1]) / 2 for i in range(bins)]
# # #     return mid_intervals, frequencies

# # # k_value = float(input("Введите коэффициент k: "))
# # # bins_count = int(input("Введите количество интервалов: "))
# # # points_count = int(input("Введите количество случайных точек: "))

# # # random_data = generate_random_values(k_value, points_count)
# # # midpoints, counts = calculate_density(random_data, bins_count)

# # # print("Центр интервала - количество точек")
# # # for center, frequency in zip(midpoints, counts):
# # #     print(f"{center:.4f} - {frequency}")

# # # import numpy as np
# # # def generate_eta(M):
# # #     xi = np.random.uniform(0, 1, (6, M))  
# # #     return np.sum(xi, axis=0)  
# # # def calculate_histogram(data, N, min_val, max_val):
# # #     counts, bin_edges = np.histogram(data, bins=N, range=(min_val, max_val))
# # #     bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
# # #     return bin_midpoints, counts
# # # def main():
# # #     print("Определение функции плотности вероятности случайной величины η = ξ₁ + ξ₂ + ξ₃ + ξ₄ + ξ₅ + ξ₆")
# # #     N = int(input("Введите количество диапазонов разбиения (N): "))
# # #     M = int(input("Введите количество точек (M): "))
# # #     eta_values = generate_eta(M)
# # #     min_val, max_val = 0, 6
# # #     bin_midpoints, counts = calculate_histogram(eta_values, N, min_val, max_val)
# # #     print("\nРезультаты:")
# # #     print("Середина диапазона - Количество точек - Плотность вероятности")
# # #     bin_width = (max_val - min_val) / N
# # #     for midpoint, count in zip(bin_midpoints, counts):
# # #         density = count / (M * bin_width)  # Нормировка для получения плотности вероятности
# # #         print(f"{midpoint:.4f} - {count} - {density:.6f}")

# # # if __name__ == "__main__":
# # #     main()

# # import numpy as np

# # def generate_eta(M):
# #     xi = np.random.uniform(0, 1, (6, M))  
# #     return np.sum(xi, axis=0)  

# # def calculate_histogram(data, N, min_val, max_val):
# #     counts, bin_edges = np.histogram(data, bins=N, range=(min_val, max_val))
# #     bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
# #     return bin_midpoints, counts

# # def main():
# #     print("Определение функции плотности вероятности случайной величины η = ξ₁ + ξ₂ + ξ₃ + ξ₄ + ξ₅ + ξ₆")
    
# #     N = int(input("Введите количество диапазонов разбиения (N): "))
# #     M = int(input("Введите количество точек (M): "))
    
# #     eta_values = generate_eta(M)
# #     min_val, max_val = 0, 1
# #     bin_midpoints, counts = calculate_histogram(eta_values, N, min_val, max_val)
    
# #     print("\nРезультаты:")
# #     print("Середина диапазона  Количество точек  Плотность вероятности")
    
# #     bin_width = (max_val - min_val) / N
# #     for midpoint, count in zip(bin_midpoints, counts):
# #         density = count / (M * bin_width)
# #         print(f"{midpoint:.4f}  В{count:6}  {density:.6f}")

# # if __name__ == "__main__":
# #     main()

# import numpy as np
# import matplotlib.pyplot as plt
# def plot_random_points():
    
#     print("Введите границы:")
#     x_min = float(input("x_min: "))
#     x_max = float(input("x_max: "))
#     y_min = float(input("y_min: "))
#     y_max = float(input("y_max: "))
    
#     np.random.seed(42) 
#     x_points = np.random.uniform(x_min, x_max, 100)
#     y_points = np.random.uniform(y_min, y_max, 100)
#     plt.figure(figsize=(12, 10))
#     plt.scatter(x_points, y_points, color='pink', marker='o', label='Случайные точки')
    
#     plt.title('Массив точек.')
#     plt.xlabel('ось X')
#     plt.ylabel('ось Y')
    
#     plt.grid(True)
#     plt.legend()
    
#     plt.show()
# plot_random_points()

# import matplotlib.pyplot as plt
# import numpy as np
# def plot_functions():
#     x = np.linspace(-5, 5, 20)
#     y1 = x**2  # Парабола
#     y2 = x**3 # Кубическая парабола
#     plt.figure(figsize=(10, 6))
#     plt.plot(x, y1, linestyle='-', color='red', label='y = x**2')  
#     plt.plot(x, y2, linestyle='--', color='violet', label='x**3')  
#     plt.title('Функции:')
#     plt.xlabel('Ось x')
#     plt.ylabel('Ось y')
#     plt.grid(True)
#     plt.legend()
#     plt.show()
# plot_functions()

from PIL import Image
def adjust_brightness(image_path, factor, output_path):

    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            r = min(255, int(r * factor))
            g = min(255, int(g * factor))
            b = min(255, int(b * factor))
            pixels[x, y] = (r, g, b)
    img.save(output_path)
    print(f"Изображение сохранено как {output_path}")
adjust_brightness("LABARATORKI\input.png", 1.5, "LABARATORKI\OUTPUT.jpg")
  
# from PIL import Image
# def replace_white_pixels(image_path, new_color, threshold, output_path):
#     img = Image.open(image_path)
#     pixels = img.load()
#     width, height = img.size
#     for x in range(width):
#         for y in range(height):
#             r, g, b = pixels[x, y][:3]
#             if r > threshold and g > threshold and b > threshold:
#                 pixels[x, y] = new_color
    
#     img.save(output_path)
#     print(f"Изображение с замененными пикселями сохранено как {output_path}")
# replace_white_pixels("LABARATORKI\DrJWeOFrpCI.jpg", (0, 0, 0), 110, "LABARATORKI\OUTPUT.jpg")

# from PIL import Image
# import matplotlib.pyplot as plt

# def analyze_image(image_path, brightness_threshold, white_threshold):
#     img = Image.open(image_path)
#     pixels = img.load()
#     width, height = img.size
#     bright_pixels = 0
#     white_pixels = 0
#     total_pixels = width * height
#     for x in range(width):
#         for y in range(height):
#             r, g, b = pixels[x, y][:3]
#             brightness = (r + g + b) / 3
            
#             if brightness > brightness_threshold:
#                 bright_pixels += 1
                
#             if r > white_threshold and g > white_threshold and b > white_threshold:
#                 white_pixels += 1
    
#     print(f"Общее количество пикселей: {total_pixels}")
#     print(f"Ярких пикселей (> {brightness_threshold}): {bright_pixels} ({bright_pixels/total_pixels*100:.2f}%)")
#     print(f"Белых пикселей (> {white_threshold}): {white_pixels} ({white_pixels/total_pixels*100:.2f}%)")
#     plt.hist([sum(pixels[x, y][:3])/3 for x in range(width) for y in range(height)], bins=50)
#     plt.title("Распределение яркости пикселей")
#     plt.xlabel("Яркость")
#     plt.ylabel("Количество пикселей")
#     plt.show()
# analyze_image("LABARATORKI\DrJWeOFrpCI.jpg",100,100)

# import random
# def bubble_sort(arr):
#     print(arr)
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     print(arr)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#     print(arr)
# def binary_search(arr, x):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1
# def insertion_sort(arr):
#     """Сортировка вставками"""
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
# N = 100
# arr = [random.uniform(0.0, 100.0) for _ in range(N)]
# x = random.choice(arr)
# sorted_quick = quick_sort(arr.copy())
# sorted_insertion = arr.copy()
# insertion_sort(sorted_insertion)
# idx = binary_search(sorted_quick, x)
# print(arr)
# if sorted_quick == sorted_insertion and sorted_quick[idx] == x:
#     print("Good")
# else:
#     print("Bad")
# print(quick_sort(arr))
    