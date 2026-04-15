class stack:
    def __init__(self):
        self.__container = []
    def pop(self):
        print('Popping:', self.__container[-1])
        del self.__container[-1]
        return self.__container
    def push(self,val):
        print('Pushing:', val)
        self.__container.append(val)
        return self.__container

class countingStack(stack):
    def __init__(self):
        super().__init__()
        self.__count = 0
    def countStack(self):
        return self.__count
    def pop(self):
        self.__count -= 1
        return stack.pop(self)
    def push(self,val):
        self.__count += 1
        return stack.push(self,val)

test1 = countingStack()
test2 = countingStack()

print('Test 1 -- Current List: ',test1.push(1))
print('Test 1 -- Current List: ',test1.push(2))
print('Test 1 -- Count:',test1.countStack())
print('Test 1 -- Current List: ',test1.pop())
print('Test 1 -- Count:',test1.countStack())

print('Test 2 -- Current List: ',test2.push(333))
print('Test 2 -- Count:',test2.countStack())
print('Test 2 -- Current List: ',test2.push(2))