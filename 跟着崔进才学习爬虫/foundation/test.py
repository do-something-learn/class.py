import asyncio

import aiohttp
async def scrapy_method():
    session = aiohttp.ClientSession()
    response = await session.get(url='https://spa5.scrape.center/api/book/?limit=18&offset=0')
    await session.close()
    return await response.json()
if __name__ == '__main__':
    task=asyncio.ensure_future(scrapy_method())
    loop=asyncio.get_event_loop()
    loop.run_until_complete(task)


