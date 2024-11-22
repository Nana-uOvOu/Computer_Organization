import binary_utils

def divide(a,b):
    # 先判溢出，小数要求被除数<除数
    if compare_large(a,b) != -1:
        print(f'{a} >= {b},OVERFLOW!')
        return -1
    # 再获取结果符号
    s_f = a.num[0] ^ b.num[0]
    # 获取绝对值
    a.num[0] = 0
    a.num[1] = 0
    b.num[0] = 0
    b.num[1] = 0
    # 获取-b的补码
    minus_b = binary_utils.get_comp([0,0] + b.num[2:] if b.num[0] == 1 else [1,1] + b.num[2:] ,2)
    # 初始化余数拼接上商数组
    ans = [0] * (2 * len(a.num) - 1)
    for i in range(len(a.num)):
        ans[i] = a.num[i]
    ans = binary_utils.BinaryNum(ans)
    temp = binary_utils.binary_add(ans.num[0:len(a.num)],minus_b.num)
    for i in range(1,len(a.num) - 1):
        # 被除数减去除数，结果为负则不够减，上商为0，恢复余数，代码中则无需加入temp
        # 结果为正，上商为1，后左移
        if temp.num[0] == 0:
            for j in range(len(temp.num)):
                ans.num[j] = temp.num[j]
            ans.num[len(ans) - 1] = 1   #上商为1
            # 左移
            if i != len(a.num) - 2:
                ans.left_move()
                # 减去除数
                temp = binary_utils.binary_add(ans.num[0:len(a.num)],minus_b.num)
        else:
            ans.num[len(ans) - 1] = 0   #上商为0
            # 左移
            if i != len(a.num) - 2:
                ans.left_move()
            # 加上除数
            temp = binary_utils.binary_add(ans.num[0:len(a.num)],b.num)

        

    return binary_utils.BinaryNum([s_f] + ans.num[len(a.num)+1:])








def compare_large(a,b):
    for i in range(2,len(a.num)):
        if a.num[i] > b.num[i]:
            return 1
        elif a.num[i] < b.num[i]:
            return -1
    return 0

if __name__ == "__main__":
    a = binary_utils.BinaryNum("0010101")
    b = binary_utils.BinaryNum("1111110")
    print(divide(a,b))