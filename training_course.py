class TrainingCours:

    def __init__(self, name_cours, about ,date, time, location) -> None:
        self.name_course=name_cours
        self.date=date
        self.time=time
        self.location=location
        self.about=about


    def courses(self):
        #To display courses to the user and their time and date
        return f"{self.name_course} \n\n The training course to learn the {self.about}\n\n Date: {self.date}\tTime: {self.time}\tCity: {self.location}\n"


    def __eq__(self, __value: object) -> bool:
        return self.name_course == __value

infromation_list=[]
class Training():

    def __init__(self, name , phone_number, email) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email=email
        


def add(training:Training):
    infromation_list.append(training)

