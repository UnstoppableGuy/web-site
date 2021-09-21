import numpy as np
#from pearsons_correlation import *
from recommendations.recommendations_logic.pearsons_correlation import *

DEBUG = True

class Independet_CMM_Element(object):
    def __init__(self, similarity, i, j):
        self.similarity = similarity
        self.i = i
        self.j = j        

# Ratings matrix element.
class Independet_RM_Element(object):
    def __init__(self, rating, i_user, j_product):
        self.rating = rating
        self.i_user = i_user
        self.j_product = j_product

# Prediction rating for i user and j product.
class Independent_Prediction_Element(object):
    def __init__(self, prediction, i_user, j_product):
        self.prediction = prediction
        self.i_user = i_user
        self.j_product = j_product 

'''
 - 'data'           - 2-d matrix.                       (strings - users ; rows - items ; statistics items inside)
 - 'user_position'  - number of string with required user
 - 'k'              - make predictions using first 'k' amount of similar users for our user. 
 RETURNS: sorted list of 'Independent_Prediction_Element' with highest prediction value in the begin.
'''
def get_recommendations(data, user_position=0, k=3): 
    if DEBUG:
        pinfo(data, text='data')
    # 0) Считаем pearsons correlation
    centered_cosine_matrix = pearsons_correlation(data)    
    if DEBUG:
        pinfo(centered_cosine_matrix, text='centered_cosine_matrix')

    # 1) Берём первых k-похожих пользователей на данного.
    first_k_similars_users = get_first_k_similars(centered_cosine_matrix, user_position, k)    
    if DEBUG:
        i=0
        for el in first_k_similars_users:
            print(f'El [{i}] = (val={el.similarity}, i={el.i}, j={el.j})')
            i += 1

    # 2) Проходимся по каждому продукту и делаем предсказание для текущего пользователя если это возможно.
    #     *Это не возможно в случае если никто из похожих пользователей ни взаимодействовал с этим товаром.
    # ВАЖНО: данный метод будет возвращать список не просто продуктов, а список обьектов которые будут
                        # хранить изначальный индекс в изначальной матрице и соответственно значения предсказанных кликов.

    predictions = []
    # для каждого продукта ,с которым наш юзер не взаимодействовал, делаем предсказание.
    for j in range(len(data[0])):
        if user_is_interacted(data, user_position, product_j=j):
            continue
        # выделяем список пользователей кто хоть раз юзал продукт.
        clear_similar_users = get_users_that_interacted_with_product(data, first_k_similars_users, product_j=j)     
        if len(clear_similar_users) == 0:
            continue
        prediction_for_product = get_prediction_for_product(data, clear_similar_users, product_j=j)
        if DEBUG:
            print(f'$ Product j={j}, prediction={prediction_for_product.prediction}')
        predictions.append(prediction_for_product)

    # Рекомендации могут содержать товары с предсказанным нулём !
    # Это нормально, но если необходимо то можно просто удалить все нулевые значения из 'recommendations'.
    recommendations = sorted(predictions, key=lambda x: x.prediction, reverse=True)

    return recommendations

'''
 - returns the list of Independent_CMM_Elements (which represents the similarity between 'i' and 'j' users).
'''
def get_first_k_similars(centered_cosine_matrix, user_position, k):
    ccm = np.copy(centered_cosine_matrix)
    # 0) Преобразуем матрицу в структуру данных другую.
    new_ccm = []
    for i in range(len(ccm)):
        new_line = []
        for j in range(len(ccm[i])):
            new_element = Independet_CMM_Element(similarity=ccm[i][j], i=i, j=j)
            new_line.append(new_element)
        new_ccm.append(new_line)    

    # 1) Выделяем значения из строки, сортируем, берём первые.
    most_similar_to_user = []    
    amoun_of_users = len(centered_cosine_matrix[0])
    i = user_position
    for j in range(len(new_ccm)):
        if (not np.isnan(new_ccm[i][j].similarity)) and (i != j):
            most_similar_to_user.append(new_ccm[i][j])

    sorted_users = sorted(most_similar_to_user, key=lambda x: x.similarity, reverse=True)
    result = []
    new_k = k if (len(sorted_users) >= k) else len(sorted_users)

    # Берём первых (или последних) k пользователей в зависимости от того как сортирует та ф-ия.    
    for i in range(new_k):
        result.append(sorted_users[i])

    return result

'''
 GET: similar_users - list of 'Independet_CMM_Element' elements.
 RETURN: similar_users but without them who doesn't iterate with product.
'''
def get_users_that_interacted_with_product(data, similar_users, product_j):
    new_users = []
    for el in similar_users:
        if user_is_interacted(data, el.j, product_j):
            new_users.append(el)
    return new_users

def user_is_interacted(data, user_index, product_j):        
    return True if (data[user_index][product_j] > 0) else False


'''
    Возвращает обькт предсказания 'Independent_Prediction_object'.
    среди похожих пользователей которые юзли продукт.
'''
def get_prediction_for_product(data, similar_users, product_j):
    prediction = 0
    numerator = 0
    denominator = 0
    similarity_was_only_zero = True
    
    for cmm_el in similar_users:
        numerator += (cmm_el.similarity * data[cmm_el.j][product_j])
        denominator += (cmm_el.similarity)
        if cmm_el.similarity != 0:
            similarity_was_only_zero = False
    if  (similarity_was_only_zero) and (denominator==0):
        denominator = 1
    elif (denominator==0):
        denominator = 1
    try:
        prediction = numerator / denominator    
    except:
        raise Exception(f'Could not get prediction for product_j = {product_j}')        

    full_prediction = Independent_Prediction_Element(prediction, similar_users[0].i, product_j)

    return full_prediction