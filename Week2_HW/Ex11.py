import time
from Week2_HW.Ex10 import play_game
import matplotlib as plt

game_len = []
time.time()
for i in range(1000):
    before = time.time()
    play_game()
    after = time.time()
    game_len.append(after - before)

print(game_len)
plt.hist(game_len)
# plt.title("Game Lengths")
# plt.xlabel("Games")
# plt.ylabel("Time Taken")

plt.show()