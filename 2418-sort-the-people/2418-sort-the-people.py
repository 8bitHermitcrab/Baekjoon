class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]
        people = sorted(people.items(), reverse=True)
        ans = [i[1] for i in people]
        return ans