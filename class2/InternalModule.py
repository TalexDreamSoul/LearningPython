import math

def main():
    r = float(input().strip())
    circumference = 2 * math.pi * r
    area = math.pi * r * r
    print(circumference)
    print(area)

if __name__ == "__main__":
    main()