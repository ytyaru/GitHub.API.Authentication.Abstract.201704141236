#!python3
#encoding:utf-8
from Database import Database
from authentication.Authentication import Authentication
from authentication.NonAuthentication import NonAuthentication
from authentication.BasicAuthentication import BasicAuthentication
from authentication.TwoFactorAuthentication import TwoFactorAuthentication
from authentication.OAuthAuthentication import OAuthAuthentication
from authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
class AuthenticationsCreator(object):
    def __init__(self, db, username):
        self.__db = db
        self.__username = username

    def Create(self, username=None, scopes=None):
        if None is username:
            username = self.__username
        authentications = []
        account = self.__db.account['Accounts'].find_one(Username=username)
        if None is account:
            raise Exception('指定したユーザ {0} はDBに未登録です。登録してから実行してください。'.format(username))
        token = self.__GetAccessToken(scopes)
        if None is not token:
            authentications.append(OAuthAuthentication(token))
        two_factor = self.__db.account['TwoFactors'].find_one(AccountId=account['Id'])
        if None is not two_factor:
            authentications.append(TwoFactorAuthentication(account['Username'], account['Password'], two_factor['Secret']))
        else:
            authentications.append(BasicAuthentication(account['Username'], account['Password']))
        return authentications

    def __GetAccessToken(self, scopes=None):
        sql = "SELECT * FROM AccessTokens WHERE AccountId == {0}".format(self.__db.account['Accounts'].find_one(Username=self.__username)['Id'])
        if not(None is scopes) and isinstance(scopes, list) and 0 < len(scopes):
            sql = sql + " AND ("
            for s in scopes:
                sql = sql + "(',' || Scopes || ',') LIKE '%,{0},%'".format(s) + " OR "
            sql = sql.rstrip(" OR ")
            sql = sql + ')'
#        print(scopes)
#        print(sql)
        res = self.__db.account.query(sql)
        ret = None
        for r in res:
#            print(r)
            ret = r
        return ret['AccessToken']
#        return self.__db.account.query(sql).next()['AccessToken']

