from collections import deque

def main():
    d = deque([])
    while True:
        input_line = input()
        console_command = (input_line.split(' '))[0]

        if console_command == 'push_front':
            number = int(input_line.split(' ')[1])
            d.appendleft(number)
            print('ok')

        if console_command == 'push_back':
            number = int(input_line.split(' ')[1])
            d.append(number)
            print('ok')

        if console_command == 'pop_front':
            if len(d) != 0:
                print(d.popleft())
            else: 
                print('error')
        
        if console_command == 'pop_back':
            if len(d) != 0:
                print(d.pop())
            else: 
                print('error')

        if console_command == 'front':
            if len(d) != 0:
                print(d[0])
            else:
                print('error')

        if console_command == 'back':
            if len(d) != 0:
                print(d[-1])
            else:
                print('error')

        if console_command == 'size':
            print(len(d))

        if console_command == 'clear':
            d.clear()
            print('ok')

        if console_command == 'exit':
            print('bye')
            break

        

if __name__ == '__main__':
    main()