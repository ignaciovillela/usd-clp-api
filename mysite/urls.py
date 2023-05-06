from django.urls import path, register_converter

from app.views import conversor
from mysite.converters import DecimalConverter

register_converter(DecimalConverter, 'decimal')

urlpatterns = [
    path('', conversor),
    path('<decimal:amount>', conversor),
    path('<decimal:amount>/<str:from_currency>/<str:to_currency>', conversor),
]
