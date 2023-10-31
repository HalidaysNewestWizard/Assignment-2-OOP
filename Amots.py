#principal is the opening balance for the account 
isExit = False
while not isExit:
    print("How many years would you like your term to be? ")


    print("======================================================")

    print("Your choices are: ")
    print("1. 1 Years")
    print("2. 2 Years")
    print("3. 3 Years")
    print("4. 5 Years")
    print("5. 10 Years")

    input("Please make your selection now: ")

   
    Years=input()

    if Years == "1":
        AnnualRate=0.0595
        EffectiveRate=(((1+AnnualRate/2)**2)**1/12)-1
        print("With an annual rate of 5.95%")
        print("Your  effective monthly interest rate has been calculated to", round(EffectiveRate,5))
     
    elif Years == "2":
        AnnualRate=0.0590
        EffectiveRate=(((1+AnnualRate/2)**2)**1/12)-1
        print("With an anual rate of 5.9%")
        print("Your  effective monthly interest rate has been calculated to",round(EffectiveRate,5))


    elif Years == "3":
        AnnualRate=0.0560
        EffectiveRate=(((1+AnnualRate/2)**2)**1/12)-1
        print("With an anual rate of 5.6%")
        print("Your  effective monthly interest rate has been calculated to",round(EffectiveRate,5))


    elif Years == "4":
        AnnualRate=0.0529
        EffectiveRate=(((1+AnnualRate/2)**2)**1/12)-1
        print("With an anual rate of 5.29%")
        print("Your  effective monthly interest rate has been calculated to",round(EffectiveRate,5))


    elif Years == "5":
        AnnualRate=0.0600
        EffectiveRate=(((1+AnnualRate/2)**2)**1/12)-1
        print("With an anual rate of 6%")
        print("Your  effective monthly interest rate has been calculated to",round(EffectiveRate,5))

else:isExit=True
