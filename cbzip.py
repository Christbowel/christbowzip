import zipfile
  
                                                    
def crack_password(password_list, obj):
    
    idx = 0
                                                                                                                                           
 
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("mot de passe trouve' ligne ",idx)
                    print("le mot de passe trouve est : ", word.decode())
                    return True
                except:
                    continue
    return False

password_list = input("entrer le nom de la wordlist si vous n'avez pas  entrer rockyou.txt: ")
  
zip_file = input("entrer le nom du fichier zip ainsi que son extension: ")


# initialisation

obj = zipfile.ZipFile(zip_file)
  
# calcul du nombre de mot present dans la wordlist

cnt = len(list(open(password_list, "rb")))
  
print("il y'a au total ",cnt ,"mots a tester")
  
if crack_password(password_list, obj) == False:
    print("mot de passe introuvable dans ce fichier")


print ("by christ bowel")
