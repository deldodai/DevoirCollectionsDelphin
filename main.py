#I. creation de la liste des 10 elements
print("I. Création d'une liste de 10 éléments de type chaîne de caractères")
element_list=[
    "Mercedes",
    "BMW",
    "Volkswagen",
    "Mazda",
    "Porche",
    "Ford",
    "Renaut",
    "Citroen",
    "Toyota",
    "Opel"]

# 1. Affichage des elements de la liste
print("1. Affichage des elements de la liste")
for i in element_list:
    print(i)
    
#2. Afficher le contenu numero 5 de la liste
print("2. Afficher le contenu numero 5 de la liste")
print(element_list[5])


#3. création d'une nouvelle liste et insertion des elements contenant la lettre 'a'
print("3. création d'une nouvelle liste et insertion des elements contenant la lettre 'a'")
new_list=[]
for i in element_list:
    b=[]
    b=list(i)
    ela='a'
    if ela in b:
        new_list.append(i)
print("liste des elements contenant la lettre 'a'")
print(new_list)