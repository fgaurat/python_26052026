
def main():
    
    # f = open('le_fichier.txt','r')
    
    # open with context manager
    with open('le_fichier.txt','r') as f:

        # content = f.read()
        # lines = content.splitlines()
        
        # lines = f.readlines()

        
        # for i,line in enumerate(lines[:]):
        #     lines[i] = line.strip()

        # for i in range(len(lines)):
        #     lines[i] = lines[i].strip()
        
        # clean_lines = []
        # for line in lines:
        #     clean_lines.append(line.strip())

        # clean_lines = [line.strip() for line in lines]
        # print(clean_lines)

        for line in f:
            print(line.strip())
        

    # f.close()

def main_write():
    f = open('le_fichier.txt','a')
    # f.write('Hello\n')
    print("Hello",file=f)

    f.close()


if __name__=='__main__':
    main()
