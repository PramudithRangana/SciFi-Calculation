from accessories import script_changer as sc


class SciNotif:
    @staticmethod
    def Suppressing(ToCal):
        # separate from - x position
        separateDecPow = ToCal.split('x')

        decNum = separateDecPow[0].strip()

        # separate decimal & tenth power
        tenthPower = [(separateDecPow[1]).replace(" ", "")]

        # tenth power (super scripted value) convert to normal integer value for calculation
        powerSet = sc.supScr_to_norm(tenthPower[0][2:])

        if powerSet[0] == '-':
            set_power = 'e' + powerSet
        else:
            set_power = 'e+' + powerSet

        return float(f"{decNum}{set_power}")

    @staticmethod
    def scifiRepr(sciNum):
        if 'e' in str(sciNum):
            factor, power = str(sciNum).split('e')

            if power[0] == '+':
                return factor.strip() + ' x 10' + sc.norm_to_supScr(str(int(power[1:])).strip())
            else:
                return factor.strip() + ' x 10' + sc.norm_to_supScr(str(int(power)).strip())
        else:
            factor, power = str(sciNum).split('*')

            tenthBase, tenthPow = power.split('^')
            return factor.strip() + ' x ' + tenthBase.strip() + sc.norm_to_supScr(str(int(tenthPow)).strip())


# print("5.97e+24      ->", SciNotif.scifiRepr(5.97e+24))
# print("5.97e-24      ->", SciNotif.scifiRepr(5.97e-24))
# print("5.97*10^24    ->", SciNotif.scifiRepr("5.97*10^24"))
# print("5.97*10^-24   ->", SciNotif.scifiRepr("5.97*10^-24"))
# print("5.970 x 10²⁴  ->", SciNotif.Suppressing('5.970 x 10²⁴'))
# print("5.970 x 10⁻²⁴ ->", SciNotif.Suppressing('5.970 x 10⁻²⁴'))
