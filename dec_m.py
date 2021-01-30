class Time_this:
    """# класс декотратора для измерения скорости выполнения вашей функции"""
    def __init__(self, num_runs = 10):
        self.num_runs = num_runs

    def __call__(self, func):
        import time
        def wrapper(*args, **kwargs):
            speed = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                speed += t1 - t0
            ever_time = speed / self.num_runs
            print('Среднее время выполнения функции: {} секунд. Функция выполнена: {} раз'.format(ever_time, self.num_runs))
        return  wrapper

# Можете декорировать свою функцию импортировав Time_this из этого модуля 
# Или задекорировать ее прямо здесь ниже:
# Например так:

# Можете декорировать свою функцию импортировав Time_this из этого модуля 
# Или задекорировать ее прямо здесь ниже:
# Например так:

# @Time_this()  # вызываем декоратор
# def my_funcion:
#   .....

#  Для примера можете задекорировать функцию поиска суммы четных чисел фибоначи
# @Time_this()
# def fibon(max_numb):
#     fib = [1, 2]
#     i = 1
#     numb = 3
#     while numb <= max_numb:
#         fib.append(numb)
#         i += 1
#         numb = fib[i] + fib[i - 1]
#     numbers = filter(lambda number: number % 2 == 0, fib)
#     return sum(numbers)

# fibon(99999999999999999)  #  в параметре функции максимальное искомое число фибоначи.
