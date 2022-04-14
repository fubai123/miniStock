# 工具方法文件

def get_type_by_code(code: str) -> str:
    """
    根据代码获取前缀
    :param code:
    :return:
    """
    code_type = ''
    if code.find('60', 0, 3) == 0:
        code_type = 'sh'
    elif code.find('688', 0, 4) == 0:
        code_type = 'sh'
    elif code.find('900', 0, 4) == 0:
        code_type = 'sh'
    elif code.find('00', 0, 3) == 0:
        code_type = 'sz'
    elif code.find('300', 0, 4) == 0:
        code_type = 'sz'
    elif code.find('200', 0, 4) == 0:
        code_type = 'sz'
    return code_type
