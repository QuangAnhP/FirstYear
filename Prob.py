# letters: abcdefghijklmnopqrstuvwxyz
def find_the_number_plate(customer_id):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    start_num_plate = "aaa001"
    fst = 'a'
    sec = 'a'
    thr = 'a'
    num = 1
    fst_done = False
    Customer_id = [fst, sec, thr, num]
    counter_al = 0
    for index in range(customer_id):
        if (num == 999):
            num = 1
            if(fst != 'z'):
                tem = alphabets.find(fst)
                fst = alphabets[tem + 1]
                continue
            elif(fst == 'z' ):
                fst = 'a'
                if (sec != 'z'):
                    tem = alphabets.find(sec)
                    sec = alphabets[tem + 1]
                    continue
                else:
                    sec = 'a'
                    if (thr != 'z'):
                        tem = alphabets.find(thr)
                        thr = alphabets[tem + 1]
                        continue
                    else:
                        continue





        else:
            num += 1
    if (len(str(num))<3):
        if (len(str(num))<2):
            num = '00' + str(num)
        else:
            num = '0' + str(num)

    print(f"{fst}{sec}{thr}{num}")

    return f"{fst}{sec}{thr}{num}"
find_the_number_plate(1)