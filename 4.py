a = open('in.pdb', 'r')
lines = a.readlines()
a.close()
res = 0
for i in lines:
    i = i.strip()
    if i.startswith('HETATM'):
        if i.split()[3] == 'HOH':
            res += 1
f = open('out.txt', 'w')
f.write(str(res))
f.close()
