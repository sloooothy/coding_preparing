class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}

        for course, preq in prerequisites:
            preMap[course].append(preq)

        #visiting and visited set
        visiting=set()
        chkOKcourse=set()

        def dfs(course):
            if course in visiting:
                return False
            if course in chkOKcourse: #pre-checked path
                return True
            visiting.add(course)

            for preq_crs in preMap[course]:
                if not dfs(preq_crs):
                    return False
            visiting.remove(course) # remove current check path from course
            chkOKcourse.add(course)#add to ok list set
            return True

 
        for course in range(numCourses):
            if not dfs(course):
                return False 

            
        return True
