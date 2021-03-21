change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

for c in change:
    string = string.replace(c, '1')
print(len(string))