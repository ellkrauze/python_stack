def main():
    stack = []
    while True:
        input_line = input()
        console_command = (input_line.split(' '))[0]
        if console_command == 'push':
            number = int(input_line.split(' ')[1])
            stack.append(number)
            print('ok')
        if console_command == 'pop':
            if len(stack) != 0:
                print(stack.pop())
            else: 
                print('stack is empty')
                break
        if console_command == 'back':
            print(stack[len(stack)-1])
        if console_command == 'size':
            print(len(stack))
        if console_command == 'clear':
            del stack[:]
            print('ok')
        if console_command == 'exit':
            print('bye')
            break

        

if __name__ == '__main__':
    main()