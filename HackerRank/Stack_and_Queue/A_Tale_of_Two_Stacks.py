class MyQueue(object):
    def __init__(self):
        self.queue = []
    
    # 큐의 0번째 원소 출력
    def peek(self):
        return self.queue[0]
    
    # 큐에서 제거
    def pop(self):
        return self.queue.pop(0)
        
    # 큐에 삽입
    def put(self, value):
        self.queue.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    # 1 : 큐에 삽입
    if values[0] == 1:
        queue.put(values[1])
    # 2 : 큐에서 제거        
    elif values[0] == 2:
        queue.pop()
    # 3 : 큐의 0번째 원소 출력
    else:
        print(queue.peek())