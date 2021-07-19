#Add labels
#Add write/save data to txt file (formatting issue when writing)
#Add backup/archive file
#Test
#write to text file function temporary for testing.

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
        self.bal = self.bal + int(input("Enter Deposit Amount:"))
    def withdrawal(self):
        self.bal = self.bal - int(input("Enter Withdrawal Amount:"))

#close account
    def closeAccount(self):
        if self.bal == 0:
            self.aSt = 'closed'
            print('Account closed')
        else:
            print ('To close an account balance must be 0')


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

    def displayAccounts(self):
        for account in bank.accountDict:
            print(self.accountDict[account].getAccNo(), self.accountDict[account].getFirstName(), self.accountDict[account].getSurname(), self.accountDict[account].getBalance(), self.accountDict[account].getAccStatus() )

    def writeAccounts(self):
        for account in bank.accountDict:
            g = 0
            x = [self.accountDict[account].getAccNo(),",",self.accountDict[account].getFirstName(),",",self.accountDict[account].getSurname(),",",str(self.accountDict[account].getBalance()),",",self.accountDict[account].getAccStatus()]
            #f = open('prime.txt', 'w').close()
            f = open('prime.txt', 'a')
            f.writelines(x)







bank=bankApp()
bank.importAcc()




nextAccNo = str(len(bankApp.accountDict)+1)





#Choices
ch=''
num=""


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

    ch = input("Choose an Option:")

    if ch == '1':
        bank.createAccount()
    elif ch =='2':
       num = input("Enter Account Number:")
       print(bank.accountDict[num].deposit())
    elif ch == '3':
       num = input("Enter Account Number:")
       print(bank.accountDict[num].withdrawal())
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
        bank.writeAccounts()
        print("\tAccounts written to txt file")
        break
    elif ch == '10':
        print("\tThanks for using bank management system")
        break
    else :
        print("Invalid choice")


         #num = int(input("\tEnter The account No. : "))
       # modifyAccount(num)
