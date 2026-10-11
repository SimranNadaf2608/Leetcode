class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        ans = []
        while top<=bottom and left<= right:
            # Collect the current top row from left to right.
            for col in range(left, right+1):
                ans.append(matrix[top][col])
            top += 1

            # Collect the current right column from top to bottom.
            for row in range(top, bottom+1):
                ans.append(matrix[row][right])
            right -= 1

            # A bottom row remains only if the top boundary has not crossed it.
            if top <= bottom :
                # Collect the current bottom row from right to left.
                for col in range(right, left-1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1

            if left<=right:
                # Collect the current left column from bottom to top.
                for row in range(bottom, top-1, -1):
                    ans.append(matrix[row][left])
                left += 1
        return ans