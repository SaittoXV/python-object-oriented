def two_digit(val):
    digit = str(val)
    if len(digit) == 1:
        digit = '0' + digit
    return digit

class Timer:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return two_digit(self.hours) + ":" + two_digit(self.minutes) + ":" + two_digit(self.seconds)
    
    def next_second(self):
        if self.seconds + 1 >= 60:
            self.seconds = 0
            if self.minutes + 1 >= 60:
                self.minutes = 0
                if self.hours + 1 >= 24:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def prev_second(self):
        if self.seconds - 1 <= 0:
            self.seconds = 59
            if self.minutes - 1 <= 0:
                self.minutes = 59
                if self.hours - 1 <= 0:
                    self.hours = 23 
                else:
                    self.hours -= 1
            else:
                self.minutes -= 1
        else:
            self.seconds -= 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
timer.prev_second()
print(timer)