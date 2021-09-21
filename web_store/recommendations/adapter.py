from django.contrib.auth.models import User
from first_app.models import Product
from recommendations.models import StatisticsItem
import numpy as np

''' Вспомогательный класс для вывода инфы из матрицы в django-модель'''
class product_with_prediction(object): # pragma: no cover
    def __init__(self, prediction_obj, product):
        self.pred_obj = prediction_obj
        self.product = product

''' Adapter class for for correct converting data form django DB to recommendations app and back '''
class Recomendations_Django_Adapter(object): # pragma: no cover

    def __init__(self):
        self.DEBUG = False  
        
    def from_users_products_statistics_to_matrix(self, users, current_user, products, current_user_index):
        """Returns 2d matrix (numpy array) and changes current_user_index"""
        data = []
        if self.DEBUG:
            print('USERS:')
        # Collect and convert data from DB into required format for "get_recommendations" method.
        current_user_index = -1
        for i in range(len(users)):
            new_line = []
            # вычисляем индекс текущего пользователя.
            if users[i] == current_user:
                current_user_index = i
            for j in range(len(products)):
                new_element = StatisticsItem.objects.get(user=users[i], product=products[j])
                new_line.append(new_element.clicks)
            if self.DEBUG:
                print(f'users[{i}] = (name: {users[i].username}); (id: {users[i].id})')
            data.append(new_line)
        data_new = np.copy(data)

        if self.DEBUG:
            print('PRODUCTS:')  
            for i in range(len(products)):
                print(f'products[{i}] = (name: {products[i].title}); (id: {products[i].id})')
            print(f'CURRENT_USER_INDEX: {current_user_index}')

        return data_new

    def from_predictions_to_django(self, product_recommendations, products):
        '''FROM : sorted list of 'Independent_Prediction_Element' with highest prediction value in the begin'''
        '''TO   : list of product_with_prediction.'''  
        # Gettin related products.
        products_recommended = []
        for i in range(len(product_recommendations)):
            index = product_recommendations[i].j_product
            current_product = products[index]
            test_object = product_with_prediction(product_recommendations[i], current_product)
            products_recommended.append(test_object)
        
        return products_recommended
    