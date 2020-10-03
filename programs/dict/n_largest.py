from operator import itemgetter 
  
# Initialize dictionary 
test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6, 'for' : 7, 'geeks' : 3 } 
  
# Initialize N  
N = 3
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# N largest values in dictionary 
# Using sorted() + itemgetter() + items() 
res = dict(sorted(test_dict.items(), key = itemgetter(1), reverse = True)[:N]) 
  
# printing result 
print("The top N value pairs are  " + str(res)) 