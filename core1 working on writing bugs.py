#Add backup/archive file
#Test
#write to text file function temporary for testing.
#make a new function for writing i.e. holds links to erase and write functions in another function. Will cut down on duplication.
#Figure out how to strip a list, or convert the list for stripping.

#account class creation
class account(object):
    aNo = ""
    fN = ""
    sN = ""
    bal = ""
    aSt = ""
    def __init__ (self, accountNo, fName, sName, balance, accountStatus):
        self.aNo = accountNo
        self.fN = fName
        self.sN = sName
        self.bal = int(balance)
        self.aSt = accountStatus

#Getters
    def getAccNo(self):
        return self.aNo
    def getFirstName(self):
        return self.fN
    def getSurname(self):
        return self.sN
    def getBalance(self):
        return self.bal
    def getAccStatus(self):
        return self.aSt

#Setters
    def setFirstName(self):
        self.fN = input("Edit Account holder First Name:")
    def setSurname(self):
        self.sN = input("Edit Account holder Surname:")
    def setBalance(self):
        self.bal = int(input("Edit Account Balance:"))
    def setAccStatus(self):
        self.aSt = input("Edit Account Status - Active/Closed:")

#Balance deposits and withdrawals
    def deposit(self):
        deposit = int(input("Enter Deposit Amount:"))
        self.bal = self.bal + deposit
        print(deposit,'Has been deposited to the account')
    def withdrawal(self):
        withdraw = int(input("Enter Withdrawal Amount:"))
        if self.bal-withdraw >=0:
            self.bal = self.bal - withdraw
            print(withdraw,'Has been withdrawn from the account')
        else:
            print('You cannot go overdrawn')

#close account
    def closeAccount(self):
        if self.bal == 0:
            self.aSt = 'closed'
            print('Account closed')
        else:
            print ('To close an account balance must be 0')

#bankApp class creation
class bankApp(object):

    accountDict={}

#Loading account data from text file to python
    def importAcc(self):
        with open ("prime.txt", "r") as ad:
            txtLines = ad.readlines()
            for line in txtLines:
                txtSplit = line.split(",")
                self.accountDict[txtSplit[0]] = account(txtSplit[0],txtSplit[1],txtSplit[2],txtSplit[3],txtSplit[4])

    def createAccount(self):
        aNo = nextAccNo
        print ("AccountnextAccNo Number:", nextAccNo)
        fN = input("Enter First Name: ")
        sN = input("Enter Surname:")
        bal = input("Deposit Amount: ")
        aSt = "Active"
        self.accountDict[aNo] = account(aNo,fN,sN,bal,aSt)

#Displays all accounts
    def displayAccounts(self):
        for account in bank.accountDict:
            print(self.accountDict[account].getAccNo(), self.accountDict[account].getFirstName(), self.accountDict[account].getSurname(), self.accountDict[account].getBalance(), self.accountDict[account].getAccStatus())

#Erase text file data in preparation for writing.
    def eraseText(self):
        f = open('prime.txt', 'w').close()

#Save account information to text file
    def writeAccounts(self):
        for account in bank.accountDict:
            x = [self.accountDict[account].getAccNo(),",",self.accountDict[account].getFirstName(),",",self.accountDict[account].getSurname(),",",str(self.accountDict[account].getBalance()),",",self.accountDict[account].getAccStatus(),'\n']
            #f = open('prime.txt', 'w').close()
            print (x)
            #this method works until I can figure out how to strip a list, or convert the list for stripping.
            x = ['Active' if i=='Active\n' else i for i in x]
            x = ['Closed' if i=='Closed\n' else i for i in x]
            print (x)
            f = open('prime.txt', 'a')
            f.writelines(x)
            f.close()


#Importing account info in prep for
bank=bankApp()
bank.importAcc()

#predef values for user options
ch=''
num=""

#User options
while ch != 10:

    print("""
    \tMAIN MENU
    1.  NEW ACCOUNT
    2.  DEPOSIT AMOUNT
    3.  WITHDRAW AMOUNT
    4.  BALANCE ENQUIRY
    5.  ALL ACCOUNT HOLDER LIST
    6.  CLOSE AN ACCOUNT
    7.  MODIFY AN ACCOUNT
    8.  DISPLAY ACCOUNT
    9.  WRITE TO TXT FILE
    10. EXIT
    Select Your Option (1-10)
    """)

#selector
    ch = input("Choose an Option:")

    if ch == '1':
        nextAccNo = str(len(bankApp.accountDict)+1)
        bank.createAccount()
        bank.eraseText()
        bank.writeAccounts()
    elif ch =='2':
        num = input("Enter Account Number:")
        bank.accountDict[num].deposit()
        bank.eraseText()
        bank.writeAccounts()
    elif ch == '3':
        num = input("Enter Account Number:")
        bank.accountDict[num].withdrawal()
        bank.eraseText()
        bank.writeAccounts()
    elif ch == '4':
        num = input("Enter Account Number")
        print("Account Number:", num, "\nAccount Balance:", bank.accountDict[num].getBalance())
    elif ch == '5':
        bank.displayAccounts()
    elif ch == '6':
         num = input("Enter Account Number:")
         bank.accountDict[num].closeAccount()
    elif ch == '7':
        num = input("Enter Account Number:")
        print("Account Number:", num, "\nAccount Holder First Name:", bank.accountDict[num].getFirstName(),"\nAccount Holder Surname:",bank.accountDict[num].getSurname(), "\nAccount Balance:", bank.accountDict[num].getBalance(),"\nAccount Status:", bank.accountDict[num].getAccStatus())
        print( "Account Number:", num, bank.accountDict[num].setFirstName(),bank.accountDict[num].setSurname(), bank.accountDict[num].setBalance(), bank.accountDict[num].setAccStatus())
        print("Account Number:", num, "\nAccount Holder First Name:", bank.accountDict[num].getFirstName(),"\nAccount Holder Surname:",bank.accountDict[num].getSurname(), "\nAccount Balance:", bank.accountDict[num].getBalance(),"\nAccount Status:", bank.accountDict[num].getAccStatus())
    elif ch == '8':
        num = input("Enter Account Number")
        print("Account Number:", num, "\nAccount Holder First Name:", bank.accountDict[num].getFirstName(),"\nAccount Holder Surname:",bank.accountDict[num].getSurname(), "\nAccount Balance:", bank.accountDict[num].getBalance(),"\nAccount Status:", bank.accountDict[num].getAccStatus())
    elif ch == '9':
        bank.eraseText()
        bank.writeAccounts()
        print("\tAccounts written to txt file")
    elif ch == '10':
        print("\tThanks for using bank management system")
        break
    else :
        print("Invalid choice")

