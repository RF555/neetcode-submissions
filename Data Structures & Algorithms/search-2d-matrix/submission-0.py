class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = (m * n) - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_m, mid_n = self.m_n_remain(m, mid)
            if matrix[mid_n][mid_m] == target:
                return True
            elif matrix[mid_n][mid_m] < target:
                l = mid + 1
            else:
                r = mid -1
        return False

    def m_n_remain(self, x: int, val: int) -> tuple(int, int):
        m = val % x
        n = val // x

        return (m, n)