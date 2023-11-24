<p align="center">  
      <a href="https://github.com/abolX/Zarinpal">  
          <img src="https://i.ibb.co/Gdq68J3/cropped-Asset-1-10x.png" alt="Zarinpal" width="350">  
      </a>  
      <br> 
      <p3><b>online payment gateway for Python</b></p3>  
      </br> 
  </p> 
  
## [Zarinpal](https://www.zarinpal.com/)
> - **create and manage an online payment gateway using [Zarinpal](https://www.zarinpal.com/) for e-commerce websites.**

> - **It allows merchants to integrate secure online functionality into their web applications and enables customers to make payments using Accelerated Network member cards.**


 # Request Example
  
```python 
from zarinpal import Zarinpal, MetaData
from asyncio import run 
  
zarinpal = Zarinpal("MERCHANT_ID") 
  

async def main(): 
   result = await zarinpal.request(
       amount=10000,
       description="for payment",
       callback_url="https://your_domain.com",
       metadata=MetaData(mobile="98900000000")
   )
   print(result)
   print(result.payment_gateway_url)


if __name__ == "__main__":
    run(main())
```

### Output :
```json
{
    "code": 100,
    "message": "Success",
    "authority": "A00000000000000000000000000*********",
    "fee_type": "Merchant",
    "fee": 1500
}
https://www.zarinpal.com/pg/StartPay/A00000000000000000000000000*********
```

# Verify Example
```python
async def main(): 
     result = await zarinpal.verify(
         amount=10000,
         authority="A00000000000000000000000000*********"
     )
     print(result)
  
run(main())
```

### output, if money has been paid :

```json
{
    "code": 101,
    "message": "Verified",
    "authority": "A00000000000000000000000000*********",
    "fee_type": "Merchant",
    "fee": 1500,
    "amount": 10000,
    "ref_id": 10000000000,
    "card_pan": "000000******0000",
    "card_hash": "hash...",
    "mobile": "98900000000"
}
```

Thanks You ❤️‍🩹