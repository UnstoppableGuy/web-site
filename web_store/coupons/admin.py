from django.contrib import admin
from .models import Coupon


'''class CouponInline(admin.TabularInline): # ЗАчем использовать эти штуки если можно просто купон зарегать.
    model = Coupon
    fields = ['code', 'valid_form', 'valid_to', 'discount', 'active']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    #list_filter = ['active', 'valid_form', 'valid_to']
    #search_fields = ['code']
    inlines = [CouponInline]

admin.site.register(Coupon, CouponAdmin)'''

admin.site.register(Coupon)
