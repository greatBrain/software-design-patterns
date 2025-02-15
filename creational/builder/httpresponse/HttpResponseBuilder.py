""" Representes the final product """

class HttpResponse:

    def __init__(self, status_code:int=200, reason_phrase:str="OK", headers:dict=None, body:str=""):
          self.status_code=status_code
          self.reason_phrase = reason_phrase
          self.headers = headers or {}
          self.body=body
          self.method:str=''


    ''' representation of the HTTP response '''
    def __str__(self):
        response_str = "HTTP/1.1 {} {}\r\n".format(self.status_code, self.reason_phrase)    
        headers = "".join(f"{key}: {value}\r\n" for key, value in self.headers.items())
        blank_line = "\r\n"
        return response_str + headers + blank_line + self.body


""" Responsible of creating the HTTP response """
class HttpResponseBuilder:
      def __init__(self):
        # Default values
        self._status_code = 200
        self._reason_phrase = "OK"
        self._headers = {}
        self._body = ""

    
      def set_status(self, status_code, reason_phrase):
        """ Configures the satus code and its phrase. """
        self._status_code = status_code
        self._reason_phrase = reason_phrase
        return self  # Returns self to allow chaining






response = HttpResponse(
     status_code = 200,
     reason_phrase = "OK",
     headers={"Content-Type": "text/plain"},
     body="Hello, World!"
)

print(str(response))
