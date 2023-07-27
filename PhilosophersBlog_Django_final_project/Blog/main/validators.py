from django.core.exceptions import ValidationError
from PIL import Image


def validate_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('The name must contain only letters.')


def clean_avatar(avatar):
    if avatar:
        if avatar.size > 5 * 1024 * 1024:
            raise ValidationError("The image size should not exceed 5 MB.")
        image = Image.open(avatar)
        img_width, img_height = image.size
        if img_width > 1920 or img_height > 1080:
            raise ValidationError("The image dimensions should not exceed 1920x1080.")

