from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Coupon
from .forms import CouponApplyForm

import logging

logger = logging.getLogger(__name__)

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid(): # pragma: no cover
        coupon_code = form.cleaned_data['code']
        # Ищем существует ли купон с таким кодом, активен ли он, проверяем дату чтоб было в промежутке действия купона.
        try:
            coupon = Coupon.objects.get(code__iexact=coupon_code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            # Сохраняем в сессию идентификатор купона для далнейшего сохранения его в заказе.
            request.session['coupon_id'] = coupon.id
            logger.info(f'user: {request.user.username}, use coupon: {coupon_id}.')
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None        
    return redirect('cart:cart_detail')