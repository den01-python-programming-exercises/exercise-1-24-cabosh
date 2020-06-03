def main():
    #write your code below this line
    age = int(input("How old are you? "))

    if age < 18:
        print("You are not an adult")
    elif age >= 18:
        print("You are an adult")

if __name__ == '__main__':
    main()
