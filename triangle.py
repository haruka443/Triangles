a = float(input('Length of side a: '))
b = float(input('Length of side b: '))
c = float(input('Length of side c: '))

if a+b>c and b+c>a and a+c>b:
       if a == b or a == c or b == c:
           print('The defined lengths create an isosceles triangle ')

       if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
           print('The defined lengths create a right-angled triangle')

       if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
           print('The defined lengths create an obtuse triangle')
else:
    print('It\'s not possible to create a triangle of the defined lengths')
