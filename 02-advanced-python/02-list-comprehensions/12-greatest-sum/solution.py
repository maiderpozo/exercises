def greatest_sum(ns):
    def slice_sum(pair):
        i, j = pair
        return sum(ns[i:j])

    return max( [ (i, j) for i in range(0, len(ns)) for j in range(i + 1, len(ns) + 1) ], key=slice_sum )

def miniMaxSum(arr):
  arr_sorted = sorted(arr)
  return sum(arr_sorted[:4]), sum(arr_sorted[-4:])

  

print(miniMaxSum([1,2,3,4,5]))
print(greatest_sum([1,2,3,4,5]))
