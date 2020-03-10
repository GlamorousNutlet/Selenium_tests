import datetime as dt

def factor(num):
    time_before = dt.datetime.now()
    count = 1
    for i in range(1, num+1):
        count *= i
    time_after = dt.datetime.now()
    delta_time = time_after - time_before
    return f'Значение факториала = {count}. Времени затрачено: {delta_time}'


print(factor(3265))