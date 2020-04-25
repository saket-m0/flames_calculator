def getnames() :
    name_1 = input("Enter First Name >> ")
    name_2 = input("Enter Second Name >> ")
    name1, name2 = name_1,name_2
    name1 = name1.lower()
    name2 = name2.lower()
    name1.replace(" ","")
    name2.replace(" ","")
    return name_1, name_2, name1, name2

def getuncommons(name_1, name_2) :
    for letter in name_1 :
        for check in name_2 :
            if letter == check :
                name_1 = name_1.replace(letter,"",1)
                name_2 = name_2.replace(check,"",1)
                break
    
    flames_unit = name_1 + name_2
    return flames_unit
    

def find_flames (count) :
    list = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Sister"] 
    temp = 0
    while len(list) > 1 :
        for i in range(count) :
            temp+=1
            if temp > len(list) :
                temp = 1
            
        list.remove(list[temp-1])
        temp -= 1
        
    return list[0]

name1_input, name2_input, fname, sname = getnames()
uncommons = getuncommons(fname, sname)
flames = find_flames(len(uncommons))
print("The Relation between " + name1_input + " and " + name2_input + " is " + flames)
