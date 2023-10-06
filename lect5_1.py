#stack

""" st = []

#스택에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

#스택의 상태 확인
print(st) #[1, 2, 3]

#스택에서 값 빼기
top = st.pop()
print(top) # 3
print(st) #
print(len(st)) # """

""" #append, pop 이용한 queue

#빈 큐 생성
queue = []

#큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue) # [1, 2, 3]

#큐에서 값 빼기
front = queue.pop(0)
print(front) # 1
print(queue) # [2, 3]
print(len(queue)) """

""" qlist = []

def enqueue(qlist, data):
    qlist.append(data)
    
def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist, 1)
print (qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist) """

""" # 0(1)
import time 
arr = [1, 2, 3, 4, 5]

def ret_01(idx) :
    return arr[idx]

start = time.time()
print(ret_01(2))
end = time.time()
print(f"{end - start : 5f} sec") """

""" # 0(n)
import time
arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)
        
start = time.time()
print_elements(arr)
end = time.time()

print(f"{end - start : 5f} sec") """

""" def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.") """
    
""" # 0(n2)

import time

def mul_for() :
    for i in range(5) :
        for j in range(5) :
            print(i, j)
        
start = time.time()    
mul_for()
end = time.time()
print(f"{end - start : 5f} sec") """

""" #버블 정렬
def bubble_sort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(i, j, arr, arr[i], arr[j])
    return arr

lrr = [1, 9, 2, 7, 5]
print(bubble_sort(lrr)) """

""" # 퀵소트

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv", pivot)
    print("left", left)
    print("mid", middle)
    print("rgt", right)
    
    return quick_sort(left) + middle + quick_sort(right)

my_list = [1, 9, 6, 4, 5, 7, 3, 2]
print(len(my_list))

sorted_list = quick_sort(my_list)

print(sorted_list) """
 
""" import requests
res = requests.get("https://www.google.com")
print(res)
print(res.content) """

""" #numpy
import numpy as np

#1차 배열 생성
#a = np.array([1, 2, 3])
#print(a)

# 2차 3행 배열, 0으로 초기화
#b = np.zeros((2, 3))
#print(b)

# 2차 3행 배열, 1로 초기화
#c = np.ones((2, 3))
#print(c)

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

# 배열 간 연산
f = d + e
g = d - e
h = d * e
i = d / e

print(f)
print(g)
print(h)
print(i) """

""" import pandas as pd

# Create a dataframe
data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
#print(df)

#print(df['Age'].describe())
print(df.sort_values(by= 'Age', ascending=False))
print("================")
print(df.sort_values(by= 'Age', ascending=True))
print("================")
print(df.sort_values(by= 'Name', ascending=True)) """

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y)

plt.xlabel('time')
plt.ylabel('n')
plt.title('Example plot')

plt.show()