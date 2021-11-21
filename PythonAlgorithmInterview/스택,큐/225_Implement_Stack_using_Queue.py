class MyStack:

    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        # 방금 삽입한 요소를 맨 앞에 두는것으로 한다
        self.q.append(x)
        for _ in range(len(self.q) - 1) :
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if not self.q :
            return True
        else :
            return False