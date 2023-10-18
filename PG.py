class Parking_Garage():

    def __init__(self, current_ticket = {}, tickets = 50, spaces = 50):
        self.spaces = spaces
        self.current_ticket = current_ticket
        self.tickets = tickets
        
# takeTicket method takes in a license # from the user, and stores the # in the 
# current_ticket dictionary as a key-value pair.  This is used again later to pay
# for parking and to exit the parking garage.

    def takeTicket(self):
        ticket = input("Enter your license plate to take a ticket and proceed to park: ")
        if self.spaces > 0:
            self.current_ticket[ticket] = 'active'
            self.spaces -= 1
            print(self.current_ticket)
            print('please proceed to parking')
            return
        else:
            print("\nSorry, no parking spaces available at this time. ")
            return
        
# payForParking once again takes the license # from the user, locates it in the
# dictionary, and asks for paymment.  If the input isn't found in the dictionary,
# the user is asked to re-enter the license #.
# once the user confirms payment, current_ticket is changed to paid, and the user 
# can now exit the garage.
        
    def payForParking(self):
        license = input("Enter your license plate to pay for parking: ")
        if license not in self.current_ticket:
            print("Try again: ")
            return 
        
        current = input("please type 'paid' once you have made payment: ")
        if current.lower() == 'paid':
            self.current_ticket[license] = 'paid'
            self.spaces += 1
            print("Thank you. Proceed to exit. ")
        else:
            print("Please complete payment. ")
            return
        
    def leaveGarage(self):
        
        for license, value in self.current_ticket.items():
            response = input("\nEnter your license plate number: ")
            if response == license and value == 'paid':
                print("\nPlease exit the garage. ")
                break
            if response != license:
                print("\nEnter a valid license # ")
            if response == license and value == 'active':
                print("\nPayment required before exiting. ")
            else:
                return("\nPlease enter a valid license #: \n")
        
park = Parking_Garage()

def Run():
    print("Welcome to the Python Garage.")
    while True:
        response = input("Enter 1 to park, 2 to pay, 3 to exit garage: ")
        if response.lower() == '1':
            park.takeTicket()
        elif response.lower() == '2':
            park.payForParking()
        elif response.lower() == '3':
            park.leaveGarage()
        else:
            print("Please enter a valid response. ")
        
Run()
