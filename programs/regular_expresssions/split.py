from re import split 
  
# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 
  
# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
  
# '\d+' denotes Numeric Characters or group of characters 
# Splitting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 


# Splitting will occurs only once, at '12', returned list will have length 2 
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1)) 
  
# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here')) 