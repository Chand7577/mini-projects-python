#caesar cipher
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_key_size=len(SYMBOLS)


def getMode():
    while True:
        print("Wanna encrypt or decrypt the message.....?")
        mode=input().lower()
        if mode in ['encrypt','e',"decrypt","d"]:
            return mode

        else:
            print('Choose "encrypt" or "e" or "decrypt" or "d "')


def getMessage():
    message=input("Enter the message ").upper()
    return message

def getKey():
    key=0

    while True:
        print(F'Enter the key number (1-{max_key_size})')
        key=int(input())
        if key>=1 and key<=max_key_size:
            return key




def getEncodedMessage(mode,message,key):
    
    
    translated=""
    if mode[0]=="d":
        key=-key

   

    for symbol in message:
      
        symbolIndex=SYMBOLS.find(symbol)
        
        if symbolIndex==-1:
            translated+=symbol # this will add all the characters which are not part of the alphabets such as ,*,(,)


        else:  # encrypt or decrypt
            symbolIndex+=key
          

            if symbolIndex>=max_key_size:
                symbolIndex-=max_key_size

            elif symbolIndex<0:
                symbolIndex+=max_key_size

            translated+=SYMBOLS[symbolIndex]
            
    return translated

mode=getMode()

message=getMessage()
key=getKey()

encoded_message=getEncodedMessage(mode,message,key)

print("Your encoded message>>>>>>>>>>>>> "+ encoded_message)