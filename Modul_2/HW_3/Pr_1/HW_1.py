# Реализуйте очередь (FIFO), используя только два стека. Реализованная очередь должна
# поддерживать все функции обычной очереди (push, peek, pop и empty).
#
# Реализуйте класс MyQueue:
#
# void push(int x) Помещает элемент x в конец очереди.
# int pop() Удаляет элемент из начала очереди и возвращает его.
# int peek() Возвращает элемент в начале очереди.
# boolean empty() Возвращает true, если очередь пуста, иначе false.
# Примечания:
#
# Нужно использовать только стандартные операции стека, что означает, что допустимы только операции push to top,
# peek/pop сверху, size и is empty.
# Можно использовать list для имитации стека
# Time Complexity = O(n), где n - количество элементов в стеке.
# Memory Complexity = O(n), где n - количество элементов в стеках self.stack1 и self.stack2.

class MyQueue:
    def __init__(self):
        self.stack_to_add = []  # стек для добавления элементов
        self.stack_to_remove = []  # стек для удаления элементов

    def push(self, x):
        self.stack_to_add.append(x)

    def pop(self):
        if self.empty():
            return None
        if not self.stack_to_remove:
            while self.stack_to_add:
                self.stack_to_remove.append(self.stack_to_add.pop())
        return self.stack_to_remove.pop()

    def peek(self):
        if self.empty():
            return None
        if not self.stack_to_remove:
            while self.stack_to_add:
                self.stack_to_remove.append(self.stack_to_add.pop())
        return self.stack_to_remove[-1]

    def empty(self):
        return not self.stack_to_add and not self.stack_to_remove


    def print_queue1(self):
        for item in self.stack_to_add:
            print(item)


    def print_queue(self):
        if self.empty():
            print("Очередь пуста")
            return
        queue = self.stack_to_remove[::-1] + self.stack_to_add
        print(queue)


queue = MyQueue()

queue.push(1)
queue.push(2)
queue.push(3)

queue.print_queue()  # [1, 2, 3]

queuer.print(q.peek())  # 1

queue.print_queue()  # [1, 2, 3]

print(queue.pop())   # 1
print(queue.pop())   # 2

queue.print_queue()  #3

print(queue.pop())   #3

queue.print_queue()  #Очередь пуста

print(queue.empty()) #True



