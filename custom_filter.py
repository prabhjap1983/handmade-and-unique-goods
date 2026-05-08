# custom_filters.py

from django import template

register = template.Library()

@register.filter
def convert_to_rupees(price_in_dollars, conversion_rate=74.5):
    # Convert price from dollars to rupees
    price_in_rupees = price_in_dollars * conversion_rate
    return round(price_in_rupees, 2)  # rounding to 2 decimal places
