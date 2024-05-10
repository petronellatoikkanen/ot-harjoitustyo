import unittest
from services.login_service import LoginService
from services.user_service import UserService
from repositories.user_repository import UserRepository

from entities.user import User

class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.user = User('testi', 'testi123')
        self.username = 'testi'
        self.password = 'testi123'