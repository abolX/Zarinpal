from typing import Union, Optional

import zarinpal
from ..objects import Data


class Request:
    
    async def request(
            self: "zarinpal.Zarinpal",
            amount: Union[int, str],
            description: str,
            callback_url: str,
            currency: Union["IRR", "IRT"] = None,
            metadata: Optional["object.MetaData"] = None
    ) -> "object.Data":
        
        if int(amount) < 1_000 or int(amount) > 1_000_000_000:
            raise ValueError(
                "the amount may not be greater than 1,000,000,000 "
                "and be at least 1,000"
            )
        json = locals()
        del json["self"]
        
        if isinstance(currency, str):
            currency = currency.upper()
            if currency not in ["IRR", "IRT"]:
                raise KeyError("currency must be IRR or IRT")
            json["currency"] = currency
            
        if len(description) >= 500:
            raise ValueError(
                "the description must be less than 500 characters"
            )
        if metadata:
            json["metadata"] = metadata.to_dict()
        
        json["merchant_id"] = self.merchant_id
        result = await self.connection.execute("request", json)
        return Data(**result)
 