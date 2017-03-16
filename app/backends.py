#from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class EmailOrUsernameModelBackend(object):
    """ Authenticated user by username or email """
    def authenticate( self, email=None, password=None):
        #if '@' in email:
        kwargs = {'email': email}
        #else:
        #    kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None 
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
