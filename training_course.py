class TrainingCours:

    def __init__(self, name_cours, about ,date, time, location,available=True) -> None:
        self.name_course=name_cours
        self.date=date
        self.time=time
        self.location=location
        #self.available = available
        self.about=about


    def courses(self):
        #To display courses to the user and their time and date
        return f"{self.name_course} \nThe training course to learn the {self.about}\n\nDate:{self.date}\tTime:{self.time}\tCity:{self.location}\n"


infromation_list=[]
class Training:

    def __init__(self, name , phone_number, email) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email=email
        


def add(training:Training):
    infromation_list.append(training)
 