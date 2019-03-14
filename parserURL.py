# -*- coding:utf-8 _*-

'''
深信服2019春招笔试题1

题目描述：

一个百分号%后面跟一个十六进制的数字，则表示相应的ASCII码对应的字符，如 %2F 表示 /； %32 表示 2.
%编码还可以进行嵌套，如 %%32F 可以解析为 %2F 然后进一步解码为 /。

输入：
第一行是一个正整数 T ，表示 T 个样例。
对于每个测试样例，输入一个字符串 s ，字符串不包括空白符且长度小于100,000.

输出：
T 行，每行一个字符串，表示解码结果，解析到不能继续解析为止。

通过率：70% （还没发现问题出在哪）

'''



def parserURL(url):
    if len(url) < 3:
        return url
    j = len(url) - 1
    # 找到最后一次出现的%
    while j >= 0 and url[j] != '%':
        j -= 1
    # 没有百分号则非法
    if j < 0:
        return url
    while j >= 0:
        # 如果后面的数字至少还有两位
        if j < len(url) - 2:
            i = j + 1
            # 判断后面两位是否是合法的十六进制
            # print 'n : ', url[i:i + 2], ':', int(url[i:i + 2], 16), ':', chr(int(url[i:i+2], 16))
            try:
                n = int(url[i:i+2], 16)
                # 注意如果此时已经到了最后一位
                if j + 2 == len(url):
                    # print '----', chr(int(url[j:j+2], 16))
                    url = url[:i-1] + chr(n)
                else:
                    url = url[:i-1] + chr(n) + url[i+2:]
            except:
                j -= 1
            # print 'url : ', url
        # j 继续向前移动，找到上一个%
        # print j, url
        else:
            j -= 1
        while 0 <= j and url[j] != '%':
            j -= 1

    # print 'url : ', url
    return url


if __name__ == '__main__':
    n = raw_input()
    for i in range(int(n)):
        url = raw_input()
        print parserURL(url)
    # print parserURL('%%323%%32F%3H')