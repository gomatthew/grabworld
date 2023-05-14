from pyquery import PyQuery as pq
with open('test.html', 'r', encoding='utf-8') as f:
    html = f.read()
doc = pq(html)
# 获取代理报文
tr_items = doc('.mt-0.mb-2.table-responsive tbody tr').items()


def extract_tr_obj(tr_obj):
    for td_item in tr_obj:
        yield td_item.text()

def insert_mysql():
    ''''''

def foo(tr_items):
    for tr_item in tr_items:
        g= extract_tr_obj(tr_item('td').items())
        host,port = next(g).split(':')
        http_type = next(g)
        hide_type = next(g)
        address = next(g)
        response_time = next(g)
        keep_alive = next(g)
        rank = next(g)
        return host,port,address,response_time,keep_alive,rank

foo(tr_items)
    # for td_item in tr_item('td').items():
    #     host,port =extract_tr_obj(td_item)
        # address =
        # speed=
        # keep_alive =
        # is_useful =
        # from_url =
        # create_time =

# 获取  页码
#
# page = doc('.page-item').eq(-2).text()
# print(page)