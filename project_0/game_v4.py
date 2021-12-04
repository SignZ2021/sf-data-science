"""Игра угадай число
Компьютер сам загадывет и сам отгадывает число методом половинного деления
"""

import numpy as np

def dichotomy_predict(number:int=1) -> int:
    """Угадываем число методом половинного деления

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0   # счетчик попыток
    prdict_number_min = 0  # нижняя граница поиска числа
    prdict_number_max = 101  # верхняя граница поиска числа
    
    while True:
        count += 1
        prdict_number = (prdict_number_max + prdict_number_min) // 2

        if number > prdict_number:
            prdict_number_min = prdict_number  # смещение нижней границы поиска числа       
        elif number < prdict_number:
            prdict_number_max = prdict_number  # смещение верхней границы поиска числа  
        else:
            break # выход из цикла если угадали
        
    return(count)


def score_game(dichotomy_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): фнуция угадывания

    Returns:
        int: среднее количество
    """
    count_ls = []
    #np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(dichotomy_predict(number)) 
    
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(dichotomy_predict)
