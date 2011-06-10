def repl():
    cmd = ''
    while cmd != 'quit':
        cmd = input('> ')
        evalcmd(cmd)
    print("Goodbye")

def evalcmd(cmdstr):
    print(cmdstr + " seen")
