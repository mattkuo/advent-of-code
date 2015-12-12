import hashlib
import inputgetter

def crack(key, start=0, num_zeroes=5):
    counter = start
    while True:
        h = hashlib.md5()
        string = "{}{}".format(key, counter)
        h.update(string.encode('utf-8'))
        result = h.hexdigest()
        if result[:num_zeroes] == '0' * num_zeroes:
            return counter
        counter += 1

if __name__ == '__main__':
    key = inputgetter.get_input().strip()
    result_for_5 = crack(key)
    print("Number that generates 5 0s is: {}".format(result_for_5))
    print("Number that generates 6 0s is: {}".format(crack(key, start=result_for_5, num_zeroes=6)))
