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
            print(email, 'in EmailOrUsernameModelBackend')
            user = User.objects.get(**kwargs)
            print( user )
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None 
