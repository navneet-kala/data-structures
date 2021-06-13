from collections import defaultdict


def LandCoordinates(filename):
    x = defaultdict(list)
    with open(filename) as f:
        # loop through each line
        lines = f.readlines()
        row = 0
        testcase = 0
        for line in lines:
            # check if patch has begun, if so check if sea or land and write land coordinates to dictionary
            if line[0].isdigit() == False:
                #print(f'Testcase {testcase}')
                for col in range(len(line)-1):
                    if line[col] == 'X':
                        coord = (row, col)
                        x[f'land-coords-testcase-{testcase}'].append((coord))
                    #print(row, col)
                row = row+1
            # check if line is for shape of patch, if so, add shape to dictionary
            elif ' ' in line and '\n' in line:
                testcase = testcase+1
                m, n = [s.strip() for s in line.split()]
                shape = (int(m), int(n))
                x[f'shape-testcase-{testcase}'].append((shape))
                row = 0
            # check if line is for # of test cases, if so, add # to dictionary
            else:
                r = [s.strip() for s in line.split()]
                x['total-testcases'].append(r)
                row = 0
        # Dictionary will contain total # of test cases, shape of each test case patch and coordinates of each test cases' land area
        return(x)

######## TESTING the METHOD ########################

# coordinates = LandCoordinates('test.txt')
# print(coordinates)
# for key, value in coordinates.items():
#     print(key)
#     for val in value:
#         print(val)
