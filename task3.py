class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return [item for item in self.__dict__.values()].__repr__()


profile = Profile('Andrii', 'Hirniak', '88005553535', 'Ivano-Frankivsk', 'hirniak.andrii@gmail.com', '01.01.2077', 'xx', 'male')
print(profile)