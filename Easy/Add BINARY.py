# def fun(a,b):
#     a_dec =""
#     b_dec=""
#     a_dec += str(int(a,2))
#     b_dec += str(int(b,2))
#     temp=int(a_dec)+int(b_dec)
#     f_ormat = format(temp,'b')
#     print(str(f_ormat))
#
# fun('11','1')


def addBinary( a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        c = a+b
        return bin(c)

print(addBinary('11','1'))