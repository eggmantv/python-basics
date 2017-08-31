"""从一个URL获取单词出现的频率

Usage:
    python words_counter.py
"""

from urllib.request import urlopen


def count_words():
    """从一个URL统计单词出现的次数

    Args:
        None

    Return:
        A dict with words number.
    """

    # 这个地方的URL可以作为参数
    response = urlopen("https://eggman.tv/files/w.txt") # hello
    words = {}

    for line in response.readlines():
        data = line.split()
        for word in data:
            word = word.decode('utf-8').lower()
            words[word] = words.get(word, 0) + 1

    return words


def print_counter(words):
    """打印出统计结果

    Args:
        A dict.

    Return:
        None
    """
    for key in words:
        print(key, words[key])


def main():
    print_counter(count_words())


if __name__ == '__main__':
    main()
