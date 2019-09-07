import apiconfig
from api.summoner import Summoner


def main():
    with open('key.txt', 'r') as key:
        apiconfig.initialize(key.readline())
    summoner = Summoner('eun1')
    for i in range(101):
        print(summoner.by_name('October'))


if __name__ == '__main__':
    main()
