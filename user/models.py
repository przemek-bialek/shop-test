from django.db import models
from star_ratings.models import AbstractBaseRating
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.width > 250:
            if image.height > 250:
                image.thumbnail((250, 250))
            else:
                image.thumbnail((250, image.height))
        else:
            if image.height > 250:
                image.thumbnail((image.height, 250))
        image.save(self.img.path)

class UserRating(AbstractBaseRating):
    comment = models.TextField(blank=True, null=True)
    rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rater')
    rated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rated')
