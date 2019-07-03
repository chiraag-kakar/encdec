from django.urls import path
from .views import(
    home,
    encrypt,
    decrypt,
    encrypted,
    decrypted
)

urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
    path('encrypted/', encrypted, name='encrypted'),
    path('decrypted/', decrypted, name='decrypted'),   
]
