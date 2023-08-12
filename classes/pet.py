class PetPost:
    def __init__(self,petName:str,petType:str,age:int,color:str,city:str,available = True,postId =0) -> None:
        self.__postId = postId
        self.__petName = petName
        self.__petType = petType
        self.__age = age
        self.__color = color
        self.__city = city
        self.__available = available
    def setId(self,postId:int):
        if isinstance(postId, int):
            self.__postId = postId
        else:
            raise ValueError("please input valid username")
        return
    def setPetName(self,petName:str):
        if isinstance(petName, str):
            self.__petName = petName
        else:
            raise ValueError("please input valid name")
        return
    def setPetType(self,petType:str):
        if isinstance(petType, str):
            self.__petType = petType
        else:
            raise ValueError("please input valid type")
        return
    def setAge(self,age:int):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("please input valid age")
        return
    def setColor(self,color:str):
        if isinstance(color, str):
            self.__color = color
        else:
            raise ValueError("please input valid color")
        return
    def setCity(self,city:str):
        if isinstance(city, str):
            self.__city = city
        else:
            raise ValueError("please input valid city")
        return
    def setAvailable(self,available:bool):
        if isinstance(available, bool):
            self.__available = available
        else:
            raise ValueError("please input true or false") 
        return
    def getPostId(self):
        return self.__postId
    def getPetName(self):
        return self.__petName
    def getPetType(self):
        return self.__petType
    def getAge(self):
        return self.__age
    def getColor(self):
        return self.__color
    def getCity(self):
        return self.__city
    def getavailable(self):
        return self.__available
