from django.db import models


class Categories(models.TextChoices):
    LIFESTYLE = 'lifestyle'
    CULTURE = 'culture'
    PROGRAMMING = 'programming'
    SURVEYING = 'surveying'