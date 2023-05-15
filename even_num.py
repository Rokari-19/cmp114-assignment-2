def gen_even(a, b):
    for num in range(a, b):
        if num % 2 == 0:
            even_list.append(num)
even_list = []
num1 = int(input(">> "))
num2 = int(input(">> "))

gen_even(num1, num2)
print(even_list)