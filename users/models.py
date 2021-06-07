from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True, primary_key=True, name='username',
        help_text='Required. 128 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid'),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        })

    def __str__(self):
        return self.username