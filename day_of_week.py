class weeker:
    def __init__(self,day):
        self.__map = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
        self.day = day
    
    def __str__(self):
        return self.day
    
    def add_days(self,num):
        if num % 7 == 0:
            self.day = self.__map[6]
        else:
            self.day = self.__map[(num%7)-1]

    def subtract_days(self,num):
        if num % 8 == 0:
            self.day = self.__map[6]
        else:
            self.day = self.__map[(num%8)-1]

weekday = weeker('Mon')
print(weekday)
weekday.add_days(15)
print(weekday)
weekday.subtract_days(23)
print(weekday)