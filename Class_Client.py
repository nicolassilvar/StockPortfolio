class Client:

    def __init__(self, first_name, last_name, money):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money

    #SET METHODS
    def SetId(self):
        #Read the client dataset if exist
        #f = open('clientDB.txt','r')
        #Read the ID, and assign the next ID available
        #f.close()
        #Assign the next available
        self.ID = '001'

        return None

    def SetClientSince(self):
        #Automatically read date since creation

        return None
    #DATABASE METHODS
    def WriteClientToFile(self):
        #Write the Client information into the client dataset
        #Assign a client ID
        self.SetId()

        #Write client record to DB
        f = open('clientDB.txt', 'w+')
        f.write(f'{self.ID}, {self.first_name}')
        f.close()

        return None

    def AddStock(self):
        #Add a Stock to the client

        return None

    def RemoveStock(self):
        #Remove a Stock from Client positions

        return None

    def UpdatePortfolioFile(self):
        #WritePortfolio to client file

        return None

    def DeleteClient(self):
        #Delete Client from client data set and all related files

        return None

    #GET METHODS
    def getName(self):
        return first_name + ' ' + last_name

    def getId(self):
        return ClientId

    def getMemberSince(self):
        return ClientSince

    def getMoney(self):
        return money

    def getPosition(self):
        #Return all the stocks in the portfolio
        return None

