from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = []
        
        if root == None:
            return 0
        
        q = deque()
        q.append((root,1))
        
        while q:
            cur_node, lv = q.popleft()
            level.append(lv)
            
            if cur_node.left:
                q.append((cur_node.left, lv+1))
            if cur_node.right:
                q.append((cur_node.right, lv+1))
        
        return max(level)