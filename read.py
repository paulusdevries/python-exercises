#dingen_file = open('files/dingen.txt')

#for line in dingen_file:
#    print(line.rstrip())

#dingen_file.seek(0)
#lines = dingen_file.readlines()
#print(lines)


def sequence_filter(line):
    return '>' not in line

with open('files/dingen.txt') as bestand:
    lines = bestand.readlines()
    print(list(filter(sequence_filter, lines)))
