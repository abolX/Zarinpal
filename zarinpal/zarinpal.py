from .connection import Connection
from .methods import Methods
from .errors import RPCError


class Zarinpal(Methods):
    
    def __init__(
            self,
            merchant_id: str,
            time_out: int = 20
            #sand_box_mode: bool = False,    
    ):
        self.merchant_id = merchant_id
        self.connection = Connection(time_out)
    
    @staticmethod
    def create_payment_gateway_url(authority):
        return f"https://www.zarinpal.com/pg/StartPay/{authority}"

    @staticmethod
    def get_error(code):
        return RPCError.get_error(code)
    