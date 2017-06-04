#!python3
#encoding:utf-8
import unittest
from Database import Database
from RequestParameter import RequestParameter
from authentication.Authentication import Authentication
from authentication.NonAuthentication import NonAuthentication
from authentication.BasicAuthentication import BasicAuthentication
from authentication.TwoFactorAuthentication import TwoFactorAuthentication
from authentication.OAuthAuthentication import OAuthAuthentication
from authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
from AuthenticationsCreator import AuthenticationsCreator
class test_AuthenticationsCreator(unittest.TestCase):
    def test_OAuthBasic(self):
        db = Database()
        db.Initialize()
        creator = AuthenticationsCreator(db, 'user0')
        authentications = creator.Create()
        self.assertEquals(len(authentications), 2)
        self.assertTrue(isinstance(authentications[0], OAuthAuthentication))
        self.assertTrue(isinstance(authentications[1], BasicAuthentication))
        print(authentications[0].AccessToken)
    def test_OAuthTwoFactor(self):
        db = Database()
        db.Initialize()
        creator = AuthenticationsCreator(db, 'user1')
        authentications = creator.Create()
        self.assertEquals(len(authentications), 2)
        self.assertTrue(isinstance(authentications[0], OAuthAuthentication))
        self.assertTrue(isinstance(authentications[1], TwoFactorAuthentication))
    def test_OAuthSelectToken0(self):
        db = Database()
        db.Initialize()
        creator = AuthenticationsCreator(db, 'user0')
        authentications = creator.Create(scopes=['repo'])
        self.assertEquals(len(authentications), 2)
        self.assertTrue(isinstance(authentications[0], OAuthAuthentication))
        self.assertEquals(authentications[0].AccessToken, 'token0')
        self.assertTrue(isinstance(authentications[1], BasicAuthentication))
        print(authentications[0].AccessToken)
    def test_OAuthSelectToken1(self):
        db = Database()
        db.Initialize()
        creator = AuthenticationsCreator(db, 'user0')
        authentications = creator.Create(scopes=['gist'])
        self.assertEquals(len(authentications), 2)
        self.assertTrue(isinstance(authentications[0], OAuthAuthentication))
        self.assertEquals(authentications[0].AccessToken, 'token1')
        self.assertTrue(isinstance(authentications[1], BasicAuthentication))
        print(authentications[0].AccessToken)
