from typing import Union

from ..objects import Data
import zarinpal


class Verify:
    
    async def verify(
            self: "zarinpal.Zarinpal",
            amount: Union[int, str],
            authority: str
    ) -> "object.Data":
        
        json = locals() 
        del json["self"]
        json["merchant_id"] = self.merchant_id
        result = await self.connection.execute("verify", json)
        return Data(**json, **result)
