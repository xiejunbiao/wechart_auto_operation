import requests


class GetToken(object):
    """
    获得token
    """
    def __init__(self):
        self._errcode = {
                        '-1': '系统繁忙，此时请开发者稍候再试',
                        '0': '请求成功',
                        '40001': 'AppSecret错误或者AppSecret不属于这个公众号，请开发者确认AppSecret的正确性',
                        '40002': '请确保grant_type字段值为client_credential',
                        '40164': '调用接口的IP地址不在白名单中，请在接口IP白名单中进行设置。（小程序及小游戏调用不要求IP地址在白名单内。',
                        '89503': '此IP调用需要管理员确认,请联系管理员',
                        '89506': '24小时内该IP被管理员拒绝调用两次，24小时内不可再使用该IP调用',
                        '89501': '此IP正在等待管理员确认,请联系管理员',
                        '89507': '1小时内该IP被管理员拒绝调用一次，1小时内不可再使用该IP调用',
        }
        # https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxc4903c0704b5652a&secret=1ded52f20df5c5781075f04510452074
        self._url = 'https://api.weixin.qq.com/cgi-bin/token?' \
                    'grant_type=client_credential&' \
                    'appid=wxc4903c0704b5652a&' \
                    'secret=1ded52f20df5c5781075f04510452074'

    def get_access_token(self):

        result = requests.get(self._url)
        token_ = result.json()
        if 'errcode' in token_.keys():
            return self._errcode[str(token_['errcode'])], 0

        return token_, 1


def get_token(loging):
    gt = GetToken()
    data, k = gt.get_access_token()
    if k == 0:
        loging.info(data)
        return data
    return data['access_token']


if __name__ == '__main__':

    # print(get_token(logger))
    pass
