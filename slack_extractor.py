import json
import sys
from collections import defaultdict


def read_lines(filename):
    with open(filename, 'r') as input:
        for line in input.readlines():
                yield (line)

def print_dict(dict_of_ditcs):
    s=''
    for key in dict_of_ditcs:
        s += '\t' + key + '\n'
        dd = sorted(dict_of_ditcs[key].items())
        for element in dd:
            s += element[0] + '\t' + str(element[1]) + '\n'
    print(s)

if __name__ == "__main__":
    results = defaultdict(lambda: defaultdict(int))
    this_time = 0
    for line in read_lines(sys.argv[1]):
        if line.startswith('bot'):
            this_time = line[9:14]
        elif line.startswith('ps-'):
            region = line[3:7]
            if '{' in line:
                results[region]['end'] = this_time
                analysis = json.loads(line[13:])
                for entry in analysis:
                    results[region][entry] += analysis[entry]
            else:
                results[region]['end'] = this_time
    print_dict(results)