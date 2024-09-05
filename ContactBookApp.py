#empty Dictionary
contacts={}
while True:
    print("\n Contact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. exit ")
    choice =input("enter your choice:= ")
    
    if choice=="1":
        name= input("Enter your name:-")
        if name in contacts:
            print(f"contact name {name} already exit ")
        else:
            age=input("enter your age =")    
            email=input("enter your email=")
            mobile=input("enter your phone number =")
            contacts[name]={"age":int (age),"email":(email),"mobile":(mobile)}
            print(f'cntact name {name} has been created successfully')

    elif choice=="2":
            name=input("Enter contact name is view =")
            if name in contacts:
                 contacts=contacts[name]
                 print(f'name:{name},age:{age},email:{email},mobile number :{mobile}')
            else:
                 print("contact info not found")    

    elif choice=="3":
         name=input("enter name to update contact =")
         if name in contacts:
            age=input("enter update your age =")    
            email=input("enter update your email=")
            mobile=input("enter update your phone number =")
            contacts[name]={"age":int (age),"email":(email),"mobile":(mobile)}
         else:
              print("contact info not found")                    
    elif choice=="4":
         name=input("Enter contact name to delete=")          
         if name in contacts:
              del contacts[name]
              print("Contact name {name} has been delete successfully")
         else:
              print("Contact info not found")
    elif choice=="5":
         search_name=input("Enter contact name is search =")  
         found=False
         for name,contacts in contacts.items():
              if search_name.lower() in name.lower():
                   print(f'Name -found {name},Age:{age},Email:{email},Mobile Number:{mobile}')
                   found=True
         if not found:
                print("Contact info not found")    
    elif choice=="6":
         print(f"Total contact number is  {len(contacts)}")   
    elif choice=="7":
         print("programe is close ")
         break  
    else:
        
         print("invaild")   
         break                             