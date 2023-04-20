import math
from SciFiFormatter import SciNotif as Sn

G = Sn.Suppressing('6.674 x 10⁻¹¹')  # Universal Gravitational Constant [Nm²kg⁻²]
M = Sn.Suppressing('5.970 x 10²⁴')  # Mass of The Earth [kg]
R = Sn.Suppressing('6.371 x 10⁶')  # Radius of The Earth [m]

# √ 2GM/R
ans = '{0:.2e}'.format((math.sqrt((2 * G * M) / R)))
print('answer :', Sn.scifiRepr(ans) + ' ms⁻¹')
