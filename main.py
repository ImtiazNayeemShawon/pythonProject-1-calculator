first = input('enter the first num:')
oparet = input('Enter the oparetor: ')
second = input('enter the second num:')
sum1 = float(first)
sum2 =float(second)

if oparet == "-":
    print(sum1 - sum2)
elif oparet == "+":
    print(sum1 + sum2)

elif oparet == "/":
    print(sum1 / sum2)
elif oparet == "*":
    print(sum1 * sum2)

else:
    print("Opps! you don't enter opartaor please try again")
