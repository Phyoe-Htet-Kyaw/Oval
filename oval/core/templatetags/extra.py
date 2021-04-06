from django import template
import base64

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
