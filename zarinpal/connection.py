from aiohttp import ClientSession
from typing import Union

from .errors import RPCError


class Connection:
    
    def __init__(self, time_out: int):
        #self.sub_domain = "sandbox" if sand_box else "api"
        self.time_out = time_out

    @property
    def url(self):
        return "https://api.zarinpal.com/pg/v4/payment"
        
    async def execute(self, method: Union["request", "verify"], json):
        json = {key: value for key, value in json.items()
                    if value is not None}
                    
                    
        async with ClientSession() as client:
            async with client.post(
                url=f"{self.url}/{method}.json",
                json=json,
                timeout=self.time_out
            ) as response:
           
                response_json = await response.json()
                if response_json["errors"]:
                    raise RPCError(response_json["errors"]["code"])
                return response_json["data"]
                
