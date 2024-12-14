"""
字符串相关自定义工具


"""

def str_reverse(s):
    """
    反转字符串
    :param s:将要被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    字符串切片
    :param s:将要被切片的字符串
    :param x:切片的开始下标
    :param y:切片的结束下标
    :return:切片后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("abcdef"))
    print(substr("abcdef",0,3))
