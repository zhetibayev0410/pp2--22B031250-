def prime_in_array(num):
    for i in range(2, int(len(num)**0.5)):
        if num % i == 1:
            print (str(num[i]) + 1)
            return
        
num =[2, 3, 4, 5, 6, 7, 8, 9]
x = prime_in_array(num)
print(x)
