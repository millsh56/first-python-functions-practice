def max_num(a,b,c):
  return max([a,b,c])
print(max_num(4, 2, 8))

def mult_list(list):
  product = list[0]
  if len(list) > 1:
    for x in list[1:]:
      product = product * x
    
    return product
print(mult_list([1, 3, 5]))

def rev_string(string):
  return string[::-1]
print(rev_string('hello'))

def num_within(x, y, z):
  return x in range(y,z+1)
print(num_within(30, 10, 50))

def pascal(n):
    if n < 1:
        print('cannot be 0')
    elif n == 1:
        print(triangle[0])
    else:
       row_number = 2
       while len(triangle) < n:
          row = []
          row_prev = triangle[row_number - 1]
          length = len(row_prev)+1
       for x in range(length):
        if x == 0:
             row.append(1)
        elif x > 0 and x < length-1:
             row.append(triangle[row_number-1][x-1]+triangle[row_number-1][x])
        else:
           row.append(1)
        triangle.append(row)
        row_number += 1

        for row in triangle:
           print(row)

triangle = [[1], [1, 1]]

pascal(1)

pascal(5)
                                                           