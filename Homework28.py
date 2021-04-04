'''1. Create a python function factorial and import this
file in another file and print factorial.'''

from Susik import factorial2 as f
print(f(7))



'''2. Write a Python function tocalculate surface volume and area of
a cylinder(Գլան). V=πr^2h and A=2πrh+2πr^2 :'''

from Susik import cylinder_volume_and_area as cyl 
print(cyl(6,4))



'''3. Write a Python function to calculate surface volume 
and area of a sphere(Գունդ). V = 4/3*π*r3 and A = 4*π*r2'''

from Susik import sphere_volume_and_area as sph 
print(sph(6))



'''4. Write a Python function to convert degree to radian.
one radian = pi/180: 90 radian = 1.57...'''

from Susik import degree_to_radian as dr 
print(dr(90))



'''5. Write a Python function to print all primes smaller than or equal to a
specified number. Call function: numbers(9) Output: (2, 3, 5, 7)'''

from Susik import allprimes 
print(allprimes(9))
