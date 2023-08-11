class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            self._transfer_elements()
        if self.stack_dequeue:
            return self.stack_dequeue.pop()

    def peek(self):
        if not self.stack_dequeue:
            self._transfer_elements()
        if self.stack_dequeue:
            return self.stack_dequeue[-1]

    def _transfer_elements(self):
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

if __name__ == "__main__":
    num_queries = int(input())
    queue = QueueUsingTwoStacks()

    for _ in range(num_queries):
        query = input().split()

        if query[0] == "1":
            queue.enqueue(int(query[1]))
        elif query[0] == "2":
            queue.dequeue()
        elif query[0] == "3":
            front_element = queue.peek()
            if front_element is not None:
                print(front_element)
