import sys
n = 0
def main():

    if len(sys.argv) < 2 :
        print("😁😁😁😁!!!Program przerwany nazwa pliku nie prawidłowa!!!😁😁😁😁")
        return

    with open(input(sys.argv)) as f:
        for line in f:
            n += 1
            if line.strip():
                print(n, ":", line.rstrip())
        print(sys.argv)
if __name__ == '__main__':
    main()



