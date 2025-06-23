# Problem 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        myq = deque()
        myq.append(root)
        if root== None:
            return res

        while myq:
            mylst = []
            for i in range(len(myq)):
                elem = myq.popleft()
                mylst.append(elem.val)
                if elem.left:
                    myq.append(elem.left)
                if elem.right:
                    myq.append(elem.right)
            res.append(mylst)
        return res



# Problem 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        indegree = defaultdict(int)

        for dep, indep in prerequisites:

            adj_list[indep].append(dep)
            indegree[dep] +=1 
        
        myq = deque()

        for i in range(0, numCourses):
            if indegree[i] == 0:
                myq.append(i)
        done = 0
        
        while myq:
            done +=1 
            course = myq.popleft()

            for deps in adj_list[course]:
                indegree[deps] -=1
                if indegree[deps] == 0:
                    myq.append(deps)
        return done == numCourses
