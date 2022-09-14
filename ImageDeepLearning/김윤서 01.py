def test():
    N = int(input())
    nums = list(input())
    result = 0

    for i in nums:
        result += int(i)

    print(result)

if __name__ == "__main__":
    test()