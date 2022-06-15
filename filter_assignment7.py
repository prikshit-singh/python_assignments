def fun(variable):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (variable in vowels):
        return True
    else:
        return False
  
  
# sequence
letters = ['g', 'e', 'e', 'j', 'k','a', 's', 'p', 'r']
  
# using filter function
filtered = filter(fun, letters)
print(list(filtered))
print('The filtered letters are:')
for s in filtered:
    print(s)