class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone_number : ", self.phone_number)
        print("e_mail :", self.email)
        print("add : ", self.addr)


def set_contact():
    name = input("NAME: ")
    phone_number = input("Phonenumber: ")
    e_mail = input("email: ")
    addr = input("addr: ")
    print(name,phone_number,e_mail,addr)

set_contact()
