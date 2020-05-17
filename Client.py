class Client:

    def __init__(self, first_name, last_name, money):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money

    #ASSIGN METHODS
    def AssignId(self):
        #Read the client dataset if exist

        #Assign the next available

    def AssignClientSince(self):
        #Automatically read date since creation

    #DATABASE METHODS
    def WriteClientToFile(self):
        #Write the Client information into the client dataset

    def DeleteClient(self):
        #Delete Client from client data set

    #GET METHODS
    def getName(self):
        return first_name + ' ' + last_name

    def getId(self):
        return ClientId

    def getMemberSince(self):
        return ClientSince

    def getMoney(self):
        return money

