def main(num):
    if num <= 1:
        return  False
    sum_div=1
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            sum_div +=i+num//i
    return sum_div == num



nums=28
print(main(nums))