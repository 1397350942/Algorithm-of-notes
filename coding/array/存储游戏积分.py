"""
[1000,700,650,600,555]
"""


class GameEntry(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "(name:{0},socre:{1})".format(self._name, self._score)


class ScoreBoard(object):
    """
    capacity: 积分排行版最多可以存储的分数
    """

    def __init__(self, capacity=10):
        self._board = [None]*capacity
        self._count = 0  # 当前积分排行版实际的分数

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return "\n".join(str(self._board[i]) for i in range(self._count))

    def add(self, entry):
        score = entry.get_score()
        good = self._count < len(
            self._board) or score > self._board[-1].get_score()
        # 满足添加条件
        if good:
            if self._count < len(self._board):
                self._count += 1
            j = self._count - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


if __name__ == "__main__":
    board = ScoreBoard(5)
    for e in (("Mike", 720), ("张三", 1720), ("王军", 500)):
        ge = GameEntry(e[0], e[1])
        board.add(ge)
        print(ge)
        print()
        print(board)
