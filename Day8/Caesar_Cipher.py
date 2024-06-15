import os

logo = """
                                                                                                                       
   _|_|_|                                                          _|_|_|  _|            _|                            
 _|          _|_|_|    _|_|      _|_|_|    _|_|_|  _|  _|_|      _|            _|_|_|    _|_|_|      _|_|    _|  _|_|  
 _|        _|    _|  _|_|_|_|  _|_|      _|    _|  _|_|          _|        _|  _|    _|  _|    _|  _|_|_|_|  _|_|      
 _|        _|    _|  _|            _|_|  _|    _|  _|            _|        _|  _|    _|  _|    _|  _|        _|        
   _|_|_|    _|_|_|    _|_|_|  _|_|_|      _|_|_|  _|              _|_|_|  _|  _|_|_|    _|    _|    _|_|_|  _|        
                                                                               _|                                      
                                                                               _|                                      
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift):
    answer=""
    for pos in range(0, len(message)):
        if not message[pos]==' ':
            answer += letters[(letters.index(message[pos])+shift)%26]
    return answer

def decode(message, shift):
    answer=""
    for pos in range(0, len(message)):
        if not message[pos]==' ':
            answer += letters[(letters.index(message[pos])-shift)%26]
    return answer
    
running = True 

os.system('cls' if os.name=='nt' else 'clear')
print(logo)
    
while running:

    operation = input("Type 'encode', 'decode' or 'exit' :\t")
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)
    
    if operation=='encode' or operation=='decode':
        message = input("Enter the message : \n")
        shift = int(input("Enter the shift number : \t"))
        if operation=='encode':
            print(f"Encoded message :\n{encode(message, shift)}")
        else:
            print(f"Encoded message :\n{decode(message, shift)}")
    else:
        print("Thank you for using  the program.")
        running=False
