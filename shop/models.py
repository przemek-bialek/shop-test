from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from io import BytesIO

import os


class Product(models.Model):
    name = models.CharField(max_length=60, unique=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_currency = models.CharField(max_length=10, default='zł')
    img = models.ImageField(default='no_pic.jpg', upload_to='product_pics')
    thumb = models.ImageField(default='no_pic.jpg', upload_to='product_pics/thumbnails')
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)
    product_type = models.CharField(max_length=6, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.create_thumbnail():
            raise Exception('Given file is not an image')

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop-product_detail', kwargs={'slug': self.slug})


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

class Whisky(Product):
    type = models.CharField(max_length=20, blank=True, null=True)
    strength = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    distillery = models.CharField(max_length=50, blank=True, null=True)
    bottler = models.CharField(max_length=50, blank=True, null=True)
    casktype = models.CharField(max_length=50, blank=True, null=True)
    casknumber = models.PositiveIntegerField(blank=True, null=True)
    vintage = models.PositiveSmallIntegerField(blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    bottled = models.DateField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    bottles_in_serie = models.PositiveIntegerField(blank=True, null=True)

    def get_fields(self):
        return [(field.name.replace('_', ' ').capitalize, field.value_to_string(self))
                for field in Whisky._meta.get_fields(include_parents=False) if field.name != 'product_ptr']

class Metal(Product):
    type = models.CharField(max_length=20, blank=True, null=True)
    alloy = models.CharField(max_length=15, blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    diameter = models.PositiveIntegerField(blank=True, null=True)
    denomination = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mintage_pcs = models.PositiveIntegerField(blank=True, null=True)
    edge = models.CharField(max_length=20, blank=True, null=True)
    quality = models.CharField(max_length=30, blank=True, null=True)
    producer = models.CharField(max_length=35, blank=True, null=True)

    def get_fields(self):
        return [(field.name.replace('_', ' ').capitalize, field.value_to_string(self))
                for field in Metal._meta.get_fields(include_parents=False) if field.name != 'product_ptr']
