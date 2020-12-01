# This is my first task i came up with

player1 = 'danila'
kill1 = 27                # Statistic player1 for one game
dead1 = 13

player2 = 'ilya'
kill2 = 23                # Statistic player2 for one game
dead2 = 18

player3 = 'george'
kill3 = 11                 # Statistic player3 for one game
dead3 = 19


def kd_statistics_calculator(player, kill, dead):
    kd = kill / dead

    print('Статистика за матч: ' + str(kd))

    if kd > 1:
        return player + ' ты хороший игрок!'
    else:
        return player + ' ничего страшного, ты сможешь лучше!'
kd1 = kd_statistics_calculator(player1, kill1, dead1)
kd2 = kd_statistics_calculator(player2, kill2, dead2)
kd3 = kd_statistics_calculator(player3, kill3, dead3)
print(kd1)
print(kd2)
print(kd3)
