generate = "generate any table"
table1 = generate.upper()
print(table1.center(50,"*"))

a = int(input("enter the number: "))
b = int(input ("enter your range: ")) 
for i in range (b):
    print(a,"X", i+1,"=", a*(i+1)) 
    
conclusion = "that's your table now you can note it"
table2 = conclusion.upper()
    
print(table2.center(50,"*"))