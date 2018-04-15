def permute_array(A, right):
    if right == len(A):
        print(A)
        return
    # print(A) 
    index = right
    for i in range(right+1):
        num = A.pop(index)
        A.insert(i, num)
        index = i
        permute_array(A, right+1)

if __name__ == '__main__':
    A = [1,2,3]
    permute_array(A, 0)