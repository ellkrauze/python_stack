from collections import deque

def main():
    queue = deque([])
    while True:
        input_line = input()
        console_command = (input_line.split(' '))[0]
        if console_command == 'push':
            number = int(input_line.split(' ')[1])
            queue.append(number)
            print('ok')
        if console_command == 'pop':
            if len(queue) != 0:
                print(queue.popleft())
                
            else: 
                print('error')
        if console_command == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print('error')
        if console_command == 'size':
            print(len(queue))
        if console_command == 'clear':
            queue.clear()
            print('ok')
        if console_command == 'exit':
            print('bye')
            break

        

if __name__ == '__main__':
    main()