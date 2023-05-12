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

# 4. ajout d'un element à la fin de la liste
print("4. ajout d'un element à la fin de la liste")
element_to_add="Chevrolet"
element_list.append(element_to_add)
print(element_list)

# 5. ajout d'un element à l' index numero 2

print("5. ajout d'un element à l' index numero 2")
element_to_insert_at_index_2="Mitsubishi"
element_list.insert(2,element_to_insert_at_index_2)
print(element_list)

# 6. Suppression de l'element numero 3

print(element_list)
print("6. Suppression de l'element numero 3")
del element_list[2]
print(element_list)

# 7. suppression de l'element à l' index numero 2
print(" 7. suppression de l'element à l' index numero 2")
element_list.pop(1)
print(element_list)


# 8. Odonner la liste
print("8. Odonner la liste")
element_list.sort()
print(element_list)

# 9. Affichage de la liste dans le sens inverse
print("9. Affichage de la liste dans le sens inverse")
element_list.reverse()
print(element_list)


# 10. Vider la liste
print("10. Vider la liste")
element_list.clear()
print(element_list)


# 11. Suppresion de la liste
print(" 11. Suppresion de la liste \n\n\n")
del element_list







# II. Creation d'un tuple
print("II. Création d'une tuple de 10 éléments de type entier \n ")
element_tuple=(10,23,4,5,76,8,7,95,4,8)


# 1. Affichage des element du tuple
print("1. Affichage des elements du tuple")
for i in element_tuple:
    print(i)

#2 . Affichage du nombre de fois ou la valeur 3 apparait
print("2 . Affichage du nombre de fois ou la valeur 3 apparait")
counter=0
for i in element_tuple:
    if i==3:
        counter=counter+1
print (counter)

# 3. Affichage de l'element numero 5
print("3. Affichage de l'element numero 5")
print(element_tuple[4])

# 4. Ordonner le tuple
print(element_tuple)
print("4. Ordonner le tuple")
element_tuple_to_list=list(element_tuple)
element_tuple_to_list.sort()
element_tuple=tuple(element_tuple_to_list)
print(element_tuple)

# 5. Ajouter un element à la fin du tuple

print("5. Ajouter un element à la fin du tuple")
to_add=90
element_tuple_to_list=list(element_tuple)
element_tuple_to_list.append(to_add)
element_tuple=tuple(element_tuple_to_list)
print(element_tuple)

# 6. Ajouter un élément à l’index numéro 3
to_insert=41
element_tuple_to_list=list(element_tuple)
element_tuple_to_list.insert(3,to_insert)
element_tuple=tuple(element_tuple_to_list)

# 7. Affichage de la nouvelle tuple
print("7. Affichage de la nouvelle tuple")
print(element_tuple,"\n\n\n")


