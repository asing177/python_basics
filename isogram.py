def is_isogram(word): 
  
    # Convert the word or sentence in lower case letters. 
    clean_word = word.lower() 
  
    # Make an empty list to append unique letters 
    letter_list = [] 
  
    for letter in clean_word: 
  
        # If letter is an alphabet then only check 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter) 
  
    return True



print(is_isogram("Machine"))                              
print(is_isogram("isogram"))                          
print(is_isogram("GeeksforGeeks"))                      
print(is_isogram("Alphabet "))  




def check_isogram(string) :  
  
    length = len(string)
    mapHash = [0] * 26 
  
    # loop to store count of chars 
    # and check if it is greater than 1  
    for i in range(length) :  
      
        mapHash[ord(string[i]) - ord('a')] += 1;  
  
        # if count > 1, return false  
        if (mapHash[ord(string[i]) - ord('a')] > 1) :  
          
            return False 
  
    return True


string = "geeks"
string2 = "computer"

print(check_isogram(string))
print(check_isogram(string2))