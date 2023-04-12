

class Person:
    def getPersonData(self):
        self.firstname = input("Please enter your first name ")
        #print("Your first name is",self.firstname)

        self.surname = input("Please enter your surname ")
       # print("Your surname name is",self.surname)
       # print("Your full name is",self.firstname,self.surname)

        self.id = input("Please enter your Staff ID ")
       # print("Your Staff ID is",self.id)

        self.email = input("Please enter your email address ")
       # print("Your email address is",self.email)

        self.issue = input("Please enter enter a description of your issue ")
      #  print("Your issue has been registered",self.issue)


        
    def printPerson(self):
        print("Your full name is",self.firstname,self.surname)
        print("Your Staff ID is",self.id)
        print("Your email address is",self.email)
        print("Your issue has been registered",self.issue)

def printstats(ticketlist):
    print("Total tickets are:", len(ticketlist))
    for ticket in ticketlist:
        ticket.printPerson()

p1= Person()

p1.getPersonData()

ticketlist=[]
ticketlist.append(p1)

printstats(ticketlist)

   





