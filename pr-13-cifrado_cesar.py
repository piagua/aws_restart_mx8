### cifrado César practica 12

alphabet="ABC"
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
def getMessage():
    stringToEncrypt = input("Favor de escribir el mensaje a encriptar: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Favor de escribir una llave (whole number from 1-25): ")
    return shiftAmount
    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter) #atrapo el indice que tiene el caracter en mi alfabeto
        newPosition = position + int(cipherKey) # calculo el nuevo indice 
        if currentCharacter in alphabet: # verifica que el caracter pertenezca al alfabeto 
            encryptedMessage = encryptedMessage + alphabet[newPosition] # anezar el caracter a mi mensaje encriptado
        else:
            encryptedMessage = encryptedMessage + currentCharacter #anexo el caracter sin alteracion
    return encryptedMessage


#desencriptar mensaje    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #declaramos alfabeto
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet) #obtenemos el doble
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage() # obtenemos mensaje a encriptar
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
    
runCaesarCipherProgram()