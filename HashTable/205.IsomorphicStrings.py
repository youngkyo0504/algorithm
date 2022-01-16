def isIsomorphic(s:str, t:str):
        isomorphic_dic_s={}
        isomorphic_dic_t={}
        number = 0
        for i in range(len(s)):
            if s[i] in isomorphic_dic_s or t[i] in isomorphic_dic_t:
                if not s[i] in isomorphic_dic_s or t[i] not in isomorphic_dic_t:
                    return False
                else:
                    if isomorphic_dic_s[s[i]] != isomorphic_dic_t[t[i]]:
                        return False
            else:
                isomorphic_dic_s[s[i]] = number
                isomorphic_dic_t[t[i]] = number
                number += 1
        return True

print(isIsomorphic("badc","baba"))



