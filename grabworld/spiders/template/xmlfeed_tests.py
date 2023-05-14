from scrapy.spiders import XMLFeedSpider


class XmlfeedTestsSpider(XMLFeedSpider):
    name = "xmlfeed_tests"
    allowed_domains = ["boss.com"]
    start_urls = ["http://boss.com/feed.xml"]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "item"  # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item["url"] = selector.select("url").get()
        #item["name"] = selector.select("name").get()
        #item["description"] = selector.select("description").get()
        return item
