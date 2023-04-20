## Scientific Notation Calculation

- To run the programme :

```python
from SciFiFormatter import SciNotif

SciNotif.scifiRepr(5.97e+24)
SciNotif.scifiRepr(5.97e-24)
SciNotif.scifiRepr("5.97*10^24")
SciNotif.scifiRepr("5.97*10^-24")
SciNotif.Suppressing('5.970 x 10²⁴')
SciNotif.Suppressing('5.970 x 10⁻²⁴')
```

e.g :

Find out the escape velocity by using **√ 2GM/R**

```python
import math
from SciFiFormatter import SciNotif as Sn

G = Sn.Suppressing('6.674 x 10⁻¹¹')
M = Sn.Suppressing('5.970 x 10²⁴')
R = Sn.Suppressing('6.371 x 10⁶')

ans = '{0:.2e}'.format(math.sqrt((2 * G * M) / R))
print('answer :', Sn.scifiRepr(ans) + ' ms⁻¹')
```

#### Represent scientific notation


    [+] Use '^' sign to refer (tenth) power

                e.g: 5.970*10^-24    >>    5.970 x 10⁻²⁴

        [*] In this case -24 is the power.
        [*] Before set power its need to refer '^' sign.
        
            Minus twenty-four is power -->   ^-24  >>  ⁻²⁴ <-- Representation 

```python
from SciFiFormatter import SciNotif as Sn

print(Sn.scifiRepr('5.970*10^-24'))
```
