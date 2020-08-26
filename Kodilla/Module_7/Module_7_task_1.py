from faker import Faker

fake = Faker()

class BusinessCard:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email

    @property
    def label_lenght(self):
        return len(f"{self.first_name}, {self.last_name}")

    @property
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
        return 'first_name : {}, last_name : {}, company {}, job : {}, email :{}, phone_number : {}' \
            .format(self.first_name, self.last_name, self.company, self.job, self.email, self.phone_number)

    def contact(self):
        return f"Wybieram prywatny numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}."


class BusinessContact(BaseContact):
    def __init__(self, phone_job, *args, **kwargs):
        super().__init__(phone_job, *args, **kwargs)
        self.phone_number = phone_job

    def contact(self):
        return f"Wybieram prywatny numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}."


# Funkcje drukowania list wizytówek

def base(copies):
    base_contact_list = []
    for contact in range(copies):
        contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            phone_number=fake.phone_number(),
            email=fake.email()
        )
        base_contact_list.append(contact)
    return base_contact_list


def business(copies):
    business_contact_list = []
    for contact in range(copies):
        contact = BusinessContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            company=fake.company(),
            job=fake.job(),
            phone_job=fake.phone_number(),
            email=fake.email(),
        )
        business_contact_list.append(contact)

    return business_contact_list

def create_contact():
    type = input("Jakiego rodzaju chcesz wizytówki? 1 = Business, 2 = Bazowe: ")
    copies = int(input("Ile chcesz wizytówek?: "))
    if type == "1":
        contacts = business(copies)
        print(business(copies))
        print(len(contacts))

    elif type == "2":
        contacts =  base(copies)
        print(base(copies))
        print(len(contacts))

    else:
        error = "error"
        print(error)
        exit()


# Program
if __name__ == "__main__":
    print("Hello")
    print("Print Y/N to create new contact cards: ")

    choice = input("Enter your choice: ")

while True:
    if choice == "Y" or "y":
        create_contact()
        continue

    else:
        error = "error"
        print(error)
        exit()
