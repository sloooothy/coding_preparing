class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for symb in tokens:
            if symb in ["+","-","*","/"]:
                num2=stack.pop()
                num1=stack.pop()
                
                if symb=="+":
                   stack.append(num1+num2) 
                elif symb=="-":
                   stack.append(num1-num2) 
                elif symb=="*":
                   stack.append(num1*num2) 
                elif symb=="/":
                   n3=num1/num2
                   n3=int(n3)
                   stack.append(n3)  
                   
            else:
                stack.append(int(symb))

            #print(stack)

        return stack[0]
