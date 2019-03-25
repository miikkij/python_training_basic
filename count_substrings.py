def count_substring(string, sub_string):
    success = 0;
    for i in range(0, len(string)):
        if string.find(sub_string, i, i+len(sub_string)) != -1:
            success += 1;
    return success


if __name__ == '__main__':
    print(count_substring("AABCDCDC", "CDC"));
