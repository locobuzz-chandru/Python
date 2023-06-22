def subsequence(str1):
    if len(str1) == 0:
        return [""]
    small = subsequence(str1[1:len(str1)])
    result = [""] * (2 * len(small))
    k = 0
    for i in range(len(small)):
        result[k] = small[i]
        k += 1
    for i in range(len(small)):
        result[k] = str1[0] + small[i]
        k += 1
    return result


def isSubsequence(str1, str2):
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return True if i == len(str1) else False


def longest_increasing_subsequence(nums):
    lst = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lst[i] = max(lst[i], lst[j] + 1)
    return max(lst)


def longest_palindromic_subsequence(s):
    result = ""
    result_len = 0
    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > result_len:
                result = s[l:r + 1]
                result_len = r - l + 1
            l -= 1
            r += 1

        # even length
        # l, r = i, i + 1
        # while l >= 0 and r < len(s) and s[l] == s[r]:
        #     if (r - l + 1) > result_len:
        #         result = s[l:r + 1]
        #         result_len = r - l + 1
        #     l -= 1
        #     r += 1
    return result


if __name__ == '__main__':
    # print(subsequence("net"))
    # print(isSubsequence(str1="bdf", str2="ddddddfadcbadcdefg"))
    # print(longest_increasing_subsequence([0, 3, 1, 6, 2, 2, 7]))
    print(longest_palindromic_subsequence("abcdefed"))
