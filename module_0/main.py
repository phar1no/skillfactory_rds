import numpy as np

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
           predict += 1
        elif number < predict:
            predict -= 1

    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Улучшенная версия game_core_v2, следущее предсказание будет выбрано из среднего от двух предыдущих или от предыдущего предсказания и минимально или максимально возможного числа '''
    count = 0
    first=1
    last=100
    predict = np.random.randint(first,last)
    while number != predict:
        count+=1
        if number > predict:
            first = predict
            predict = (first+last+1) // 2
            #print(number, ">", predict, first, last) #debug
        elif number < predict:
            last = predict
            predict = (first+last) // 2
            #print(number, "<", predict, first, last) #debug
    return(count) # выход из цикла, если угадали

#def score_game(game_core_v2):
def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

# запускаем
#score_game(game_core_v2)
score_game(game_core_v3)
