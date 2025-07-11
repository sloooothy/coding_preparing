class Solution:
    def isValid(self, s: str) -> bool:
        parentheses=[]

        for pt in s:
            if pt in ['(','{','[']:
                parentheses.append(pt)
            else:
                if len(parentheses)>0 and pt==")" and parentheses[-1]=="(":
                    parentheses.pop()
                elif len(parentheses)>0 and pt=="}" and parentheses[-1]=="{":
                    parentheses.pop()
                elif len(parentheses)>0 and pt=="]" and parentheses[-1]=="[":
                    parentheses.pop()
                else:
                    return False

        return len(parentheses)==0
