"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
import sys
import json
from sys import argv
from aes import AEScoder
import os
import config
from utils.tgbot_push import tgbot_push

class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')            
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers['Cookie'] = cookies  

    def checkin(self):
        """
        签到函数
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content




if __name__ == '__main__':
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    CFG = {};
    if "cookies" in  os.environ:
        cookies =  os.environ["COOKIES"]
    else:
        COOKIEENCKEY = os.environ["COOKIEENCKEY"]
        aes = AEScoder(COOKIEENCKEY);
        enccookie = open("/".join([sys.path[0], "config.json.enc"])).read();
        cfgstring = aes.decrypt(enccookie);
        CFG = json.loads(cfgstring);
        cookies = CFG['COOKIES']


    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    if 'TGBOG' in os.environ:
        TGBOT = os.environ["TGBOTAPI"]
    else:
        TGBOT = CFG['TGBOTAPI']
    
    if isinstance(TGBOT,str) and len(TGBOT)>0:
        print('检测到 SCKEY， 准备推送')
        tgbot_push(text = '什么值得买每日签到',
                        desp = str(res),
                        secretKeyAPI = TGBOT)
    print('代码完毕')