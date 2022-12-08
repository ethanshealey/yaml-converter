current = []
with open('yaml-in.txt', 'r') as file:
    for line in file:
        line = line.rstrip().replace('    ', '\t').split('\t')
        if len(line) == 1:
             current = line
        else:
            current = current[:len(line) - 1]
            current.append(line[-1])
            if ': ' in '.'.join(current).replace(':.', '.'):
                print('.'.join(current).replace(':.', '.'))
