from json import load
from os import path


with open(f"{path.dirname(__file__)}/errors.json") as errors_json:
    errors = load(errors_json)


class RPCError(Exception):
    name = "RPC"
    
    def __init__(self, code=None):
        self.code = code

    def __str__(self):
        error = self.get_error(self.code)
        text = f"code: {error['code']}\ntype: {error['type']}\ndescription: {error['en']}"
        return text
    
    @staticmethod
    def get_error(code):
        return errors.get(str(code))
        
