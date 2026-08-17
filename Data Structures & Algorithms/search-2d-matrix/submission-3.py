class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                # if we reach a row where the first number is less than our target is the last number >  our target?
                # if last one is then we know were on the right row
                last_idx = len(matrix[m])-1
                l1 = 0
                if matrix[m][last_idx] == target:
                    return True
                elif matrix[m][last_idx] > target:
                    while l1 <= last_idx:
                        m1 = l1 + (last_idx - l1) // 2
                        if matrix[m][m1] == target:
                            return True
                        elif matrix[m][m1] > target:
                            last_idx = m1 - 1
                        else:
                            l1 = m1 + 1
                    return False
                else:
                    l = m + 1
            else:
                r = m - 1
        return False