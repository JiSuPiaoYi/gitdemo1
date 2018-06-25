
from random import randrange


class Mahjong(object):      #一张牌
    def __init__(self, mytype, face):    #mytype:牌的类型face: 牌的点数

        self._mytype = mytype
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def mytype(self):
        return self._mytype

    def __str__(self):      # 返回牌的类型和点数
        return '%d%s' % (self._face, self._mytype)


class Mahjongs():         #一副麻将

    def __init__(self):
        self._mahjongs = []
        self._count = 0
        for x in ['萬', '筒', '条']:
            for y in range(1, 10):
                for _ in range(4):
                    mahjong = Mahjong(x, y)
                    self._mahjongs.append(mahjong)

    def shuffle(self):      #洗牌
        self._count = 0
        for index, ma in enumerate(self._mahjongs):
            pos = randrange(len(self._mahjongs))
            self._mahjongs[index], self._mahjongs[pos] = self._mahjongs[pos], self._mahjongs[index]

    def deal(self):     #发牌
        if self._count < len(self._mahjongs):
            mahjong = self._mahjongs[self._count]
            self._count += 1
            return mahjong

    def ma_end(self):   #判断是否摸完牌
        return self._count < len(self._mahjongs)

    def show(self):     #显示牌
        return self._mahjongs


class Player():

    def __init__(self, name):       #name: 玩家的名字

        self._name = name
        self._ma_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def ma_on_hand(self):       # 在手里的牌
        return self._ma_on_hand

    def get_ma(self, other):    # 摸牌
        self._ma_on_hand.append(other.deal())

    def show(self):        # 展示手里的牌
        return self._ma_on_hand

    def hand_sort(self):      # 整理手牌
        self._ma_on_hand.sort(key=get_key)


def get_key(mahjong):   #mahjong: 一张牌  返回牌点数和类型所对应ACSII码的和
    return mahjong.face + ord(mahjong.mytype)


def display(player):    #player: 一个玩家  返回: 玩家的手牌

    player.hand_sort()
    print(player.name, end=':')
    for mahjong in player.ma_on_hand:
        print(mahjong, end=' ')
    print()


def main():
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    mahjongs = Mahjongs()
    mahjongs.shuffle()
    for index, player in enumerate(players):
        if index == 0:
            for _ in range(14):
                player.get_ma(mahjongs)
        else:
            for _ in range(13):
                player.get_ma(mahjongs)

    for player in players:
        display(player)


if __name__ == '__main__':
    main()

