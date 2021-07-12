from django import template
import base64
from django.db import connections

register = template.Library()


@register.filter
def encrypt_email(email):
    encoded_bytes = base64.b64encode(email.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str


@register.filter
def encrypt_id(id):
    str_id = str(id)
    encoded_bytes = base64.b64encode(str_id.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str


@register.filter
def get_country(country_id):
    if country_id:
        cursor = connections['default'].cursor()
        cursor.execute("SELECT * FROM core_country WHERE id= %s", [country_id])
        country = cursor.fetchone()
        return country[1]


@register.filter
def get_city(city_id):
    if city_id:
        cursor = connections['default'].cursor()
        cursor.execute("SELECT * FROM core_city WHERE id= %s", [city_id])
        city = cursor.fetchone()
        return city[1]


@register.filter
def byte_mood(b):
    return b.decode("UTF-8")


@register.filter
def check_none(variable):
    if variable:
        return variable
    else:
        return ""


