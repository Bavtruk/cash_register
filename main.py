#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import json

preces = []

             
with open('preces.json', 'r') as openfile:
    preces_file = open('preces.json') 
    preces = json.load(preces_file)
    preces_file.close()

   
#mēs izmantojam šeit while, lai mēs varētu jebkuru no tālāk uzskaitītajiem
    while True:
        print("kases aparatu menu")
        print("1.pievienot jaunu preci - nosaukumu un cenu")
        print("2.dzēst preci pēc kārtas numura")
        print("3.iztukšot preču sarakstu")
        print("4.piemērot atlaidi, ievadīt summu procentos")
        print("5.samaksāt, ja iedota lielāka summa - izdrukāt atlikumu")
        print("6.izdrukāt čeku uz ekrāna - preces nosaukumus un summas")
        print("7.Exit")    
        choice = input("Enter your choice: ")
#mēs izmantojam šeit if,ja atlasītu 1 numuru un pievienotu produktu savam sarakstam  
        if choice == "1":
            nosaukums = input("Enter nosaukums:")
            cena = float(input("Enter prece cena"))
            new_prece ={"nosaukums" : nosaukums, "cena" : cena}
            preces.append(new_prece)
            pass
#šeit, ja atlasāt numuru 2, varat kaut ko noņemt no saraksta      
        if choice == "2":
            id = int(input("Enter the index of the prece to remove:"))
            preces.pop(id)
            pass
#šeit, ja atlasāt numuru 3, varat izdzēst visu sarakstu    
        if choice == "3":
            del preces
            pass
#5% atlaide jebkurai precei, izvēloties numuru 4
        if choice == "4":
            summa = input
            d1 = int(input("10:  "))
            g1 = d1 // 100 * 5
            print("cena ar atlaidu - ", d1 - g1)
            pass
            

        with open("preces.json", "w") as preces_file:
                json.dump(preces, preces_file)