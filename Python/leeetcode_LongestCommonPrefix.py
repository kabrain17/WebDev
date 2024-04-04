def longestCommonPrefix(strs):
    min_len = min(len(s) for s in strs)
    result_s = ""

    for i in range(0, min_len):
        temp_s = strs[0][i]
        for s in strs:
            if temp_s != s[i]:
                return result_s
        else:
            result_s += temp_s

    return result_s


strs = ["flower","flow","flight"]
a = longestCommonPrefix(strs)
print(a)