def evaluate(s, debug=False, calc=False):
    calc_ans = 0
    ret = []
    stack = []
    ip = 0
    ans = ''
    buf = []
    while ret or ip < len(s):
        if ip >= len(s): s, ip = ret.pop()
        com = s[ip]
        ip += 1
        if debug:
            print(s)
            print('Command:', com)
            print('Stack:')
            for i in stack:
                print(i)
            input('...')
        match com:
            case '>':
                if len(stack) < 2:
                    ans += ''.join(f'[{s}]' for s in stack) + com
                    stack = []
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(f'[{b}]{a}')
            case '<':
                if len(stack) < 2:
                    ans += ''.join(f'[{s}]' for s in stack) + com
                    stack = []
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(f'{a}[{b}]')
            case '+':
                if len(stack) < 1:
                    ans += com
                    stack = []
                else:
                    stack.append(stack[-1])
            case '-':
                if len(stack) < 2:
                    ans += ''.join(f'[{s}]' for s in stack) + com
                    stack = []
                else:
                    a, _ = stack.pop(), stack.pop()
                    if ip < len(s):
                        ret.append((s, ip))
                    s = a
                    ip = 0
            case ',':
                if not buf:
                    buf = list(input() + '\n')
                stack.append(encode_nat(ord(buf.pop(0))))
            case '.':
                if len(stack) < 1:
                    ans += com
                    stack = []
                    print(f'Output desynchronisation at position {ip} in "{s}"')
                else:
                    print(chr(evaluate(f'[$]{stack.pop()}', calc=True)), end='')
            case '[':
                n = ''
                c = 1
                while True:
                    try:
                        com = s[ip]
                    except IndexError:
                        raise Exception(f'Unclosed "[" in "{s}"')
                    ip += 1
                    if com == '[':
                        c += 1
                    if com == ']':
                        c -= 1
                    if c:
                        n += com
                    else:
                        break
                stack.append(n)
            case ']':
                raise Exception(f'Unexpected "]" at position {ip} in "{s}"')
            case '$':
                calc_ans += 1
    ans += ''.join(f'[{s}]' for s in stack)
    return calc_ans if calc else ans


def encode_nat(n):
    if n == 0: return '[]-'
    return '+<+-' * (n - 1) + '+-'
