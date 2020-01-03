from typing import List


# Runtime: 48 ms, faster than 44.36% of Python3 online submissions for Distance Between Bus Stops.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Distance Between Bus Stops.
class Solution:

    def bus_trip(self, idx: int, target_idx: int, distances: List[int], direction: int):
        max_index = len(distances) - 1
        current_idx = idx
        count = 0
        while True:
            if current_idx == target_idx:
                break
            count += distances[current_idx]
            if current_idx + direction > max_index:
                current_idx = 0
            elif current_idx + direction < 0:
                current_idx = max_index
            else:
                current_idx += direction
        if direction == -1:
            count -= distances[idx]
            count += distances[target_idx]
        return count

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        one = self.bus_trip(start, destination, distance, 1)
        two = self.bus_trip(start, destination, distance, -1)
        return min(one, two)


if __name__ == '__main__':
    s = Solution()
    res = s.distanceBetweenBusStops([1,2,3,4], 0, 3)
    print(res)