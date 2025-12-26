class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split('/')

        arr = []
        for s in pathArr:
            if not s:
                continue
            if s == '..':
                if arr:
                    arr.pop()
            elif s == '.':
                continue
            else:
                arr.append(s)

        return '/' + '/'.join(arr)


# result = Solution().simplifyPath('/home//foo/')
# result = Solution().simplifyPath('/home/user/Documents/../Pictures')
# result = Solution().simplifyPath('/../')
result = Solution().simplifyPath("/.../a/../b/c/../d/./")
print(result)
