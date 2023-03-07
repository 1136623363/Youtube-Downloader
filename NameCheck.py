import re
from xpinyin import Pinyin

def namecheck(text):
    # 创建拼音转换器实例
    p = Pinyin()

    # 要处理的文本
    #text = "习近平主席在会议上发表了重要讲话。中共中央决定对某些地方的腐败问题进行严肃查处。"

    # 定义中共领导人姓名和其他敏感词列表
    leaders = ["习近平", "李克强", "王沪宁", "赵乐际", "栗战书", "李希", "李强", "赵克志", "陈希", "阳晓东", "李作成","曾毓群","马化腾","马云"]
    sensitive_words = ["中共", "腐败", "严肃", "查处","共产党","中国共产党","两会代表","两会","国家资本主义","民主","美国","海外","中国", '毛泽东', '周恩来', '胡锦涛', '江泽民', '邓小平', '六四', '天安门','民运']

    # 构建正则表达式，用于匹配中共领导人姓名和其他敏感词
    pattern = "|".join(leaders + sensitive_words)
    regex = re.compile(pattern)

    # 检测文本中的中共领导人姓名和其他敏感词，并将其转换为拼音首字母缩写
    def replace_sensitive(match):
        return "".join([p.get_initials(match.group()), ""])

    result = regex.sub(replace_sensitive, text)
    result = result.replace('-', '')
    return result

