from game import Game1, Game2, Game3

game1 = Game1()
game1.add_winner(2, "player1")

game2 = Game2()
game2.add_winner(3, "player2")

game3 = Game3()
game3.add_winner(1, "player3")

game1.leaderboard.print()
game2.leaderboard.print()
game3.leaderboard.print()