from faker import Faker
fake = Faker()

class BusinessCard:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email

    def __str__(self):
        return f'{self.first_name}, {self.last_name},{self.company}, {self.job}, {self.email}'

    def __repr__(self):
        return 'BusinessCard(first_name: %s, last_name: %s, company: %s, job: %s, email: %s, phone_number: %s)' % (
            self.first_name, self.last_name, self.company, self.job, self.email, self.phone_number)

class BaseContact(BusinessCard):
    def __init__(self, phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_number = phone_number
  
    def __str__(self):
        return 'first_name : {}, last_name : {}, company {}, job : {}, email :{}, phone_number : {}'\
            .format(self.first_name, self.last_name, self.company, self.job, self.email, self.phone_number)

#Zakomentowałem funkcje label_lenght, wydaje mi się, że jest prawidłowo napisana ale oczywiście 
# mam problem: 'function' object has no attribute 'first_name'
    
    #def label_length_base(self):
     #   lenght = lambda base : sum(len(int({self.first_name}, {self.last_name}))) 
      #  return lenght
    
    #@label_length_base
    def contact(self):
        return f"Wybieram prywatny numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}."

class BusinessContact(BaseContact):
    def __init__(self,phone_job, *args, **kwargs):
        super().__init__(phone_job, *args, **kwargs)
        self.phone_number = phone_job

    def contact(self):
        return f"Wybieram prywatny numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}."
    
    def label_length_business(self):
        lenght = lambda BusinessContact : sum(len(f'{self.first_name}, {self.last_name}'))
        return lenght 

#Funkcje drukowania list wizytówek
base_contact_list =[]
def base(copies):
    for contact in range (copies):
        contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            phone_number=fake.phone_number(),
            email=fake.email()
        )
        base_contact_list.append(contact)
        print((contact))
        print(contact.contact())
        return base_contact_list
        contact ()

business_contact_list = []
def business(copies):
    for contact in range (copies):
        contact = BusinessContact (
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            phone_job=fake.phone_number(),
            email=fake.email(),
        )
        business_contact_list.append(contact)
        print(contact)
        print(contact.contact)
        return business_contact_list
        contact()

def create_contact():
    type = input("Jakiego rodzaju chcesz wizytówki? 1 = Business, 2 = Bazowe")
    copies = int(input("Ile chcesz wizytówek?:"))
    if type == "1":
        business(copies)
        return copies 
    elif type == "2":
        base(copies)
        return copies 
    else:
        print("error")

#Program
if __name__ == "__main__":
    print("Hello")
    print("Print >>>a<<< to create new contact cards: ")

    choice = input("Enter your choice: ")

while True:
    if choice == "a":
        create_contact()
        continue

    else:
        error = "error"
        print(error)
        exit()
