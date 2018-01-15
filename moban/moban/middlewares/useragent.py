# coding:utf-8
import random

class RandomUserAgentMiddleware(object):
    """
    随机分配user-agent
    """
    def __init__(self,settings):
        self.user_agent_list = settings.getlist('USER_AGENTS')

    def random_useragent(self):
        print random.choice(self.user_agent_list)
        return random.choice(self.user_agent_list)

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings)

    def process_request(self,request,spider):
        request.headers['User-Agent'] = self.random_useragent()