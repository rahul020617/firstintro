n = int(input("enter value upto which even cube is required : "))
def mylist(n):
    ls_cube = [i * i * i for i in range(0,n,2)]
    return ls_cube

print(mylist(n))