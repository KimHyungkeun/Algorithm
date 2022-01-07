class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 유클리드 거리를 기준으로 원점과 좌표간의 거리가 가까운 순서대로 k번째까지 출력한다
        points.sort(key = lambda x : (x[0]**2 + x[1]**2)**0.5)
        points = points[:k]
        return points