# import aiohttp
# import asyncio
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url='https://api.github.com/events',proxy='https://103.103.3.6:8080') as resp:
#             print(resp.status)
#             print(await resp.text())
#
# asyncio.run(main())

import requests
url = 'https://www.baidu.com'
resp = requests.get(url=url, proxies={'https': 'http://177.229.194.30:999'})
print(resp.text)