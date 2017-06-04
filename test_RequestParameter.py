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
class test_RequestParameter(unittest.TestCase):
    def test_NonAuthentication(self):
        db = Database()
        db.Initialize()
        authentications = [NonAuthentication()]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        
    def test_BasicAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'user'
        password = 'pass'
        authentications = [BasicAuthentication(username, password)]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertTrue('auth' in params)
        self.assertEqual(params['auth'], (username, password))

    def test_TwoFactorAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'user'
        password = 'pass'
        two_factor_secret = 'base32secret3232'
        auth = TwoFactorAuthentication(username, password, two_factor_secret)
        authentications = [auth]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('X-GitHub-OTP' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEqual(params['headers']['X-GitHub-OTP'], auth.OneTimePassword)
        self.assertTrue('auth' in params)
        self.assertEqual(params['auth'], (username, password))

    def test_OAuthAuthentication(self):
        db = Database()
        db.Initialize()
        token = 'token1'
        authentications = [OAuthAuthentication(token)]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEqual(params['headers']['Authorization'], 'token ' + token)

    def test_OAuthTokenFromDatabaseAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'user0'
        authentications = [OAuthTokenFromDatabaseAuthentication(db, username)]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertIn(params['headers']['Authorization'].replace('token ', ''), ['token0', 'token1'])
        
    def test_OAuthTokenFromDatabaseAndCreateApiAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'user1'
        password = 'pass1'
        two_factor_secret = 'base32secret3232'
        authentications = [OAuthTokenFromDatabaseAndCreateApiAuthentication(db, username, password, two_factor_secret)]
        reqp = RequestParameter(db, authentications)
        http_method = 'GET'
        endpoint = 'test'
        params = reqp.Get(http_method, endpoint)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEqual(params['headers']['Authorization'], 'token ' + 'token2')

