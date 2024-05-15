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
#

###
produkti = []

produkts = {
    "name": "Piens",
    "cena": 2.20
}

produkti.append(produkts)
###


import json #json fails
with open('list.json', 'r') as openfile:
    list=json.load(openfile)

    print("sveiki, jūs atrodaties cash registration/kases aparāta programā.") #ievada teksts kas pasaka ko lietotajam vajag darīt
    print("Jūsu uzdevums ir pārdot preces klientiem.")

    food = [["H","Hamburgers", 1,50],["F","Frī kartupeļi", 0,50],["L","Limonāde", 0,79],["O","Onion rings", 1,70],["M","mozzarella sticks", 2,10],["K","Kids happy meal", 2,20],["T","Todays special", 4,39]["S","Months special", 8,99],] #

    def menu(): #the menu
        print("""
            food menu:
            H-Hamburgers, 1,50€
            F-frī kartupeļi, 0,50€
            L-Limonāde, 0,79€
            O-Onion rings, 1,70€
            M-mozzarella sticks, 2.10€
            K-Kids happy meal, 2,20€
            T-Todays special, 4,39€
            S-Months special, 8,99€
            """)
        
        more = "Yes"
        total_cost = list ["Total cost"]
        menu()
        prices = []
        index = 0
        quantity = list[quantity]
        quantity = list["discount"]


        choice = input ("Izvēlieties burtu kas atbilst precei:").upper()
        while choice = "E"
        match = 0
        or i in food:
if choice ==i[0]:
try:
    num = int(input("cik daudz" + str(i[1]) + "s vai klients izvelejas:"))
    exept ValueError:
    Print("Kļūda, lūdzu ievadiet numuru ar cik daudz" + i[1] + "s bija izvēlēti")
    num = int(input("Cik daudz" + str(i[1]) + "s klients izvelejas:"))
    food_price = round(i[2]*num,2)
    total_cost += food_price
    print(i[1],"\t €", food_price)
    entry = [i[1],num,food_price]
    quantity.append(entry)
new_cost = total_cost 














        





        

