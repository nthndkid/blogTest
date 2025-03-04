# # backends.py
# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
# from .models import UserAuth  # Import your custom user model
# from django.utils import timezone

# class UserAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # Fetch the user from your custom model
#             user = UserAuth.objects.get(username=username)
#             # Check if the provided password matches the stored password
#             if check_password(password, user.password):  # Make sure passwords are hashed
#                 # Create or update a Django User instance for session management
#                 django_user, created = User.objects.get_or_create(username=user.username)
#                 django_user.email = user.email
#                 django_user.first_name = user.first_name
#                 django_user.last_name = user.last_name
#                 django_user.last_login = timezone.now()  # Set last_login on authentication
#                 django_user.save()
#                 return django_user
#         except UserAuth.DoesNotExist:
#             return None  # User not found

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)  # Get the Django user by ID
#         except User.DoesNotExist:
#             return None  # User not found




