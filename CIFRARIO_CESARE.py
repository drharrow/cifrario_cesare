#lab10.2.1
 
def main():
    key_word = input("Inserisci la parola chiave con cui decifrare/cifrare il file: ")
    filename = input("Inserisci il nome del file da elaborare: ")
    
    key_word = key_word.upper()
    chiave = cifratura(key_word)
    
    try:
        FILE = open(filename, "r", encoding="utf-8")
    except OSError:
        exit(f"Errore: il file '{filename}' è inesistente o nel formato non corretto.")
    
    OUTPUT = open("file_elaborato.txt", "w" , encoding="utf-8")
    
    
    comando = input("Vuoi decriptare o criptare il file (D/C)? : ")
    
    if comando.upper() == "D":
        for line in FILE:
            for ch in line:
                if "A" <= ch <= "Z":
                    new_ch = lettera_corrispondente(chiave,ch,"D")
                    OUTPUT.write(new_ch)
                elif "a" <= ch <= "z":
                    new_ch = lettera_corrispondente(chiave,ch,"D")
                    OUTPUT.write(new_ch.lower())
                else:
                    OUTPUT.write(ch)
    elif comando.upper() == "C":
        for line in FILE:
            for ch in line:
                if "A" <= ch <= "Z":
                    new_ch = lettera_corrispondente(chiave,ch,"C")
                    OUTPUT.write(new_ch)
                elif "a" <= ch <= "z":
                    new_ch = lettera_corrispondente(chiave,ch,"C")
                    OUTPUT.write(new_ch.lower())
                else:
                    OUTPUT.write(ch)
    OUTPUT.close()
    FILE.close()
                    
                    
                          
         
         
# ----------------------------------------------------------------------------------------------------------------  
         
           
def cifratura(parola):
    chiave = []
    for ch in parola:
        if ch not in chiave:
            chiave.append(ch.upper())
    for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
        if ch not in chiave:
            chiave.append(ch)
    return chiave

def lettera_corrispondente(chiave,lettera,modalità):
    alfa = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    alfabeto = alfa.split()
    alfabeto.sort()
    i_corrispondente = 0
    
               
    if modalità.upper() == "D":
        for i,ch in enumerate(chiave):
            if ch == lettera.upper():
                i_corrispondente = i
                break
        
        nuova_lettera = alfabeto[i_corrispondente]
        return nuova_lettera
    elif modalità.upper() == "C":
        for i,ch in enumerate(alfabeto):
            if ch == lettera.upper():
                i_corrispondente = i
                break
        
        nuova_lettera = chiave[i_corrispondente]
        return nuova_lettera

        
        
        
main()    
    

