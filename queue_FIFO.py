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

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")