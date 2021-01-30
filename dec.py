
# Функция декотратор для измерения скорости выполнения вашей функции
def time_this(num_runs = 10):
    def s_tester(func):
        import time
        def wrapper(*args, **kwargs):
            speed = 0
            for _ in range(num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                speed += t1 - t0
            ever_time = speed / num_runs
            print('Функция выаолнена {} раз. Среднее время выполнения функции: {} секунд'.format(num_runs, ever_time))
        return wrapper
    return s_tester

if __name__ == "__main__":

# Можете декорировать свою функцию импортировав time_this из этого модуля 
# Или задекорировать ее прямо здесь ниже:
# Например так:

    # @time_this(50)  (В аргументы декоратора можно передать количество запусков декорированой функции по умолчанию 10 здесь 50)
    # def my_func():
    #    ........

    # Или погонять поиск суммы четных чисел фибоначи как ниже
    # @time_this(50)
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

    # fibon(9999999999)
     # параметр - максимальное число фибоначи которое функция будет  искать.
