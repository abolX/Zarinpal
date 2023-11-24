from .object import Object

class MetaData(Object):
    
    def __init__(
            self,
            mobile: str = None,
            email: str = None,
            order_id: str = None,
            **_
    ):
        self.mobile = mobile
        self.email = email
        self.order_id = order_id
