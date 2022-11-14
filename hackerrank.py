num = int(input())

def multiply_digit(n):
    final_num = 1
    while(n!=0):
        if(((n%10)%2)==0):
            final_num = final_num*(n%10)
        n=n//10
    return final_num

print(multiply_digit(num))
