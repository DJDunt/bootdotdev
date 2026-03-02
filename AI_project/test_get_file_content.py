from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    print(f"Lorem.txt length: {len(result)}")
    print(f"Ends with truncation message: {result.endswith(']')}")
    
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)


if __name__ == "__main__":
    test()