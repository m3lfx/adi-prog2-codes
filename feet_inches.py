def main():
    feet = float(input("enter size in feet"))
    size = feet_inches(feet)
    print(f"the equivalent value of {feet} ft is {size} inches")


def feet_inches(feet):
    inches = feet * 12
    return inches

main()