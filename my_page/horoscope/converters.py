from datetime import datetime
class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

class MyFloatConverter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

class MyDateConverter:
    regex = '[0-9]{2}-[0-9]{2}-[0-9]{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')

class SplitConvertor:
    regex = r'(\w+,)+\w+'

    def to_python(self, value):
        return value.split(",")

    def to_url(self, value):
        return ",".join(value)

class UpperConvertor:
    regex = r'\w+'

    def to_python(self, value):
        return str(value.upper())

    def to_url(self, value):
        return str(value.lower())

