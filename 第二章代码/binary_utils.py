'''
初始化时输入String类型的二进制数
'''
class BinaryNum():
    num_mark = ['0','1',1,0]
    def __init__(self, num_str):
        num = [0] * len(num_str)
        for i in range(len(num_str)):
            if num_str[i] in BinaryNum.num_mark:
                num[i] = int(num_str[i])
            else:
                print(f'{num_str} is not a binary number!')
                self.num = 0
        self.num = num

    def __str__(self):
        return "".join([str(i) for i in self.num])
    
    def left_move(self):
        for i in range(len(self.num)):
            if i != len(self.num) - 1:
                self.num[i] = self.num[i+1]
            else: 
                self.num[i] = 0
        return self

    def right_move(self):
        for i in reversed(range(len(self.num))):
            if i != 0:
                self.num[i] = self.num[i-1]
            else: 
                self.num[i] = 0
        return self
    
    def __len__(self):
        return len(self.num)
    
    


 

def binary_add(a,b):
    if type(a) != type(BinaryNum("1001")):
        a = BinaryNum(a)
    if type(b) != type(BinaryNum("1001")):
        b = BinaryNum(b)
    if len(a.num) != len(b.num):
        print(f"{a} and {b} is not same-size!")
        return -1
    add = 0
    ans = [0] * len(a.num)
    for i in reversed(range(len(a.num))):
        if a.num[i] + b.num[i] + add == 3:
            ans[i] = 1
            add = 1
        elif a.num[i] + b.num[i] + add == 2:
            ans[i] = 0
            add = 1
        else:
            ans[i] =  a.num[i] + b.num[i] + add
            add = 0
    return BinaryNum(ans)

def get_comp(a,f):
    if type(a) != type(BinaryNum("1001")):
        a = BinaryNum(a)
    if f == 1 or f == 2:
        if a.num[0] == 0:
            return a
        else:
            one = [0] * len(a.num)
            one[len(a.num) - 1] = 1
            ans = [0] * len(a.num) 
            ans[0] = a.num[0]
            ans[1] = a.num[1]
            for i in range(f,len(a.num)):
                ans[i] = 1 - a.num[i]
            ans = binary_add(ans,one)
            return ans
    else:
        print(f"{f} too high!Need 1 or 2.")
        return -1



if __name__ == "__main__":
    a = BinaryNum("000011")
    b = BinaryNum("110101")
    c = BinaryNum("0011")
    d = BinaryNum("ad123")
    print(a)
    print(b)
    print(binary_add(a,b))
    print(binary_add(a,c))
    print(0.95 ** 20)

