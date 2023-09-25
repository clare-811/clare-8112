""" import calc
#print(dir(calc))
#res = calc.add(8,4)
#print(res)
print(calc.add(8,4))
print(calc.sub(8,4))
print(calc.mul(8,4))
print(calc.div(8,4)) """

""" import calc as cl

print(cl.add(6,3))
print(cl.sub(6,3))
print(cl.mul(6,3))
print(cl.div(6,3)) """

import mod.circle_mod as cm

""" print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5)) """

""" def cutstr(st,wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url, "/", 3)
print(rs) """

""" import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res) """


""" import math
sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi /2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res)

import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi) """

""" import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres) """

""" import mod.utils as mu

my_list = ['apple', 'banana', 'cherry']
print(mu.rd_int(1,100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar()) """

""" from datetime import datetime as dt

print(dt.now())

#문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)
 """
""" 
import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res) """

""" import os

# 현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경
os.chdir('../')

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력
print(os.listdir())

#디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

#디렉토리 삭제
os.rmdir('mew_directory')
print(os.listdir()) """

""" import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir("python")
print(os.listdir()) """

import sys
print(sys.version)
print(sys.argv)
