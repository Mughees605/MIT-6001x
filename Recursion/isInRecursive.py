# str = 'abcdefghijklmnopqrstuvwxyz'
# high = len(str)
# low = 0
# char = 'o'
# mid = int((high + low) /2)

# while mid >= 0:
#     if str[mid] == char:
#         print('yes its is in at', mid )
#         break
#     elif str[mid] > char:
#         high = mid
#         mid = int((high + low) / 2)
#     elif str[mid] < char:
#         low = mid
#         mid = int((high + low) / 2)
#     else:
#         print("not find a solution")
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 1:
        return aStr == char
    if aStr[int(len(aStr)/2)] == char:
        return True
    else:
        if aStr[int(len(aStr)/2)] > char:
           return isIn(char, aStr[0:int(len(aStr)/2)])
           
        elif aStr[int(len(aStr)/2)] < char:
         return  isIn(char, aStr[int(len(aStr)/2):])
            
print(isIn('a','abc'))
         
        
        
    
    
        
    

