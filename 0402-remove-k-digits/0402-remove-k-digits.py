class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if n==k:
            return "0"
        kt=0
        i=1
        j=1
        st=[]
        st.append(num[0])
        while i<n:
            while len(st)!=0 and ord(num[i])<ord(st[j-1]) and kt<k:
                ss=st.pop()
                j-=1
                kt+=1
            st.append(num[i])
            j+=1
            i+=1
        i=0
        while i<len(st):
            if st[i]!="0":
                break
            i+=1
        ans=""
        while i<len(st)+kt-k:
            ans+=st[i]
            i+=1
        if len(ans)==0:
            return "0"
        return ans