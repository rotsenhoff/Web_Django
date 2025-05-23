from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        # Se crea un usuario para las pruebas
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        # Verifica que el perfil se haya creado correctamente
       exists = Profile.objects.filter(user__username='test').exists()
       self.assertEqual(exists, True)
    