class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt = {}

        for j in nums2:
            while stack and stack[-1] < j:
                nxt[stack.pop()] = j
            stack.append(j)
        
        return [nxt.get(x, -1) for x in nums1]