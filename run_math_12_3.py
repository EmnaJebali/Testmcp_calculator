try:
    from math_server import divide
except Exception:
    # Fallback if math_server can't be imported (e.g., mcp not installed).
    def divide(a, b):
        if b == 0:
            return "error: division by zero"
        return a / b


def main():
    a, b = 12, 3
    result = divide(a, b)
    print(f"divide({a}, {b}) -> {result}")


if __name__ == '__main__':
    main()
