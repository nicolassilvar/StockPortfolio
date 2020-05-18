import Class_Client
#import Class_Stock

def CreateNewAccount():
    ''' Function to create a Client object with input
        data from the client and return class obj'''

    name = input("Please enter name: ")
    money = input("Amout of money to invest: ")
    #Assume Name enter First Last
    first_name,last_name = name.split()
    #Create and Return Client Object
    return Class_Client.Client(first_name, last_name, money)

#def LoadUser():

if __name__ == '__main__':

    ControlFlow = True

    while ControlFlow:
        print('Welcome to the Portfolio Tracker')
        print('\n')
        print('Choose from the below')
        print('(1) Create an account \n')
        print('(2) Log in to your account')
        Choice = input('>>>>')

        if Choice == '1':
            #Client obj created
            Client = CreateNewAccount()
            print(f'Mr. {Client.last_name} account created')
            #Store client info in the file
            Client.WriteClientToFile()
            print('Back to main menu, log in again')
            continue

        #elif Choice == '2':
            #LoadUser()
