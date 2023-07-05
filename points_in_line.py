"""
2. Given three points, check whether they lie on a straight (collinear) or not. [Google]

For example:
Input-  [(1,1), (1,6), (0,9)]
Output- No

Input- [(1,1), (1,4), (1,5)]
Output- Yes

"""
#
def collinearity_of_points(list_of_points):
     # check for area
     x1, y1 = list_of_points[0]
     x2, y2 = list_of_points[1]
     x3, y3 = list_of_points[2]

     # calculate the area of a triangle
     area = 0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

     if area == 0:
          return 'Yes'
     
     else:
          return 'No'


# driver function
#list_of_points = [(1,1), (1,6), (0,9)]
list_of_points = [(1,2), (2,4), (3,6)]
print(collinearity_of_points(list_of_points))