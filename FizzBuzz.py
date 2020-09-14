def fizzBuzz(n):
    if 0 < n < 200000:

        # Write your code here
        for i in range(1, n + 1):
            if i % 15 == 0:
                print("FizzBuzz")

            elif i % 3 == 0:
                print("Fizz")

            elif i % 5 == 0:
                print("Buzz")

            elif i % 15 != 0:
                print(i)

    else:
        print("Please input an integer between 0 to 200000")


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

