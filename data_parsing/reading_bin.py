
with open('../data/032516/binlog/032516_3.bin', mode='rb') as inf:
    k = 16
    byte = inf.read(k)
    a = 0
    print(len(inf.read()))
    print('started')
    while byte != "":
        print(byte, a)
        # x = int.from_bytes(byte, byteorder='little', signed="True")
        # print(x)
        # print()
        a += 1
        byte = inf.read(16)
        if a == 16:
            break
