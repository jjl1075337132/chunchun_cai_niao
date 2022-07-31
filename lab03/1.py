def max_subseq(n, l):
    if n == 0 or l == 0:
        return 0
    with_lastdigit = max_subseq(n//10, l-1) * 10 + n%10
    no_lastdigit = max_subseq(n//10, l) # 这条路是n == 0时，return 0
    if with_lastdigit > no_lastdigit:
        return with_lastdigit
    else:
        return no_lastdigit

print(max_subseq(12345,3))
