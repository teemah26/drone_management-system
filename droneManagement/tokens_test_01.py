from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user=User.objects.get(username='username')
Token= Token.objects.get(user=user)
token=Token.key
print(token)
print(f'The token for user {user.username} is: {token}')