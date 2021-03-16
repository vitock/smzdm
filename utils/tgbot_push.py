
import config
import requests
from urllib.parse import quote


def tgbot_push(text,desp,secretKeyAPI):
    """
    通过serverchan将消息推送到tg
    :param secretKeyAPi
    :param text: 标题
    :param desp: 内容
    :return resp: json
    """
    msg = quote(text) + quote(desp)
    url = f'{secretKeyAPI}&text={msg}'
    session = requests.Session()
    resp = session.get(url)
    return resp.json()


if __name__ == '__main__':
    resp = push_to_wechat(text = 'test', desp='hi', secretKey= config.SERVERCHAN_SECRETKEY)
    print(resp)