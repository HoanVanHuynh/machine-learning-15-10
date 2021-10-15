import csv
tsv_file = open("politicians_train.tsv")

read_tsv = csv.reader(tsv_file, delimiter="\t")

tsv_headings = next(read_tsv)   # to read only the first row of the csv file use next() on the reader object.
data = [row for row in read_tsv]
#print(row1)
# print(tsv_headings)
# x_1 = tsv_headings[0]
# print(x_1)
# x_1 = []
# print(x_1)
# attribute_m

# def split(m):


# print(type(data))
# print(data[0])
# print(data[1][-1])
def train(D):
    m = int(input('pick an attribute, m: '))
    D_0 = [row for row in D if row[m] == 'n' ]
    D_1 = [row for row in D if row[m] == 'y' ]
    return D_0

D_1 = [[1,2,'y'],
    [3,4,'n'],
    [2,3,'y'],
    [2,33,'y']
]
def majority_vote(D):
    vote = {}
    for row in D:
        if row[-1] not in vote:
            vote[row[-1]] = 0 
        vote[row[-1]] += 1

    max_value = max(vote.values())
    for k, v in vote.items():
        if v == max_value:
            m_vote = k 
    
    return m_vote 

#  m = 1 len(D_0) = 86
#  m = 0 len(D_0) = 96
# import sys 

# if __name__ == '__main__':
#     infile = sys.argv[1]
#     #outfile = sys.argv[2] 

# print("The input file is: %s" % (infile))

# print("The input file is: %s" % (output))
