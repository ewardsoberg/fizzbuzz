def main():
    for number_list in range(1, 101):
        if number_list % 3 == 0 and number_list % 5 == 0:
            print("Fizzbuzz")
        elif number_list == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        elif number_list % 3 == 0:
            print("Fizz")
        elif number_list % 5 == 0:
            print("Buzz")
        else:
            print(number_list)


if __name__ == "__main__":
    main()

