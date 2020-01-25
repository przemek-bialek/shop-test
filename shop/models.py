from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.base import ContentFile
from djmoney.models.fields import MoneyField
from PIL import Image
from io import BytesIO

import os


class Product(models.Model):
    name = models.CharField(max_length=60, unique=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = MoneyField(decimal_places=2, default=0, default_currency='PLN', max_digits=7)
    img = models.ImageField(default='no_pic.jpg', upload_to='product_pics')
    thumb = models.ImageField(default='no_pic.jpg', upload_to='product_pics/thumbnails')
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if not self.create_thumbnail():
            raise Exception('Given file is not an image')

        super().save(*args, **kwargs)

    def create_thumbnail(self):
        image = Image.open(self.img)
        if image.width > 250:
            if image.height > 250:
                image.thumbnail((250, 250))
            else:
                image.thumbnail((250, image.height))
        else:
            if image.height > 250:
                image.thumbnail((image.height, 250))

        image_name, image_extension = os.path.splitext(self.img.name)
        image_extension = image_extension.lower()

        if image_extension in ['.jpeg', '.jpg']:
            FTYPE = 'JPEG'
        elif image_extension == '.png':
            FTYPE = 'PNG'
        elif image_extension == '.gif':
            FTYPE = 'GIF'
        else:
            return False

        thumb_fname = image_name + '_thumb' + image_extension

        tmp = BytesIO()
        image.save(tmp, FTYPE)
        tmp.seek(0)

        self.thumb.save(thumb_fname, ContentFile(tmp.read()), save=False)

        return True
