class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
       
        for crs, pre in prerequisites:
            courses[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if courses[crs] == []:
                return True
            visit.add(crs)

            for i in courses[crs]:
                if not dfs(i):
                    return False
            visit.remove(crs)
            courses[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True