def recursiveFactorial(num):
    # 5! 5*4*3*2*1
    if num == 1 or num == 0:
        return 1
    else:
        return num * recursiveFactorial(num-1)

print(recursiveFactorial(0))
    