def repl():
    cmd = ''
    while cmd != 'quit':
        cmd = input('> ')
        evalcmd(cmd)
    print("Goodbye")

def hello(arglst):
    print("Hello!")

def add(arglst):
    argsum = 0
    for num in arglst:
        argsum += int(num)
    print(argsum)

cmds = {'hello': hello, 'add': add}

def evalcmd(cmdstr):
    cmdlst = cmdstr.split()
    if cmdlst[0] == 'quit':
        return
    elif cmdlst[0] in cmds.keys():
        cmds[cmdlst[0]](cmdlst[1:])
    else:
        print("Invalid command")
