class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtrack(start, curr_ip, parts):
            if len(curr_ip) == 4:
                if start == len(s):
                    res.append(".".join(curr_ip))
                return

            if start == len(s):
                return
            
            if (4 - parts) * 3 < len(s) - start or (4 - parts) > len(s) - start:
                return
            
            for i in range(1, 4):
                if start + i > len(s):
                    break
                if i > 1 and s[start] == '0':
                    break
                if int(s[start:start+i]) > 255:
                    break
                
                curr_ip.append(s[start:start+i])
                backtrack(start+i, curr_ip, parts+1)
                curr_ip.pop()
        
        res = []
        backtrack(0, [], 0)
        return res