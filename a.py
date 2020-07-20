
# a,b,R = map(int,input("input a,b,R: ").split(" "))
# print(type(a))
# N = input("input N: ")
# xs = [[]]
# x = [[0,0]]
# for i in range(0,int(N)):
#     x[i][0], x[i][1] = input("input x,y: ").split(" ")

# print(x)

#입력 받은 숫자 N의 모든 약수 출력하시오

#입력 받은 정수값들 중 최대값과 최소값을 순서대로 출력
#max,min 못씀
stack = []

def process_stack(command,number):
    if command == 'push':
        stack.append(number)
    elif command == 'pop':
        i = stack.pop()
        if i != -1:
            print(i)
        else:
            print(-1)
            
    elif command == 'top':
        i = stack.pop()
        print(i)
        stack.append(i)
    elif command == 'size':
        print(s_size)
    elif command == 'empty':
        if s_size == 0:
            print(1)
        else:
            print(0)

while(1):
    c = input("명령어를 입력하시오 e.g push 1 :").split()

    command = c[0]
    try:
        number = int(c[1])
    except:
        pass

    process_stack(command,number,s_size)