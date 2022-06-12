def nth_longest_string(n, strings):
    return sorted(strings, key=len)[-n]



print(nth_longest_string(1, [ 'appppppppppppp', 'bb', 'ccc', 'ddddoooo','oleej' ]))