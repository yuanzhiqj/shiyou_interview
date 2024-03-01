
def change(str, k):
    # 用双指针维护窗口内的k个数据
    left = 0
    right = 0
    len_str = len(str)
    # 定义字典，存储窗口内字符出现的数量
    dict = {}
    # 返回的结果字符串
    res = ""

    # 遍历字符串
    for i in range(len_str):
        c = str[i]
        #字符第一次出现，存入字典
        if dict.get(c) == None:
            dict[c] = 1
            res += c
        else:
            #该字符在前k个字符在出现过
            if dict[c] > 0:
                res += '-'
            else:
                res += c
            dict[c]+=1
        #维护大小为k的窗口
        if right-left < k:
            right+=1
        else:
            #左指针对应的字符出列
            dict[str[left]]-=1
            left+=1
            right+=1
    return res


if __name__ == '__main__':
    s = input("Please enter a string: ")
    k = int(input("Please enter a number of k: "))
    res = change(s, k)
    print(res)


