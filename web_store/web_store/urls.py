"""web_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from first_app import views as main_views

# for static stuff. in debug mode.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('products/', main_views.get_products_page, name="products_url"),    
    path('products/<slug:slug>/', main_views.get_specific_product, name='specific_product_url_with_slug'),
    path('categories/', main_views.get_categories, name="categories_url"),    
    re_path(r'^recommendations/', include(('recommendations.urls', 'recommendations'), namespace='recommendations')),
 
    # User stuff.
    path('activate/<uidb64>/<token>/', main_views.VerificationView.as_view(), name='activate'), # Вызывается метод __get__() который мы переопределили.
    path('register/', main_views.get_register_page, name="register_url"),
    path('login/', main_views.loginPage, name="login_url"),    
    path('logout/', main_views.logout_user, name="logout_url"),
    path('user-profile/', main_views.get_user_profile_page, name="user_profile_url"),

    # Test zone.    
    path('set-balance/', main_views.set_balance, name='set_balance'),   

    # Actions with buy products.
    path('buy-product/<slug:slug>/', main_views.buy_product, name='buy_product_url_with_slug'),
    re_path(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    re_path(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    re_path(r'^coupons/', include(('coupons.urls', 'coupons'), namespace='coupons')),

    # Base stuff.
    path('admin/', admin.site.urls),
    path('about_us/', main_views.get_about_us, name="about_us_url"),    
    path('', main_views.get_categories, name="home_url"),       

    # API.
    re_path(r'^api/', include(('orders.api.urls', 'orders_api'), namespace='orders_api')),
]

# В режиме дебаг потому что на продакшене так не делают.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # pragma: no cover