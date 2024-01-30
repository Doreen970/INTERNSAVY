from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def extract_image(content):
    soup = BeautifulSoup(content, 'html.parser')
    img_tag = soup.find('img')
    return str(img_tag) if img_tag else ''