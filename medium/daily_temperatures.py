from typing import List, Tuple


class SlowSolution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        results = []
        for i in range(len(T)):
            tmp = 0
            found = False
            for j in range(i, len(T)):
                if T[j] > T[i]:
                    found = True
                    break
                else:
                    tmp += 1
            tmp = tmp if found else 0
            results.append(tmp)
        return results


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        result: List[int] = [0] * len(T)

        for index, temperature in enumerate(T):
            while stack and stack[-1][0] < temperature:
                prev_index = stack[-1][1]
                diff = index - prev_index
                result[prev_index] = diff
                stack.pop()
            stack.append((temperature, index))
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(res)