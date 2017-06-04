#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
class Authentication(metaclass=ABCMeta):
    """
    requestsライブラリのAPIで使うheadersを生成する。
    """
    @abstractmethod
    def GetHeaders(self):
        return  {
            'Time-Zone': 'Asia/Tokyo',
            'Accept': 'application/vnd.github.v3+json',
        }

    """
    requestsライブラリのAPIで使う**kwargsを生成する。
    requests.get(url, **(this.GetRequestParameters()))
    """
    @abstractmethod
    def GetRequestParameters(self):
        return {
            'headers': self.GetHeaders()
        }
