class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            pre = strs[0]
            for word in strs[1:]:
                for i in range(len(pre)):
                    if i > len(word) - 1 or pre[i] != word[i]:
                        pre = pre[:i]
                        break
        else:
            pre = ''
        return pre


#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
#         return strs[0][:r.index(0)] if strs else ''


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         r = [len(set(c)) == 1 for c in zip(*strs)]
#         return strs[0][:r.index(False)] if strs else ''
