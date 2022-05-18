from argparse import ArgumentParser as AP

parser = AP()
parser.add_argument('-s','--side',type=int)

args = parser.parse_args()

def sq_area(side):
    area = side**2
    return area

side = 5
if args.side:
 side = args.side
area = sq_area(side)    

print('Area is = ', area)
