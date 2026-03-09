palabra_secreta="perro"
palabra=""
contador =6
lista_resultados=[]

while palabra != palabra_secreta:
    palabra= input("adivina la palabra: ") 
    contador=contador-1
    if contador==0:
        print("Te quedaste sin intentos")
        break
    
    lista_resultados.clear() 
    
    
    if len(palabra) != 5:
        print("la palabra debe contener 5 letras")
    
    if len(palabra)==5:
        
        for i in range (len(palabra_secreta)):
                
            if palabra.lower()[i] == palabra_secreta[i]:
                lista_resultados.append("🟩 "+palabra[i])
            
                    
            elif palabra.lower()[i] in palabra_secreta:
                lista_resultados.append("🟨 "+palabra[i])
            
            
            elif palabra.lower()[i] not in palabra_secreta:
                lista_resultados.append("⬛ "+palabra[i])
    
    print(lista_resultados)
    if palabra.lower()!= palabra_secreta:
        print(f"te quedan {contador} intento/s") 
    if palabra.lower()== palabra_secreta:
        print("Ganaste!!!")

