# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n= int(input())
    a= n % 1440
    b= a // 60
    a= a % 60
    print(f"{b:02}:{a:02}")

   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()