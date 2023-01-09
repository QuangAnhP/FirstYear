
def nar(value):
    original = value
    new_num = 0
    leng = len(str(original))
    for x in range(leng):
        last_dig = (value%10)
        new_num = new_num + (last_dig**leng)
        value = (value - (last_dig))/10
    
    if new_num == original:
        print(f"{original} -> true")
    else:
        print(f"{original} -> false")


nar(153)
nar(1652)
nar(7)
nar(371)
nar(122)
nar(4887)