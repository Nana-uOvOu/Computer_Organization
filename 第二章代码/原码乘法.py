def mul(x_str,y_str):
    x = [0] * len(x_str)
    y = [0] * len(y_str)
    for i in range(len(x)):
        x[i] = int(x_str[i])
        y[i] = int(y_str[i])
    s_f = x[0] ^ y[0]
    ans = [0] * (2*(len(x) - 1)+1)
    for i in range(len(x)-1):
        ans[len(x) + i] = y[1+i]
    for i in range(len(x)-1):
        print(ans)
        # 判别位为1，部分积加上x
        if ans[len(ans) - 1] == 1:
            temp = bin_add(ans[0:len(x)],x[0:len(x)])
            for j in range(len(temp)):
                ans[j] = temp[j]
            #右移
            ans = right_move(ans)
        else:
            ans = right_move(ans)
    ans[0] = s_f
    return ans
    
def bin_add(a_str,b_str):
    a = [0] * len(a_str)
    b = [0] * len(b_str)
    for i in range(len(a)):
        a[i] = int(a_str[i])
        b[i] = int(b_str[i])
    add = 0
    ans = [0] * len(a)
    for i in reversed(range(len(a))):
        if a[i] + b[i] + add == 3:
            ans[i] = 1
            add = 1
        elif a[i] + b[i] + add == 2:
            ans[i] = 0
            add = 1
        else:
            ans[i] = a[i] + b[i] + add
            add = 0
    return ans

def right_move(a):
    for i in reversed(range(len(a))):
        if i == 0:
            a[i] = 0
        else:
            a[i] = a[i-1]
    return a



    
print(mul('011001','010001'))

