class Queue():
    def __init__(self):
        self.__list = []
    def put(self,val):
        self.__list.append(val)
        return self.__list
    def get(self):
        item = self.__list[0]
        del self.__list[0]
        return item
    def isempty(self):
        if len(self.__list) == 0:
            return True
        else:
            return False

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

print(que.__dict__)
print(que._Queue__list)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")