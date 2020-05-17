# Final521
Final Project CS521

The program will be a Client Portofilio Software.

Quick idea of how it will run:

SCREEN LOG IN
1. New Client
2. Existing Client

If is a new client, it will create the account and write to client database file
If existing, request Id, and load information from file

ONCE LOGGED IN
-> display portfolio information (TBD Details)
-> Actions:
  -> Buy/Sell a Stock
  -> Plot Portfolio
  -> Load News (TBD)
  
 -----------------------------------------------------------------------------------
 
 CLASS DIAGRAM
 
 Class Name: Client
 -> Data
 name (string)
 member_since (string)
 member_id (int)
 
-> Methods
get_name()
get_member_id()
get_member_since()
