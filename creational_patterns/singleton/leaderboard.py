class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
      return cls
    
    @classmethod
    def print(cls):
        print("-----------Leaderboard------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()
    
    @classmethod
    def add_winner(cls, position, name):
        cls._table[position] = name 