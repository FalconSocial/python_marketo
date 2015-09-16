
class MarketoException(Exception):
    message = None
    code = None
    data = None

    def __init__(self, exc={'message': None, 'code': None}):

        if exc['errors']:
            self.data = exc
            exc = exc['errors'][0]

        self.message = exc['message']
        self.code = exc['code']
      
    def __str__(self):
        return self.message, "\nCode: ", self.code, "\nJSON:\n", self.data
