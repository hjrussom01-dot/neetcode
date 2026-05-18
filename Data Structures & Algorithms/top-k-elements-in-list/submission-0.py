import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
                if num in freqs:
                        freqs[num] += 1
                else:
                        freqs[num] = 1

        heap = []
        for val, freq in freqs.items():
                heapq.heappush(heap, [freq, val])
                if len(heap) > k:
                        heapq.heappop(heap)
        fin  = []
        for freq, val in heap:
                fin.append(val)

        return fin