def str_float():
    with open('smt_smt_new.txt', 'r', encoding="utf-8")as f:
        ebay_text = f.readlines()
        for i in ebay_text:
            a = 0
            tt = []
            us_name = i.strip().split(',')
            for us in us_name:
                if a == 8:
                    aaa = Float.parseFloat(str)
                    tt.append(aaa)
                tt.append(us)
                a += 1
            print(tt)


if __name__ == '__main__':
    str_float()
