##Write a Python program to display the first and last colors from the following list. Go to the editor

color_list = ["Red", "Green", "White", "Black"]

## counter pt elementele din lista.
##  se parcurg toate

print( "%s %s"%(color_list[0],color_list[-1]))

# SAU
# size = len(color_list)
# for i in color_list:
#     if (color_list.index(i) == 0):
#         first = color_list.index(i)
#         print(color_list[int(first)])
#
#     if (color_list.index(i)) == size - 1:
#         last = color_list.index(int(size - 1))
#         print(color_list[size-1])
