class priorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def pop(self):
        self.queue.sort()
        return self.queue.pop(0)

    def decreaseKey(self, key, weight):
        have = 0
        for i in self.queue:
            if key in i:
                have = 1

        if have == 0:
            return None
                
        for i in self.queue:
            if key == i[1]:
                self.queue.remove(i)
                break
        self.queue.append((weight,key))