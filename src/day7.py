def not_(sig_in: str, sig_out: str):
    global wires
    assert sig_in.isalpha() or sig_in.isdigit()
    if sig_in.isalpha():
        if sig_in in wires:
            wires[sig_out] = wires[sig_in] ^ int('1' * 16, 2)  # 65535
    elif sig_in.isdigit():
        wires[sig_out] = int(sig_in) ^ int('1' * 16, 2)  # 65535


def or_(sig_in1: str, sig_in2: str, sig_out: str):
    global wires
    assert sig_in1.isalpha() or sig_in1.isdigit()
    assert sig_in2.isalpha() or sig_in2.isdigit()
    if sig_in1.isalpha():
        if sig_in1 in wires:
            a = wires[sig_in1]
        else:
            return
    else:
        a = int(sig_in1)
    if sig_in2.isalpha():
        if sig_in2 in wires:
            b = wires[sig_in2]
        else:
            return
    else:
        b = int(sig_in1)
    wires[sig_out] = a | b


def and_(sig_in1: str, sig_in2: str, sig_out: str):
    global wires
    assert sig_in1.isalpha() or sig_in1.isdigit()
    assert sig_in2.isalpha() or sig_in2.isdigit()
    if sig_in1.isalpha():
        if sig_in1 in wires:
            a = wires[sig_in1]
        else:
            return
    else:
        a = int(sig_in1)
    if sig_in2.isalpha():
        if sig_in2 in wires:
            b = wires[sig_in2]
        else:
            return
    else:
        b = int(sig_in1)
    wires[sig_out] = a & b

wires = {}
TARGET_NODE = 'a'

loops = 0

while TARGET_NODE not in wires:
    with open('../input/day7') as f:
        loops += 1
        print(len(wires))
        for line in f:
            args, destination = line.split(' -> ')
            args = args.split(' ')
            destination = destination.replace('\n', '')
            if len(args) > 1:
                if args[0] == 'NOT':
                    source = args[1]
                    if source in wires:
                        wires[destination] = wires[source] ^ 65535
                elif args[1] == 'OR':
                    or_(args[0], args[2], destination)
                elif args[1] == 'AND':
                    and_(args[0], args[2], destination)
                elif args[1] == 'RSHIFT':
                    source = args[0]
                    shift_amount = int(args[2])
                    if source in wires:
                        wires[destination] = wires[source] >> shift_amount
                elif args[1] == 'LSHIFT':
                    source = args[0]
                    shift_amount = int(args[2])
                    if source in wires:
                        wires[destination] = wires[source] << shift_amount
            else:
                if str(args[0]).isalpha():
                    source = args[0]
                    if source in wires:
                        wires[destination] = wires[source]
                elif str(args[0]).isdigit():
                    value = int(args[0])
                    wires[destination] = value

print('Done')
print(wires['a'])
