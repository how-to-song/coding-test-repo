class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        tuple_list = []
        for i in range(n):
            tuple_list.append((names[i], heights[i]))

        tuple_list.sort(key=lambda x: x[1], reverse = True)


        return [tuple_list[i][0] for i in range(n)]
            
            
