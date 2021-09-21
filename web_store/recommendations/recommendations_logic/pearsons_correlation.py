import numpy as np
DEBUG = True


'''
2) Calculate centered cosine similarity (Pearson correlation)
    - gets 2-d matrix of ratings.
    - actions : 1) normalized matrix;
                2) calculates cosines simularities;
    - returns 2-d matrix of centered cosine simularities.
'''
def pearsons_correlation(data): # pragma: no cover
    sdata = np.copy(data) 
    normalized = normalize_ratings_matrix(sdata)

    #### <-------------- Тут после нормализации матрицы проверять на то есть ли пользователи с нулевыми полями и если есть то удалить их
    #### ! В конечном счёте это все равно никак не повлияет на похожесть пользователей, т.к. такие пользователи заведомо просто новые пользователи или 
    # пользователи у которых одинаковые оценки (в этом случае мы теряем потенциально хорошие рекомендации!!!!!!)
    
    # Solution 1: <- ЭТО НЕ ПОДХОДЯЩЕЕ РЕШЕНИЕ ТК НЕЛЬЗЯ НАРУШАТЬ ИНДЕКСЫ И РАЗМЕРЫ ИСХОДНОЙ МАТРИЦЫ.
        #correct_normalized = remove_null_vectors(normalized)
    
    # Solution 2:
    correct_normalized = normalized
        # normalized - contains zeros.
        # but also my_cosine - contains nan values.
    
    result = my_full_cos_sim(correct_normalized)    
    return result


'''
1) Normalize ratings matrix:
    - gets 2-d matrix where each string is user rating for items.
    - for each string : находим среднее значение в строке (Mx) и заменяем каждое значение(x) как (x - Mx).
    - returns normalized 2-d matrix.
'''
def normalize_ratings_matrix(data): # pragma: no cover
    data = np.copy(data)
    res = []
    for i in range(len(data)):
        new_line = []
        average_line = get_average(data[i])
        for j in range(len(data[i])):
            old_value = data[i][j]
            if old_value != 0:
                new_val = old_value - average_line                
            else:
                new_val = old_value
            new_line.append(new_val)
        res.append(new_line)

    res_cor = np.copy(res)
    return res_cor 

'''
- Gets 2-d matrix of user ratings
- returns cosine simularity 2-d matrix between users.
- WARNIN !!!
- IT COULD HAS nan VALUES CUZ IAM NOT SURE HOW TO REPRESENT IT.
'''
def my_full_cos_sim(data): # pragma: no cover
    res = []
    for i in range(len(data)):
        new_line = []
        for j in range(len(data)):
            #new_num = my_cosine_sim(data[i], data[j])
            new_num = my_cosine_sim_test(data[i], data[j])
            new_line.append(new_num)
        res.append(new_line)
    res_correct = np.copy(res)
    return res_correct

'''
 The same as np.dot(x,y) method.
'''
def sum_multi(x, y): # pragma: no cover
    up_value = 0
    for i in range(len(x)):
        up_value += x[i] * y[i]
    return up_value

# returns average val from non null values in vector.
def get_average(x): # pragma: no cover
    amount = 0
    sum = 0
    for i in range(len(x)):
        if x[i] != 0:
            amount += 1
            sum += x[i]
    if amount != 0:
        return sum / amount
    else:
        return 0

'''
 1. Как с точки зрения линейной алгебры понимать тот факт что я не могу найти 
    косинусное расстояние между векторами если хотя бы один из них нулевой ?
 2. Заметка: с точки зрения логики нулевой вектор после нормализации матрицы может 
    получится в 2-ух случаях:
        а) Пользователь никак не оценил фильмы/продукты;
        б) Пользователь оценил некоторые фильмы/продукты одинаково а другие не оценил; (в этом кейсе как мне кажется теряется что-то важное)
 3. Решение: Расчитывать матрицу косинусов только после проверки матрицы на пользователей с полностью нулевыми полями оценок.
 4. Решение 2: Для нулевых матриц возвращать nan. 
'''
def my_cosine_sim_test(x, y): # pragma: no cover
    up_value = 0
    down_value = 1
    up_value = sum_multi(x, y)    
    down_value = np.sqrt(sum_multi(x, x)) * np.sqrt(sum_multi(y, y))    
    if down_value == 0:
        return np.nan
        #raise Exception('Check for vectors ')
    return up_value / down_value

'''
Calculates cosine simularity
(Angle between vectors x and y.)
'''
def my_cosine_sim(x, y): # pragma: no cover
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

# DEFAULT STUFF ---------------------------------------------------------------------------------------------------------------------------------

def pinfo(x, up=True, down=True, text='debug info:'): # pragma: no cover  
    if up:
        print(f'-----------------text:{text}-------------------------------|')
    print(x)
    print(type(x))
    if down:
        print('------------------------------------------------|')

'''
 - data should contain at least 1 element;
 - matrix should be square;
 - returns 2-d matrix without zeros strings.
'''
def remove_null_vectors(data): # pragma: no cover
    zeros_vector = np.zeros(len(data[0]))
    result = np.array([string for string in data if not np.all(string==zeros_vector) ])
    return result


