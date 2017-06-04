#!python3
#encoding:utf-8
from authentication.Authentication import Authentication
from authentication.NonAuthentication import NonAuthentication
from authentication.BasicAuthentication import BasicAuthentication
from authentication.TwoFactorAuthentication import TwoFactorAuthentication
from authentication.OAuthAuthentication import OAuthAuthentication
from authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
class RequestParameter:
    def __init__(self, db, authentications):
        self.__db = db
        self.__authentications = []
        if isinstance(authentications, list):
            for a in authentications:
                if isinstance(a, Authentication):
                    self.__authentications.append(a)

    def Get(self, http_method, endpoint):
        api = self.__db.api['Apis'].find_one(HttpMethod=http_method.upper(), Endpoint=endpoint)
        if None is api:
            for a in self.__authentications:
                if isinstance(a, OAuthTokenFromDatabaseAndCreateApiAuthentication):
                    a.SetAccessToken()
                    return a.GetRequestParameters()
                elif isinstance(a, OAuthTokenFromDatabaseAuthentication):
                    a.SetAccessToken()
                    return a.GetRequestParameters()
                elif isinstance(a, OAuthAuthentication):
                    return a.GetRequestParameters()
                elif isinstance(a, TwoFactorAuthentication):
                    return a.GetRequestParameters()
                elif isinstance(a, BasicAuthentication):
                    return a.GetRequestParameters()
            return NonAuthentication().GetRequestParameters()
        grants = api['Grants'].split(",")
        if ("Token" in api['AuthMethods']):
            for a in self.__authentications:
                if isinstance(a, OAuthTokenFromDatabaseAndCreateApiAuthentication):
                    a.SetAccessToken(grants)
                    return a.GetRequestParameters()
                elif isinstance(a, OAuthTokenFromDatabaseAuthentication):
                    a.SetAccessToken(grants)
                    return a.GetRequestParameters()
                elif isinstance(a, OAuthAuthentication):
                    return a.GetRequestParameters()
        elif ("Basic" in api['AuthMethods']):
            for a in self.__authentications:
                if isinstance(a, TwoFactorAuthentication):
                    return a.GetRequestParameters()
                elif isinstance(a, BasicAuthentication):
                    return a.GetRequestParameters()
        elif ("ClientId" in api['AuthMethods']):
            raise Exception('Not implemented clientId authorization.')
        else:
            raise Exception('Not found AuthMethods: {0} {1}'.format(api['HttpMethod'], api['Endpoint']))
