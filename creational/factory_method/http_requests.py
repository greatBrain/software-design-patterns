import http.client
from abc import ABC, abstractmethod

class HttpRequest(ABC):
      @abstractmethod
      def request(self, id:int)->str:  
          ...

class HttpGet(HttpRequest):
      def __init__(self, domain:str, path:str)->None:
          self.__domain = domain
          self.__path = path

      def request(self, id:int)->str:
          conn = http.client.HTTPSConnection(self.__domain)
          conn.request("GET", "/{}/{}".format(self.__path, id))
          response = conn.getresponse()

          if response.status==200:
             data=  response.read()
             return data.decode("utf-8")

          else: print("Error en la solicitud. {}".format(data.status))
          conn.close()
