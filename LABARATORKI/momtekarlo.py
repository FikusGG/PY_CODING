# # # import random
# # # a_init = float(input('Введите коэффициент a в y = a + bх: '))
# # # b_init = float(input('Введите коэффициент b в y = a + bх: '))
# # # x = [random.uniform(0.0, 100.0) for _ in range(10000)]
# # # y = [a_init + b_init * xi for xi in x]
# # # def least_squares(x, y):
# # #     n = len(x)
# # #     sum_x = sum(x)
# # #     sum_y = sum(y)
# # #     sum_xy = sum(xi * yi for xi, yi in zip(x, y))
# # #     sum_x2 = sum(xi ** 2 for xi in x)
# # #     denominator = n * sum_x2 - sum_x ** 2
# # #     b = (n * sum_xy - sum_x * sum_y) / denominator
# # #     a = (sum_y - b * sum_x) / n
# # #     return a, b
# # # a_calc, b_calc = least_squares(x, y)
# # # print(f"Исходные коэффициенты: a = {a_init}, b = {b_init}")
# # # print(f"Вычисленные коэффициенты: a = {a_calc}, b = {b_calc}")
# # # print(f"Разница в коэффициенте a: {abs(a_init - a_calc)}")
# # # print(f"Разница в коэффициенте b: {abs(b_init - b_calc)}")


# # # import random
# # # def bubble_sort(arr):
# # #     n = len(arr)
# # #     for i in range(n):
# # #         for j in range(0, n-i-1):
# # #             if arr[j] > arr[j+1]:
# # #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# # # def quick_sort(arr):
# # #     if len(arr) <= 1:
# # #         return arr
# # #     pivot = arr[len(arr) // 2]
# # #     left = [x for x in arr if x < pivot]
# # #     middle = [x for x in arr if x == pivot]
# # #     right = [x for x in arr if x > pivot]
# # #     return quick_sort(left) + middle + quick_sort(right)
# # # def binary_search(arr, x):
# # #     low, high = 0, len(arr) - 1
# # #     while low <= high:
# # #         mid = (low + high) // 2
# # #         if arr[mid] < x:
# # #             low = mid + 1
# # #         elif arr[mid] > x:
# # #             high = mid - 1
# # #         else:
# # #             return mid
# # #     return -1
# # # def insertion_sort(arr):
# # #     """Сортировка вставками"""
# # #     for i in range(1, len(arr)):
# # #         key = arr[i]
# # #         j = i - 1
# # #         while j >= 0 and arr[j] > key:
# # #             arr[j + 1] = arr[j]
# # #             j -= 1
# # #         arr[j + 1] = key
# # # N = 10_000
# # # arr = [random.uniform(0.0, 100.0) for _ in range(N)]
# # # x = random.choice(arr)
# # # sorted_quick = quick_sort(arr.copy())
# # # sorted_insertion = arr.copy()
# # # insertion_sort(sorted_insertion)
# # # idx = binary_search(sorted_quick, x)
# # # if sorted_quick == sorted_insertion and sorted_quick[idx] == x:
# # #     print("Good")
# # # else:
# # #     print("Bad")
    
    
    
    
    
# # # def euler_solve(f, y0, t_start, t_end, step):
# # #     t, y = t_start, y0
# # #     result = [(t, y)]
    
# # #     while t < t_end:
# # #         y += step * f(t, y)
# # #         t += step
# # #         result.append((t, y))
    
# # #     return result
# # # def improved_euler_solve(f, y0, t_start, t_end, step):
# # #     t, y = t_start, y0
# # #     result = [(t, y)]
    
# # #     while t < t_end:
# # #         k1 = step * f(t, y)
# # #         k2 = step * f(t + step, y + k1)
# # #         y += (k1 + k2) / 2
# # #         t += step
# # #         result.append((t, y))
# # #     return result
# # # def equation(t, y):
# # #     return y - t**2 + 1
# # # y_start = 0.5
# # # t_start = 0
# # # t_end = 2
# # # step = 0.1
# # # euler_result = euler_solve(equation, y_start, t_start, t_end, step)
# # # improved_result = improved_euler_solve(equation, y_start, t_start, t_end, step)
# # # print("Метод Эйлера:")
# # # for t, y in euler_result[::10]:  # Выводим каждые 10 шагов для краткости
# # #     print(f"t = {t:.1f}, y = {y:.4f}")

# # # print("\nУлучшенный метод Эйлера:")
# # # for t, y in improved_result[::10]:
# # #     print(f"t = {t:.1f}, y = {y:.4f}")
# # # print("\nСравнение в конечной точке:")
# # # print(f"Метод Эйлера: y({t_end}) = {euler_result[-1][1]:.6f}")
# # # print(f"Улучшенный метод: y({t_end}) = {improved_result[-1][1]:.6f}")

# # import numpy as np
# # import matplotlib.pyplot as plt
# # def euler_method(f, t0, y0, h, n):
# #     t = np.zeros(n+1)
# #     y = np.zeros(n+1)
# #     t[0] = t0
# #     y[0] = y0
# #     for i in range(n):
# #         y[i+1] = y[i] + h * f(t[i], y[i])
# #         t[i+1] = t[i] + h  
# #     return t, y
# # def heun_method(f, t0, y0, h, n):
# #     t = np.zeros(n+1)
# #     y = np.zeros(n+1)
# #     t[0] = t0
# #     y[0] = y0
    
# #     for i in range(n):
# #         k1 = f(t[i], y[i])
# #         k2 = f(t[i] + h, y[i] + h * k1)
# #         y[i+1] = y[i] + h * (k1 + k2) / 2
# #         t[i+1] = t[i] + h
# #     return t, y

# # def rk4_method(f, t0, y0, h, n):
# #     t = np.zeros(n+1)
# #     y = np.zeros(n+1)
# #     t[0] = t0
# #     y[0] = y0
    
# #     for i in range(n):
# #         k1 = f(t[i], y[i])
# #         k2 = f(t[i] + h/2, y[i] + h/2 * k1)
# #         k3 = f(t[i] + h/2, y[i] + h/2 * k2)
# #         k4 = f(t[i] + h, y[i] + h * k3)
# #         y[i+1] = y[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
# #         t[i+1] = t[i] + h
    
# #     return t, y

# # def compare_methods(f, t0, y0, h, n, exact_solution=None):
# #     t_euler, y_euler = euler_method(f, t0, y0, h, n)
# #     t_heun, y_heun = heun_method(f, t0, y0, h, n)
# #     t_rk4, y_rk4 = rk4_method(f, t0, y0, h, n)
# #     plt.figure(figsize=(10, 6))
# #     plt.plot(t_euler, y_euler, label='Метод Эйлера')
# #     plt.plot(t_heun, y_heun, label='Метод Хойна')
# #     plt.plot(t_rk4, y_rk4, label='Метод Рунге-Кутта 4')
# #     if exact_solution is not None:
# #         y_exact = exact_solution(t_euler)
# #         plt.plot(t_euler, y_exact, 'k--', label='Точное решение')
    
# #     plt.xlabel('t')
# #     plt.ylabel('y(t)')
# #     plt.title('Сравнение методов численного интегрирования')
# #     plt.legend()
# #     plt.grid()
# #     plt.show()
    
# #     if exact_solution is not None:
# #         errors = {
# #             'Euler': np.abs(y_euler - y_exact),
# #             'Heun': np.abs(y_heun - exact_solution(t_heun)),
# #             'RK4': np.abs(y_rk4 - exact_solution(t_rk4))
# #         }
# #         avg_errors = {method: np.mean(err) for method, err in errors.items()}
# #         print("Средние абсолютные ошибки:")
# #         for method, err in avg_errors.items():
# #             print(f"{method}: {err:.6f}")
# #         max_errors = {method: np.max(err) for method, err in errors.items()}
# #         print("\nМаксимальные абсолютные ошибки:")
# #         for method, err in max_errors.items():
# #             print(f"{method}: {err:.6f}")
# # if __name__ == "__main__":
# #     def f1(t, y):
# #         return y
# #     def exact_solution1(t):
# #         return np.exp(t)
# #     print("Пример 1: y' = y, y(0) = 1")
# #     compare_methods(f1, t0=0, y0=1, h=0.1, n=20, exact_solution=exact_solution1)

# #     def f2(t, y):
# #         return t - y
    
# #     def exact_solution2(t):
# #         return 2*np.exp(-t) + t - 1
    
# #     print("\nПример 2: y' = t - y, y(0) = 1")
# #     compare_methods(f2, t0=0, y0=1, h=0.2, n=25, exact_solution=exact_solution2)
    
# #     def f3(t, y):
# #         return -2 * t * y
    
# #     def exact_solution3(t):
# #         return np.exp(-t**2)
    
# #     print("\nПример 3: y' = -2ty, y(0) = 1")
# #     compare_methods(f3, t0=0, y0=1, h=0.1, n=30, exact_solution=exact_solution3)

# def euler(f, t0, y0, h, n):
#     t, y = [t0], [y0]
#     for _ in range(n):
#         y.append(y[-1] + h * f(t[-1], y[-1]))
#         t.append(t[-1] + h)
#     return y

# def heun(f, t0, y0, h, n):
#     t, y = [t0], [y0]
#     for _ in range(n):
#         k1 = f(t[-1], y[-1])
#         k2 = f(t[-1] + h, y[-1] + h * k1)
#         y.append(y[-1] + h * (k1 + k2) / 2)
#         t.append(t[-1] + h)
#     return y

# def rk4(f, t0, y0, h, n):
#     t, y = [t0], [y0]
#     for _ in range(n):
#         k1 = f(t[-1], y[-1])
#         k2 = f(t[-1] + h/2, y[-1] + h/2 * k1)
#         k3 = f(t[-1] + h/2, y[-1] + h/2 * k2)
#         k4 = f(t[-1] + h, y[-1] + h * k3)
#         y.append(y[-1] + h * (k1 + 2*k2 + 2*k3 + k4) / 6)
#         t.append(t[-1] + h)
#     return y

# def exact(t):
#     return 2 * 2.71828**(-t) + t - 1  # 2*e^(-t) + t - 1

# y_euler = euler(lambda t, y: t - y, 0, 1, 0.2, 10)
# y_heun = heun(lambda t, y: t - y, 0, 1, 0.2, 10)
# y_rk4 = rk4(lambda t, y: t - y, 0, 1, 0.2, 10)

# print("Средние ошибки:")
# print(f"Эйлера: {sum(abs(y - exact(0.2*i)) for i,y in enumerate(y_euler))/11:.6f}")
# print(f"Хойна:  {sum(abs(y - exact(0.2*i)) for i,y in enumerate(y_heun))/11:.6f}")
# print(f"РК4:    {sum(abs(y - exact(0.2*i)) for i,y in enumerate(y_rk4))/11:.6f}")
    

def euler_method(f, yo, to, tn, h):
    t = [t0]
    y = [y0]
    while t[-1] < tn:
        y_new = y[-1] + h * f(t[-1], y[-1])
        t_new = t[-1] + h
        y.append (y_new)
        t. append(t_new)
    return t, y
def improved_euler_method(f, yo, to, tn, h):
    t = [to]
    y = [y0]
    while t[-1] < tn:
        k1 = h * f(t[-1], y[-1])
        k2 = h * f(t[-1] + h, y[-1] + k1)
        y_new = [-1] + (k1 + k2) / 2
        t_new = t[-1] + h
        y. append (y_new)
        t. append(t_new)
    return t, y
def runge_kutta method(f, yo, to, tn, h):
    t = [t0]
    y = [y0]
    while t[-1] < tn:
        k1 = h * f(t[-1], y[-1])
        k2 = h * f(t[-1] + h/2, y[-1] + k1/2)
        k3 = h * f(t[-1] + h/2, y[-1] + k2/2)
        k4 = h * f(t[-1] + h, y[-1] + k3)


        y_new = y[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t_new = t[-1] + h
        y.append (y_new)
        t.append(t_new)


def f(t, y):
    """Пример функции: у' = у - t*2 + 1"""
    return y - t**2 + 1
yo = 0.5
t0 = 0
h = 0.1
t_euler, y_euler = euler_method(f, ye, to, tn, h)
t_improved, Y_improved = improved_euler_method(f, yo, te, tm, h)
t_rk, y_rk = runge_kutta method(f, yo, to, tm, h)
print ("Метод эйлера (последнее значение):", y-euler [-1]) 
print ("Улучшенный метод Эйлера:", y_improved[-1])
print ("Метод Рунге-кутты:", У_гk[-1])