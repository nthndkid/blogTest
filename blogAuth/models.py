from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils import timezone


class UserAuth(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'  # Define which field will act as the unique identifier
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # Any additional fields required for creation

    class Meta:
        managed = False
        db_table = 'user_auth'

# class UserAuthManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not username:
#             raise ValueError("The Username field is required")
#         if not email:
#             raise ValueError("The Email field is required")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)  # This will hash the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, email, password, **extra_fields)

# class UserAuth(AbstractBaseUser):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     last_login = models.DateTimeField(null=True, blank=True)  # Add last_login field
#     is_active = models.BooleanField(default=True)  # Add is_active field
#     is_staff = models.BooleanField(default=False)  # Add is_staff field

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

#     objects = UserAuthManager()  # Set the custom manager

#     class Meta:
#         db_table = 'user_auth'

