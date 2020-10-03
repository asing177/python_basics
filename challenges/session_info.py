import sys
import math


#INPUT
# 4,c
# 1,a
# 1,a
# 2,a
# 1,b
# 2,d
# 2,d
# 2,d
# 1,e
# 3,b
# 3,b
# 3,b
# 3,f
# 3,f
# 3,f
# 4,c
# 3,a

session_info = {}
l1 = {}
t = int(input())
for i in range(t):
    row = input()
    user_id,session_id = row.split(",")
    if user_id in session_info:        
        session_info[user_id].append(session_id)
    else:
        session_info[user_id] = [session_id]
    
for k in session_info:
    l1[k] = len(session_info.get(k))


for k,v in l1.items():
    print(k,",",v)

    