import math
print("Convert Decimal to n-base number")
base = int(input("Base: "))
num = float(input("Number: "))
int_part = math.floor(num)
floating_part = num - int_part
reverse_base_arr = []
floating_base_arr = []
def floating_part_exist():
    if(floating_part != float(0)):
        return True
    else:
        return False
def reverse_reversed_base_arr(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[len(arr) - i - 1])
    return(new_arr)
def check_if_base_16(num):
    if (base == 16):
        if(num == 10):
            return 'A'
        elif(num == 11):
            return 'B'
        elif(num == 12):
            return 'C'
        elif (num == 13):
            return 'D'
        elif (num == 14):
            return 'E'
        elif (num == 16):
            return 'F'
        else:
            return num
    else:
        return num
def print_base_number(interger_binary_arr, float_binary_arr):
    result = ''
    if(floating_part_exist):
        for i in range(len(interger_binary_arr)):
            result = result + str(interger_binary_arr[i]) 
        for i in range(len(float_binary_arr)):
            if (i == 0):
                result = result + "."
            result = result + str(float_binary_arr[i])   
    else:
        for i in range(len(interger_binary_arr)):
            result = result + str(interger_binary_arr[i])
    print(result)
#main
while(int_part != 0):
    reverse_base_arr.append(check_if_base_16(int_part % base))
    int_part = int_part // base
reversed_binary_arr = reverse_reversed_base_arr(reverse_base_arr)
if(floating_part_exist()):
    while (floating_part != math.floor(floating_part)):
        floating_base_arr.append(check_if_base_16(math.floor(floating_part*base)))
        floating_part = floating_part*base - math.floor(floating_part*base)
else:
    pass
print_base_number(reversed_binary_arr,floating_base_arr)
