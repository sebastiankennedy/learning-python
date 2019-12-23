import os
import time


def main():
    content = ' 十年又过去，举止仍像少女，你跟我每夜仍在聚，到梦里追。 '
    while True:
        os.system('clear')
        print(content)
        content = content[1:] + content[0]
        time.sleep(0.25)


if __name__ == '__main__':
    main()
