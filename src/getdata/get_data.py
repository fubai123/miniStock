import requests
from src.utils.utils import get_type_by_code
import re


class GetStockData(object):

    def __init__(self, url):
        self.url = url

    def get_tick_data(self, code):
        """
        获取股票数据
        :param code:
        :return: 数据字典，字典的key 如下
        ['股票名称', '开盘价', '昨日收盘价', '当前价格', '今日最高价', '今日最低价', '买一价', '卖一价', '成交的股票数',
                 '成交金额', '买一数量', '买一报价', '买二数量', '买二报价', '买三数量', '买三报价', '买四数量', '买四报价',
                 '买五数量', '买五报价', '卖一数量', '卖一报价', '卖二数量', '卖二报价', '卖三数量', '卖三报价', '卖四数量', '卖四报价',
                 '卖五数量', '卖五报价', '日期', '时间', '-', '股票代码', '涨幅']
        """
        code_type = get_type_by_code(code)
        stock_url = '{}{}{}'.format(self.url, code_type, code)
        headers = {'Referer': 'https://finance.sina.com.cn/'}
        page = requests.get(stock_url, headers=headers)
        stock_info = page.text
        return self.data_parse(stock_info, code)

    def data_parse(self, data, code):
        re_str = re.compile('"(.*)"')
        data_ = re.findall(re_str, data)[0]
        mt_info = data_.split(",")[0: 32]  # 爬取到数据信息
        title = ['股票名称', '开盘价', '昨日收盘价', '当前价格', '今日最高价', '今日最低价', '买一价', '卖一价', '成交的股票数',
                 '成交金额', '买一数量', '买一报价', '买二数量', '买二报价', '买三数量', '买三报价', '买四数量', '买四报价',
                 '买五数量', '买五报价', '卖一数量', '卖一报价', '卖二数量', '卖二报价', '卖三数量', '卖三报价', '卖四数量', '卖四报价',
                 '卖五数量', '卖五报价', '日期', '时间']
        data_dict = {'股票代码': code}
        assert len(title) == len(mt_info), '列表长度不同！'
        for i in range(len(mt_info)):
            data_dict[title[i]] = mt_info[i]
            # print(title[i], '\t', mt_info[i])
        # 计算涨幅
        zf = (float(mt_info[3]) - float(mt_info[2])) / float(mt_info[2]) * 100
        zf = format(zf, '.2f')
        data_dict['涨幅'] = str(zf) + '%'
        # print(
        #     '股票名称:{}({}) 当前价格:{} 涨幅：{} 日期时间:{} {}'.format(data_dict['股票名称'], stock, data_dict['当前价格'], zf, data_dict['日期'],
        #                                                   data_dict['时间']))
        return data_dict


if __name__ == '__main__':
    stock_url = 'http://hq.sinajs.cn/list='
    stock = GetStockData(url=stock_url)
    data_dict = stock.get_tick_data('600519')
    # data_dict = stock.get_tick_data('002127')
    print(data_dict)
