import sys
def parse_line(line):
    return int(line)


def load_scores(lines):
    scores = [parse_line(line) for line in lines]
    return scores


try:
    res2 = load_scores(["gfhgfh", "324", "324"])
except:
    print('------ Error while parsing scores')
    sys.exit(1)


print("------- helloooooo")