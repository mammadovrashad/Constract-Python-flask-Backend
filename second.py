class User:
    def __init__(self,_name,_surname):
        self.Name=_name
        self.Surname=_surname
    def fullName(self):
        print(f'sizin adiniz: {self.Name} sizin soyadiniz:{self.Surname} ')