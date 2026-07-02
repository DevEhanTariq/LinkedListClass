from _testcapi import error, MyList


class LinkedList:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next

    def append(self, LinkedList: object):
        nextList = self
        while nextList.next != None:
            nextList = nextList.next
        nextList.next = LinkedList

    def replace(self, index: int, LinkedList: object):
        if index == 0:
            LinkedList.next = self.next

        else:
            try:
                nextList = self
                for i in range(index + 1):
                    nextList = nextList.next
                if nextList != None:
                    LinkedList.next = nextList

                nextList = self
                for i in range(index - 1):
                    nextList = nextList.next
                nextList.next = LinkedList
            except:
                print("LinkedList index out of range")


    def show(self):
        nextList = self
        print("[", end="")
        while nextList.next != None:
            print(nextList.value, end=" -> ")
            nextList = nextList.next
        print(nextList.value, end="]\n")

    def list(self):
        list = []
        nextList = self
        while nextList.next != None:
            list.append(nextList.value)
            nextList = nextList.next
        list.append(nextList.value)
        return list


if __name__ == '__main__':
    MyList = LinkedList(0)
    for i in range(5):
        MyList.append(LinkedList(i+1))
    MyList.show()
    print(MyList.list())
    MyList.replace(2, LinkedList("HEY"))
    MyList.show()