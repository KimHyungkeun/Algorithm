select 
case
    when a >= b+c or b >= a+c or c >= a+b then 'Not A Triangle'
    when a = b and b = c and c = a then 'Equilateral'
    when a = b or b = c or c = a then 'Isosceles'
    else 'Scalene'
end
from triangles