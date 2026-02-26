class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
                if len(s1) != len(s2):
                    return False
                
                s_even = []
                s_odd = []
                t_even = []
                t_odd = []
                
                for i in range(len(s1)):
                    if i % 2 == 0:   
                        s_even.append(s1[i])
                        t_even.append(s2[i])
                    else:
                        s_odd.append(s1[i])
                        t_odd.append(s2[i])
                
                if sorted(s_even) == sorted(t_even) and sorted(s_odd) == sorted(t_odd):
                    return True
                else:
                    return False
        