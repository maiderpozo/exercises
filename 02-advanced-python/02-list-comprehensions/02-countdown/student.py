# Write your code here
def countdown(n):
    return ",".join(str(number) for number in range(n,0,-1))
    

print(countdown(10))