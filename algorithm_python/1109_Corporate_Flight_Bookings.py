class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        # build difference array
        diff = [0] * (n + 1)

        # repeatedly add value
        for booking in bookings:
            diff[booking[0]-1] += booking[2]
            diff[booking[1]] -= booking[2]

        # rebuild original array
        presum = [diff[0]]
        for i in range(1, n):
            presum.append(presum[-1] + diff[i])

        return presum