import datetime
today = datetime.date.today()
year = today.year
class Student:

    def __init__(self,id,name,dob,clas,age,reg):
      self.__id = id
      self.__name = name
      self.__dob = dob
      self.__clas = clas
      self.__age = 0
      self.__reg = ''

    def calc_current_age(self):
        date = self.__dob.split('/')
        d_year = int(date[2])
        self.__age = year - d_year

    def reg_time(self):
       if self.__clas == 'Senior':
          self.__reg = 'registration is avaiable from 4/1 to 4/3'
       elif self.__clas == 'Junior':
          self.__reg = 'registration is avaiable from 4/4 to 4/6'
       elif self.__clas == 'Sophomore':
          self.__reg = 'registration is avaiable from 4/7 to 4/9'
       else:
          self.__reg = 'registration is avaiable from 4/10 to 4/12'
    
    def get_time(self):
       return self.__reg
    
    def get_age(self):
       return self.__age
          
