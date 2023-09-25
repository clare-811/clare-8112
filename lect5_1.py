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

#append, pop 이용한 queue

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
print(len(queue))
