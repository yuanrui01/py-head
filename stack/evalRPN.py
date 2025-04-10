from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opSet = {'+', '-', '*', '/'}
        st = []
        for c in tokens:
            if c in  opSet:
                p1 = st.pop()
                p2 = st.pop()
                if c == '+':
                    st.append(p2 + p1)
                elif c == '-':
                    st.append(p2 - p1)
                elif c == '*':
                    st.append(p2 * p1)
                else:
                    st.append(int(p2 / p1))
            else:
                st.append(int(c))
        return st.pop()
        

soluction = Solution()
tokens = ["2","1","+","3","*"]
soluction.evalRPN(tokens)