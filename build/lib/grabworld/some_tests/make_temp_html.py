import requests
import asyncio
import aiohttp
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
}
url = 'http://www.nimadaili.com/https/1/'


async def make_temp_html(fetch_url):
    resp = requests.get(url=fetch_url, headers=headers)
    if resp.status_code == requests.codes.ok:
        with open('test.html', 'w', encoding='utf-8') as f:
            f.write(resp.text)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(make_temp_html(url))
    loop.run_until_complete(task)