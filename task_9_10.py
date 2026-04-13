def sort_by_length(lines):
    return sorted(lines, key=len)

if __name__ == "__main__":
    print("Введите строки:")
    lines_input = []
    while True:
        line = input()
        if not line: break
        lines_input.append(line)
    print("По длине:", sort_by_length(lines_input))

def sort_by_word_count(lines):
    return sorted(lines, key=lambda x: len(x.split()))

if __name__ == "__main__":
    print("По количеству слов:", sort_by_word_count(lines_input))