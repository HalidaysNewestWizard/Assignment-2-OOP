art = """
 $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\       $$$$$$$\                      $$\       
$$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|      $$  __$$\                     $$ |      
$$ /  $$ |$$ /  \__|$$$$\  $$$$ |$$ |            $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\ 
$$$$$$$$ |$$ |      $$\$$\$$ $$ |$$$$$\          $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |
$$  __$$ |$$ |      $$ \$$$  $$ |$$  __|         $$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  / 
$$ |  $$ |$$ |  $$\ $$ |\$  /$$ |$$ |            $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<  
$$ |  $$ |\$$$$$$  |$$ | \_/ $$ |$$$$$$$$\       $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\ 
\__|  \__| \______/ \__|     \__|\________|      \_______/  \_______|\__|  \__|\__|  \__|
                                                                                                                                                                             
"""
isExit = False

#program loop
while not isExit:
    print(f"{art}\n\n")

    print("-------------Menu--------------")
    print("===============================")
    print("1 - Monthly Payments Calculator")
    print("2 - Amortization Schedule      ")
    choice = input("Type x to exit and any character to continue").lower()

    if choice == "x":
        isExit = True

    
    elif choice == "1":
        client_name = input("Enter Client Name: ")
        client_address = input("Enter Client Address: ")
        purchase_price_property = int(input("Enter price: "))
        downpayment = 0
        downpayment_percentage = 0


        if purchase_price_property <= 500000:
            downpayment = purchase_price_property * 0.05


        elif purchase_price_property > 1000000:
            downpayment = purchase_price_property * 0.20

        else:
            remainder = purchase_price_property - 500000
            remainder_downpayment = remainder * 0.10
            downpayment = 25000 + remainder_downpayment
    


    elif choice == "2":
        print("amortization schedule")
        
        


