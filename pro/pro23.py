def dir(s):
    a = s[:len(s) // 2]
    if len(s) / 2 == len(s) // 2:
        b = s[len(s) // 2:]
    else:
        b = s[len(s) // 2 + 1:]
    if a == b:
        print('yes')
    else:
        print('no')


def main():
    try:
        str = input()
        dir(str)
    except:
        print('invalid')
