from .object import Object
from typing import Union


class Error(Object):
    
    def __init__(
            self,
            code: Union[int, str] = None,
            message: str = None,
            validations: list = None,
            **_
    ):
        self.code = code
        self.message = message
        self.validations = validations
 