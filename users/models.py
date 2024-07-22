from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.


class User(auth_models.AbstractUser):
    """User model of all application users.
    Users profile can be customized here"""