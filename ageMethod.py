def AgeResponse(user_Age):
    if user_Age <= 16:
        print('Not of working age')
    elif user_Age >= 64:
        print('Retired')
    else:
        print('Working age')

AgeResponse(16)
AgeResponse(30)
AgeResponse(64)