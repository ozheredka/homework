class Stack:
    def __init__(self):
        self.array = []

    def push(self, item): # положить элемент в стек
        self.array.append(item)

    def pop(self): # удалить элемент из стека и вернуть его значение
        if self.array.isEmpty:
            return "none"
        else:
            return self.array.pop()

    def peek(self): # вернуть значение последнего элемента стека (не удаляя его)
        return self.array[len(self.array)-1]

    def isEmpty(self): # вернуть True, если стек пуст, иначе вернуть False
        if len(self.array) == 0:
            return True
        else:
            return False

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def isEmpty1(self):
        if len(self.stack1) == 0:
            return True
        else:
            return False

    def isEmpty2(self):
        if len(self.stack2) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.stack1.isEmpty1 and self.stack2.isEmpty2:
            self.stack1.append(item)

    def dequeue(self):
        if self.stack2.isEmpty2():
            if self.stack1.isEmpty1:
                return 'None'
            else:
                while not self.stack1.isEmpty1:
                    self.stack1.pop()
                    self.stack2.append(item)
        return self.stack2.pop()

s = MyQueue()
n = 1
for n in range(10):
    s.enqueue(n)
    n+=1

s.dequeue()
print (s)