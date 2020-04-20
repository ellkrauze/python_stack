def main():
    file = open('input.txt', 'r')
    text = file.read().splitlines()
    file.close()
    for grade in range(9,11+1):
        for line in text:
            if int(line.split(' ')[0]) == grade:
                print(line)
    file.close()


if __name__ == '__main__':
    main()