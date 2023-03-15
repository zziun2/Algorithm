#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 재귀함수
def fac(num) :
    if num <= 1 :
        return 1
    else :
        return num * fac(num-1)
    
n = int(input())
print(fac(n))

