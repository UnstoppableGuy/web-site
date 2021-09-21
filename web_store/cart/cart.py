from decimal import Decimal
from django.conf import settings
from first_app.models import Product
from coupons.models import Coupon # Пытаемся применить введенный купон ко всей корзине.


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # Сохранение текущего купона в корзине.
        self.coupon_id = self.session.get('coupon_id')
    
    def add(self, product, quantity=1, update_quantity=False): # pragma: no cover
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id) 
        if product_id not in self.cart: 
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self): # pragma: no cover
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product): # pragma: no cover
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self): # pragma: no cover
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product # ЗАЧЕМ ТУТ ЭТО ????

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине. 
        Возвращает кол-во всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self): # pragma: no cover
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    '''
    Общаемся с купоном через свойство потому что у нас может и не быть купона.
    Поэтому присваивать переменной значение было бы некорректно.
    '''
    @property
    def coupon(self): # pragma: no cover
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    '''
    Возвращает скидку в долларах.
    '''
    def get_discount(self): # pragma: no cover
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
