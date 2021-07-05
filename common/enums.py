from django.db import models


class Alignment(models.TextChoices):
    LEFT = "left", "Left"
    RIGHT = "right", "Right"
    CENTER = "center", "Center"
    JUSTIFY = "justify", "Justify"


class Aspect(models.TextChoices):
    ORIGINAL = "original", "Original"
    SQUARE = "square", "Square"
    PORTRAIT = "portrait", "Portrait"
    LANDSCAPE = "landscape", "Landscape"


class Size(models.TextChoices):
    SMALL = "small", "Small"
    MEDIUM = "medium", "Medium"
    LARGE = "large", "Large"
