class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        cnt = [0] * k
        time_set = {}
        
        for id, minutes in logs:
            if id not in time_set:
                time_set[id] = [minutes]
            elif id in time_set and minutes not in time_set[id]:
                time_set[id].append(minutes)
        
        for id, minutes in time_set.items():
            cnt[len(minutes) - 1] += 1
        return cnt