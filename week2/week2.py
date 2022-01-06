print("要求一：函式與流程控制")
def calculate(min, max):
    sum=0
    for x in range(min, max+1):
        sum=sum+x
    print(sum)
calculate(1,3)
calculate(4,8)

print("要求二：Python 字典與列表")
def avg(data):
    num=len(data["employees"])
    sum=0
    for i in range(num):
        salary=data["employees"][i]["salary"]
        sum=sum+salary
    print(sum/num)
avg({
    "count":3,
    "employees":[
    {
    "name":"John",
    "salary":30000
    },
    {
    "name":"Bob",
    "salary":60000
    },
    {
    "name":"Jenny",
    "salary":50000
    }
    ]
}) # 呼叫 avg 函式


print("要求三：演算法")
def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    one = 0
    max = -float('inf') #最小負數
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                one = nums[i] * nums[j]
                # print(one)
                if one > max:
                    max = one
    print(max)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


print("要求四：演算法")
def twoSum(nums, target):

    array=[]
    for i in range(len(nums)):
        for j in range(len(nums)): 
            if nums[i] + nums[j] == target:
                # print(i, j)
                array.append(i)
                array.append(j)
                return array
                
        
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


