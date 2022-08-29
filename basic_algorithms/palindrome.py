def palindrome(string):
    reverse_str = string[:][::-1]
    if string == reverse_str:
        return True
    else:
        return False


"""
rotator
1. r o t a t o r
2. r otato r
3. r o tat o r
"""


def partitioned_palindrome(string, initial_index, result, temp):  # k=0 e=1 e=2 p=3 s=4
    tmp_str = ''
    current_list = temp[:]  # [k]
    for i in range(initial_index, len(string)):  # 1, 4
        tmp_str = tmp_str + string[i]  # ''+k+e
        if palindrome(tmp_str):
            temp.append(tmp_str)  # [k e e  p s]
            if i + 1 < len(string):  # 1<5
                partitioned_palindrome(string, i + 1, result, temp[:])  # partitioned_palindrome("keeps", 1, result,
                # [k])
            else:
                result.append(temp)
            temp = current_list


if __name__ == "__main__":
    string = str(input("Enter the string:").strip()).lower()
    str_length = len(string)
    temp = []
    result = []
    partitioned_palindrome(string, 0, result, temp)

    for i in result:
        word = ''.join(i)
        if len(word) == str_length:
            print(*i, sep=' ')
