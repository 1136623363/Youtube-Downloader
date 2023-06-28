import re
from xpinyin import Pinyin

def namecheck(text):
    # 创建拼音转换器实例
    p = Pinyin()

    # 要处理的文本
    #text = ""

    # 定义敏感词列表
    leaders = []
    sensitive_words = []

    # 构建正则表达式，用于匹配敏感词
    pattern = "|".join(leaders + sensitive_words)
    regex = re.compile(pattern)

    # 检测文本中的敏感词，并将其转换为拼音首字母缩写
    def replace_sensitive(match):
        return "".join([p.get_initials(match.group()), ""])

    result = regex.sub(replace_sensitive, text)
    result = result.replace('-', '')
    return result

