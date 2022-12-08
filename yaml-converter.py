import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--comments', help='include comments', action='store_true')

args = parser.parse_args()

print(args)

current = []
with open('yaml-in.txt', 'r') as file:
    for line in file:
        line = line.rstrip().replace('    ', '\t').split('\t')
        if len(line) == 1:
            if '#' in line[0] and args.comments:
                print('\n' + line[0])
            else:
                current = line

        else:
            current = current[:len(line) - 1]
            current.append(line[-1])
            if ': ' in '.'.join(current).replace(':.', '.'):
                print('.'.join(current).replace(':.', '.'))