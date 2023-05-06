from decimal import Decimal
from django.urls.converters import StringConverter


class DecimalConverter(StringConverter):
    regex = r'[0-9]+(\.[0-9]+)?'

    def to_python(self, value):
        return Decimal(value)

    def to_url(self, value):
        return str(value)
