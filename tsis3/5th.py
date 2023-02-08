import itertools
 
if __name__ == '__main__':
    s = 'ABC'
 
    nums = list(s)
    permutations = list(itertools.permutations(nums))
 
    print([''.join(permutation) for permutation in permutations])
 
