import asyncio
import time
import traceback
import aiohttp
import aiomysql
import requests
from datetime import datetime
from random import randint
from pyquery import PyQuery as pq

seed_url = 'http://www.nimadaili.com/https/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
}

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'makemoney'
MYSQL_DATABASE = 'grabworld'


def get_page_num():
    """ get the number of pages """
    resp = requests.get(url=seed_url, headers=headers)
    if resp.status_code == requests.codes.ok:
        doc = pq(resp.text)
        page_num = doc('.page-item').eq(-2).text()
        return page_num


async def fetch(url, session):
    """ make a request to get html """
    try:
        async with session.get(url) as resp:
            if resp.status == requests.codes.ok:
                data = await resp.text()
                return data
    except BaseException as e:
        print(e)


async def judge_useful(host, port):
    """ make a request to baidu then get the spending time of the Internet request """
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url='https://www.baidu.com', proxy=f'http://{host}:{port}', headers=headers) as resp:
                # resp = requests.get(url='https://www.baidu.com', proxies={'https': host + ':' + port}, headers=headers)
                pass
        except BaseException as e:
            end_time = time.time() - start_time
            return -1, end_time
    end_time = time.time() - start_time
    if resp.status == requests.codes.ok:
        print(f'{datetime.now().strftime("%Y-%m-%d %X")}---IP https://{host}:{port} is available!')
        return 1, end_time
    else:
        print(f'{datetime.now().strftime("%Y-%m-%d %X")}---IP https://{host}:{port} not available!')
        return -1, end_time


def extract_tr_obj(tr_obj):
    """ generator of the html_tr object """
    for td_item in tr_obj:
        yield td_item.text()


async def extract_html(pool, url, html):
    """ extract element of html and insert mysql """
    doc = pq(html)
    async with pool.acquire() as conn:
        tr_items = doc('.mt-0.mb-2.table-responsive tbody tr').items()
        for tr_item in tr_items:
            generator = extract_tr_obj(tr_item('td').items())
            host, port = next(generator).split(':')
            http_type = next(generator)  # useless
            hide_type = next(generator)  # useless
            address = next(generator)
            speed = next(generator)  # useless
            keep_alive = next(generator)
            rank = next(generator)  # useless
            is_useful, response_time = await judge_useful(host, port)

            insert_sql = f'''INSERT INTO proxy_pool(host,port,address,response_time,keep_alive,is_useful,from_url,create_time) VALUES('{host}','{port}','{address}','{response_time}','{keep_alive}','{is_useful}','{url}','{str(datetime.now())}');'''
            async with conn.cursor() as cur:
                await cur.execute(insert_sql)


async def main(loop):
    # http 访问
    # 解析
    # 入库
    # 可用性分析
    try:
        print(f'{datetime.now().strftime("%Y-%m-%d %X")}---start crawl---')
        page_num = int(get_page_num())
        mysql_pool = await aiomysql.create_pool(host=MYSQL_HOST, port=3306, user=MYSQL_USER, password=MYSQL_PASSWORD,
                                                db=MYSQL_DATABASE, charset='utf8', autocommit=True, loop=loop)
        async with aiohttp.ClientSession() as session:
            for i in range(1, page_num + 1):
                print(f'{datetime.now().strftime("%Y-%m-%d %X")}---爬取第{i}页')
                waiting_for_html = True
                url = seed_url + str(i)
                task = asyncio.create_task(fetch(url, session))
                done, pending = await asyncio.wait({task})
                # html = await fetch(url, session)
                retry = 0
                while waiting_for_html:
                    if task in done:
                        waiting_for_html = False
                        break
                    elif retry > 3:
                        break
                    retry += 1
                    print(f'{datetime.now().strftime("%Y-%m-%d %X")}---retry : {retry} time')
                    await asyncio.sleep(5)
                if waiting_for_html is True:
                    # 结果还没出来
                    print(f'{datetime.now().strftime("%Y-%m-%d %X")}---爬取第{i}页超时')
                    continue
                html = task.result()
                await extract_html(mysql_pool, url, html)
                await asyncio.sleep((randint(40, 50)))
    except BaseException as e:
        print('异常为: ' + str(e))
        print('\r\n')
        print(traceback.format_exc())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
