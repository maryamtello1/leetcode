def fib(num):
    #base case
    if num==1:
        return 1
    if num==0:
        return 0 
    #recursive call
    return fib(num-1)+fib(num-2)


# recursion tree for fibonacci
#    fib(5)
#    /   \
# fib(4)  fib(3)
#  / \      / \
# fib(3)  fib(2) fib(2) fib(1)
#  / \
# fib(2) fib(1)