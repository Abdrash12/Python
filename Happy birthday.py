def happy_birthday(name:str,age:int):
    print("Happy",age,"th birthday", name,"!!!")
name_input = str(input("Enter the name of the person: "))
age_input = int(input("Enter the age of the person: "))
happy_birthday(name_input,age_input)