def person(name , **other):
    print("name :" ,name )
    
    for k,v in other.items():
       print(k , ":" , v)
    

person(name = "Shaheer" , age = 15 , location = "Daultala")

