__version__ = 'dev'
from django.contrib.auth import get_user_model
try:
    from django_user import User
except:
    pass
#print User

