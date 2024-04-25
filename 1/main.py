from lex import tokenize_line
def main():
    with open('test.txt', 'r') as t:
        tokens = []
        lines = t.readlines()
        for i in range(len(lines)):
            tokens.extend(tokenize_line(lines[i], i))
        
        for token in tokens:
            a, b, c, d = str(token).split('\t')
            print("{:<10}".format(a), '\t',
                  "{:<10}".format(b), '\t',
                  "{:<15}".format(c), '\t',
                  "{:<10}".format(d), '\t',
                  )




if __name__ == "__main__":
    main()