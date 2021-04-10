bank_accounts = ['1111','2222','3333','4444','5555','6666']
account_price = ['1000','2000','3000',4000,5000,6000,7000,8000,9000,10000]
comand = ["ok"]
user_input = ""
while user_input != "cancel":
    user_input = input("Enter pin")
    if user_input !="cancel":
        for account_numbers in bank_accounts:
            if user_input == account_numbers:
                print("please wait")
                user_input = ""
                while user_input !="cancel":
                    user_input = input("enter your price")
                    for price_enter in account_price:
                        if user_input == price_enter:
                            print("please wait your transation is processing")
                            user_input = ""
                            user_input = input("enter ok to comfrom")
                            # for user_input ="cancel":
                            for enter_com in comand:
                                if user_input == enter_com:
                                    print("process sucessfull completed")