class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        dic = {}
        for num1 in arr1:
            if num1 in dic:
                dic[num1] += 1
            else:
                dic[num1] = 1
        
        for num2 in arr2:
            for _ in range(dic.pop(num2)):
                ans.append(num2)

        keys = list(dic.keys())
        keys.sort()

        for key in keys:
            ans += [key] * dic[key]

        return ans