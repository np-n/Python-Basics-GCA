"""
    value % 3 foo
    value % 5 bar
    value % 3 and value % 5 foobar
    value
"""

def foobar(upto):
    for num in range(1, upto):
        if num % 3 == 0 and num % 5 == 0:
            print("FooBar")
        elif num % 3 == 0:
            print("Foo")
        elif num % 5 == 0:
            print("Bar")
        else:
            print(num)
    print("This is num", num)


def main():
    till = int(input("Enter a number: "))
    foobar(till)

if __name__ == "__main__":
    main()
