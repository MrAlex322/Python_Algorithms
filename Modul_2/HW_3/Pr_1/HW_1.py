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


class MyQueue:
    def __init__(self):
        self.stack1 = []  # стек для добавления элементов
        self.stack2 = []  # стек для удаления элементов

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.empty():
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.empty():
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

    def print_queue(self):
        if self.empty():
            print("Очередь пуста")
            return
        queue = self.stack2[::-1] + self.stack1
        print(queue)


queue_items = MyQueue()

queue_items.push(1)
queue_items.push(2)
queue_items.push(3)
queue_items.push(4)
queue_items.print_queue()
print(queue_items.pop())
queue_items.print_queue()
queue_items.push(44)
print(queue_items.pop())
queue_items.print_queue()
