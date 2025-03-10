
class HttpResponse:
    def __init__(self, status_code:int=200, reason_phrase:str="OK", headers:dict={}, body:str=""):
        self.status_code = status_code
        self.reason_phrase = reason_phrase
        self.headers = headers
        self.body = body

        # Returns the representation of the HTTP response:
        def __str__(self):
            response_line = f"HTTP/1.1 {self.status_code} {self.reason_phrase}\r\n"
            headers = "".join(f"{key}:{value}\r\n" for key, value in self.headers.items())
            blank_line = "\r\n"

            return (response_line + headers + blank_line + self.body)



class HttpResponseBuilder:
      def __init__(self):
          self._status_code = 200
          self._reason_phrase = "OK"
          self._headers = {}
          self._body = ""

      def set_status_code(self, status_code:int=200, reason_phrase:str="OK")->None:
          self._status_code = status_code
          self._reason_phrase = reason_phrase


      def add_header(self, key, value):
        """Adds an HTTP header."""

        self._headers[key] = value
        return self


      def set_body(self, body):
        """ Defines the answer body."""
        self._body = body
        return self


      def build(self):
        """ Constructs and returns an instance of HttpResponse. """
        return HttpResponse(
            status_code=self._status_code,
            reason_phrase=self._reason_phrase,
            headers=self._headers,
            body=self._body
        )



def main()->None:
    builder = HttpResponseBuilder()
           
    response = {
        builder
        .set_status(200, "OK")
        .add_header("Content-Type", "text/plain")
        .add_header("X-Custom-Header", "CustomValue")
        .set_body("Hello, this is a custom response!")
        .build()
    }

    str(response)


if __name__=="__main__":
   main() 
