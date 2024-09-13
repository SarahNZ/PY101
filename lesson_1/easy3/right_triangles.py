def triangle(n):
    preceeding_whitespace = n - 1
    for idx in range(n):
        print(f"{' ' * (preceeding_whitespace)}{'*' * (idx+1)}")
        preceeding_whitespace -= 1

triangle(5)