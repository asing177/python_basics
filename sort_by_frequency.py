from collections import Counter 
  
ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7,  
            1, 1, 2, 4, 7, 8, 9, 6, 6, 6] 
  
# printing initial ini_list 
print ("initial list", str(ini_list)) 
  
# sorting on bais of frequency of elements 
result = [item for items, c in Counter(ini_list).most_common() 
                                      for item in [items] * c] 
  
# printing final result 
print("final list", str(result)) 



from itertools import repeat, chain 
  
ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 
            1, 1, 2, 4, 7, 8, 9, 6, 6, 6] 
  
# printing initial ini_list 
print ("initial list", str(ini_list)) 
  
# sorting on bais of frequency of elements 
result = list(chain.from_iterable(repeat(i, c) 
         for i, c in Counter(ini_list).most_common())) 
  
# printing final result 
print("final list", str(result)) 



ini_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 
               5, 5, 5, 4, 4, 4, 4, 4, 4] 
  
# printing initial ini_list 
print ("initial list", str(ini_list)) 
  
# sorting on bais of frequency of elements 
result = sorted(ini_list, key = ini_list.count, 
                                reverse = True) 
  
# printing final result 
print("final list", str(result)) 