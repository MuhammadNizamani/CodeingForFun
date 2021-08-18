def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp
 
 
# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
 
    if curr_index == len(ch) - 1:
        print(''.join(ch))
 
    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)
 
 
if __name__ == '__main__':
 
    s = input("enter string ")
    num = int(input("enter number"))
    permutations(list(s), num)
 
