def compute_prefix_function(needle):
    m = len(needle)
    prefix_function = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and needle[i] != needle[j]:
            j = prefix_function[j - 1]
        if needle[i] == needle[j]:
            j += 1
        prefix_function[i] = j
    return prefix_function


def kmp_search(needle, haystack):
    m = len(needle)
    n = len(haystack)
    prefix_function = compute_prefix_function(needle)
    matches = []
    j = 0

    for i in range(n):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix_function[j - 1]

        if haystack[i] == needle[j]:
            j += 1

        if j == m:
            matches.append(i - m + 1)
            j = prefix_function[j - 1]

    return matches


def process_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()

    i = 0
    result = []

    while i < len(data):
        needle_len = int(data[i].strip())
        needle = data[i + 1].strip()
        haystack = data[i + 2].strip()

        matches = kmp_search(needle, haystack)

        if matches:
            result.append("\n".join(map(str, matches)))
        else:
            result.append("")

        i += 3

    sys.stdout.write("\n\n".join(result) + "\n")

process_input()
