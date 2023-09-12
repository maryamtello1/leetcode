def factorial(num):
    #base case
    if num==1:
        return 1
    #recursive call
    return num*factorial(num-1)

print(factorial(4))

# factorial recursion tree:
#            4!
#          /   \
#        3!     * 4
#       /  \   
#     2!    * 3
#    /  \
#  1!    * 2
#   |
#  1