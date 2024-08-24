def calculate_expression(i):
    product = 1
    for j in range(2, i + 1):
        product *= (202 - j) / 200
    return product * (i - 1) / 200

def find_maximum():
    max_value = 0
    optimal_i = 0
    sum=0
    for i in range(2, 201):
        value = calculate_expression(i)
        sum+=value
        print(value)
        if value > max_value:
            max_value = value
            optimal_i = i
    print (sum)
    return optimal_i, max_value

optimal_i, max_value = find_maximum()
print(f"The maximum value is achieved at i = {optimal_i} with a value of {max_value:.6f}")