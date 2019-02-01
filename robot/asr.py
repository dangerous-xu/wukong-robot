from aip import AipSpeech
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaiduASR():
    """
    百度的语音识别API.
    要使用本模块, 首先到 yuyin.baidu.com 注册一个开发者账号,
    之后创建一个新应用, 然后在应用管理的"查看key"中获得 API Key 和 Secret Key
    填入 config.xml 中.
    ...
        baidu_yuyin: 
            appid: '9670645'
            api_key: 'qg4haN8b2bGvFtCbBGqhrmZy'
            secret_key: '585d4eccb50d306c401d7df138bb02e7'
        ...
    """

    SLUG = "baidu-stt"

    def __init__(self, appid, api_key, secret_key, **args):
        super(self.__class__, self).__init__()
        self.client = AipSpeech(appid, api_key, secret_key)

    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def transcribe(self, fp, frameRate=16000):
        # 识别本地文件
        res = self.client.asr(self.get_file_content(fp), 'wav', frameRate, {
            'dev_pid': 1936,
        })
        if res['err_no'] == 0:
            logger.info(('百度语音识别到了', res['result']))
            return res['result']
        else:
            logger.info('百度语音识别出错了：' + res['err_msg'])
            return []
        