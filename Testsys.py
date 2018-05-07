from optparse import OptionParser

def main():
    option = option_args()
    if option.verbose:
        print('verbose')
    print(option.greet % option.who)

def option_args():
    parser = OptionParser(usage='%prog [OPTIONS] [WHO]')
    parser.add_option('-g','--greet',dest='greet',default='Hello %s',help='12313213212312123123123',metavar='mssage')
    parser.add_option('-v','--verbose',action='store_true',dest='verbose',default=False,help='Print current times as well')

    option,args = parser.parse_args()
    
    if '%s' not in option.greet
        parser.error('-g options requires a placeholder %s in it.')
    if len(args) > 1:
        parser.error('Too many arguments.')
    option.who = 'World' if len(args) == 0 else args[0]
    return option

if __name__ == '__main__':
    main()