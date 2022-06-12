def frequencies(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result

# Using a lambda
def mode2(ns):
    return max(frequencies(ns).items(), key=lambda pair: pair[1])[0]

# Alternative
def second(pair):
    return pair[1]

def mode(ns):
    fs = frequencies(ns)
    return max(fs.items(), key=second)[0]

def mode3(ls):
    # dictionary to keep count of each value
    counts = {}
    # iterate through the list
    for item in ls:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    # get the keys with the max counts
    return [key for key in counts.keys() if counts[key] == max(counts.values())]

print(mode2([1, 2, 1, 3, 3, 3]))
print(mode3([1, 2, 1, 3, 3, 3]))
