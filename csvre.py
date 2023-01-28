import sys
import os

"""
specification

a,b,c,d -> d,c,b,a                  # reverse order of columns
a_c -> ac                           # drop middle column
a,b,c -> "static info",a,b,c        # insert extra string in first column

tyler weston 2023

"""

def main():
    print("csvre")
    # TODO: add remove header flag
    # get in file, out file, pattern in, pattern out
    if len(sys.argv) != 5:
        print("python main.py infile outfile inpattern outpattern")
        exit()

    _, infilename, outfilename, inpattern, outpattern = sys.argv
    # TODO: confirm valid pattern, right now this will vaguely throw an error if
    # a key from the input pattern isn't in the output pattern

    if not os.path.exists(infilename):
        print("cannot find input file")
        exit()
    infile = open(infilename)

    if os.path.exists(outfilename):
        # print(f"this will remove file {outfilename}, are you sure? type 'y'")
        confirm = input(f"this will overwrite file {outfilename}, are you sure? type 'y': ")
        if confirm != 'y':
            exit()
        os.remove(outfilename)
    outfile = open(outfilename, "x")    # x = create a file if it doesn't exist

    line = infile.readline().rstrip()

    # make sure length of line matches inpattern
    columnlength = len(line.split(','))
    inlength =  len(inpattern.split(','))
    if columnlength != inlength:
        print("inpattern must have same number of chars as csv columns")
        exit()

    mapping = make_mapping(inpattern, outpattern)

    output_length = len(outpattern.split(','))
    strings = get_strings(outpattern)

    while line != "":
        res = parse_line(line, mapping, output_length)
        if strings is not False:
            res = write_strings(res, strings)
        outfile.write(res)
        line = infile.readline().rstrip()
        if line != "":
            outfile.write('\n')

    infile.close()
    outfile.close()
    print("success")
    exit()


def write_strings(res, strings):
    res_split = res.split(',')
    for i in strings.keys():
        res_split[i] = strings[i]
    return ','.join(res_split)


def get_strings(outpattern):
    # return False OR a dictionary mapping output indices to strings
    # this is used to write a static string to an output column
    return_dict = {}
    has_strings = False
    for i, str in enumerate(outpattern.split(',')):
        if len(str) > 1:
            has_strings = True
            return_dict[i] = str
    if not has_strings:
        return False
    return return_dict


def make_mapping(inpattern, outpattern):
    # inpattern is same number of chars as a line of the input csv
    # it makes to the same letter in 
    # mapping just says to ignore a column or where the column is going in the final output
    # so an array the length of inpattern
    # -1 mean to drops a string
    # >= 0 means to put source into that out index#
    mapping = []
    for ch in inpattern.split(','):
        if ch == "_":
            mapping.append(-1)
        else:
            for i, ch2 in enumerate(outpattern.split(',')):
                if ch == ch2:
                    mapping.append(i)
                    break
            else:
                print(f"can't find key {ch} in outpattern")
                exit()
    return mapping


def parse_line(line, mapping, output_length):
    # take in a line and return its formatted equivalent
    items = line.split(',')
    output = ["" for _ in range(output_length)]
    for value, destination in zip(items, mapping):
        if destination == -1:
            continue
        output[destination] = value
    return ','.join(output)    


if __name__ == "__main__":
    main()

