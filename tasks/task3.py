# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n= int(input("введите количество евро:"))
    count=0
    count += n // 100
    n %= 100
    count+= n // 20
    n %=20
    count += n // 10
    n %= 10
    count += n // 5
    n %= 5
    count += n
    print("минимальное количество купюр" , count)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()