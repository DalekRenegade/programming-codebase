"""


 ^   |\                       /|
 |   |  \                   /  |
 |   |    \ L/2       L/2 /    |      y = (h - g)
 h   |      \           /      |
 |   |        \       /        |
 |   |          \   /          |
 |   |            -            | ---------------------
 |   |            ^            |
 v   |            g            |         g
     |            v            |

     <----------- 2x ---------->


The equation for a catenary tangent/touching the ground/x-axis is:
y = a cosh(x/a) - a
=> a cosh(x/a) = (h - g) + a
=> cosh(x/a) = (h - g + a) / a


arc length = a sinh(x/a)
=> a sinh(x/a) = (L/2)
=> sinh(x/a) = (L/2) / a


We then use the hyperbolic identity:

cosh2 t - sinh2 t = 1
=> (h - g + a)^2    (L/2)^2
   ___________ -    _______   = 1
       a^2            a^2


            (L/2)^2  -  (h - g)^2
=>   a = _________________________
                2 *(h - g)
"""


def hangingCable(pole_height, rope_length, rope_above_ground):
    if (pole_height - rope_above_ground) >= (rope_length / 2):
        return 0
    a_numerator = ((rope_length / 2) ** 2) - ((pole_height - rope_above_ground) ** 2)
    a_denominator = 2 * (pole_height - rope_above_ground) * 1.0
    return a_numerator / a_denominator


print hangingCable(50, 80, 10)
print hangingCable(50, 80, 20)
# print hangingCable(30, 80, 20)
# print hangingCable(30, 80, 20)
# print hangingCable(30, 80, 20)
