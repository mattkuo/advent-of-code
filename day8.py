import inputgetter





def main():
    total = 0
    total_mem = 0
    content = inputgetter.get_input(gen=True)

    for line in content:
        line = line.strip()
        total += len(line)

        in_escape = False
        in_hex = False
        for char in line:
            if char == '"':





    print(total)

if __name__ == '__main__':
    main()
