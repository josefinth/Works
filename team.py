# register and administrate handball teams for a handball event. This program
# will keep track of all the teams that a user of the program creates and administers
#  Every team in the program shall be represented as an object, an instance,
# of the class ”Team”

from datetime import date
import random
class Team:
 
    # A constructor for the class team. This method is called every time an object is
    # created. Helps to initialize the objects attibute when needed.
    
    
    def __init__(self, name:str, type_:str, fee_paid:bool, fee:int):

            
        date_ = date.today()      # Use the current date. Is the comma sign useful?
        a=1
        b=1000000
        id_= random.randint(a, b)       # This id can potentially be repeated but since we 
        self.__id_=id_                  # generate from 1 000 000 numbers it´s highly unlikely.
        self.__date_ = date_         
        self.fee = fee
        self.name = name
        self.type_ = type_
        self.fee_paid = fee_paid
        self.cancellation = "Active"    # "Active" is used as a defult value


    # Accessor methods
    
    def get_name(self):
        return self.name

    def get_type_(self):
        return self.type_

    def get_fee_paid(self):
        return self.fee_paid

    def get_id(self):
        return self.__id_

    def get_date(self):
        return self.__date_

    def get_fee(self):
        return self.fee

    def get_cancellation(self):
        return self.cancellation


    # Mutator methods
    
    def set_name(self, name):
        self.name = name

    def set_type_(self, type_):
        self.type_ = type_

    def set_fee_paid(self, fee_paid):
        self.fee_paid = fee_paid

    def set_fee(self, fee):
        self.fee = fee

    def set_cancellation(self, cancellation):
        self.cancellation = cancellation


# A method the class user_interaface call to create an object. The method also
# add the object to a list called teams. 

def create_team(name, type_, fee_paid, fee):
    team = Team(name, type_, fee_paid, fee)
    return(team)
  
    

