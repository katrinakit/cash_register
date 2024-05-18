#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu-------------------
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)--------------------
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)------------
# 0.5pt dzēst preci pēc kārtas numura---------------
# 0.5pt atcelt ievadu / iztukšot preču sarakstu----------------
# 0.5pt piemērot atlaidi, ievadīt summu procentos------------
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu-----------
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas-----------
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)--------------
#     0.5pt izdrukāt kopējo summu---------------------

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
#
import json

produkti_file = open ('produkti.json')
produkti = json.load(produkti_file) 
produkti_file.close()
###

produkts = {}
discount=0
#produkti.append(produkts)

print("Guten morgen! Please tell me, what would you like and remember we only take credit cash, no credit cards ")
while True: # katru reizi parada to garo print un visa programma darbojas
    
    print("""press one of the following buttons for further action:
nr.1 to add item
nr.2 show list
nr.3 to remove an item
nr.4 leave my store and delete all of the list
nr.5 add a discount
nr.6 pay for everything
nr.7 get out""")
    command = input("\nChoose command:")
    if command == "1": #pievieno produktu
        produkts={}
        produkts['name']=input("Enter name of product")
        if len(produkts['name']) > 120 or len(produkts['name']) < 2: #nosaukumu validācija
            print("ERROR")
        else:
            produkts['cena']=float(input("Enter price of product"))
            if produkts['cena'] > 9999 or produkts['cena'] < 0: #cenas validācija
                print("ERROR")
            else:
                produkti.append(produkts)
            print(produkti)
    if command == "2": #parada listu
        print(produkti)
        
    if command == "3": # noņem produktu
        trashcan=int(input("what product would you like to remove from your list?(write the number of the product)"))
        produkti.pop(trashcan-1)
        print()
    if command == "4": # noņem visus produktus no lista
       print("you wished to delete all of your list, remeber refund is not given if you did not buy anything")
       produkti=[]
    if command == "5": # iedod/pievieno akciju vai atlaidi
       discount=int(input("Enter discount(%): "))
    if command == "6": #samaksa
        total=0
        for product in produkti: #saskaita kopeja produktu summu
            total= total + product['cena']
        print("Sales: ", total)
        print("Discount: ",discount,"%")
        print("Total Sales: ", total-total*(discount/100))
        payment=float(input("please pay, remember we only take cash"))
        if payment<total-total*(discount/100):# parbauda vai pietiek naudas
            print("you dont have enough money please remove some of the products")
        else:
            exchange=payment-(total-total*(discount/100))
            print("here's your exchange", exchange)
    if command == "7": # iziet ara
        with open ("produkti.json", "w") as outfiles:
            json.dump(produkti, outfiles)
        print("Exiting...")
        break
###


















        





        

