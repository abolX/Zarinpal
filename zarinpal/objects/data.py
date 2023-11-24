from .object import Object


class Data(Object):
    
    def __init__(
            self,
            code: int = None,
            message: str = None,
            fee_type: str = None,
            fee: str = None,
            amount: int = None,
            authority: str = None,
            ref_id: str = None,
            card_pan: str = None,
            card_hash: str = None,
            mobile: str = None,
            email: str = None,
            order_id: str = None,
            **_
    ):
        self.code = code
        self.message = message
        self.authority = authority
        self.fee_type = fee_type
        self.fee = fee
        self.amount = amount
        self.ref_id = ref_id
        self.card_pan = card_pan
        self.card_hash = card_hash
        self.mobile = mobile
        self.email = email
        self.order_id = order_id

    @property
    def payment_gateway_url(self):
        return f"https://www.zarinpal.com/pg/StartPay/{self.authority}"
 