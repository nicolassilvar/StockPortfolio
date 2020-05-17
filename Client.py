class Client:

    def __init__(self, first_name, last_name, money):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money

    #SET METHODS
    def SetId(self):
        #Read the client dataset if exist

        #Assign the next available

    def SetClientSince(self):
        #Automatically read date since creation

    #DATABASE METHODS
    def WriteClientToFile(self):
        #Write the Client information into the client dataset

    def AddStock(self):
        #Add a Stock to the client

    def RemoveStocl(self):
        #Remove a Stock from Client positions

    def UpdatePortfolioFile(self):
        #WritePortfolio to client file

    def DeleteClient(self):
        #Delete Client from client data set and all related files

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

