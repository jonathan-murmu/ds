"""
Question 1 (scoring only – 15’s)
Cribbage is a card game.  A player can score points is various ways, however, we will look at 1 of the ways that a player can score below.
Imagine you need to write code in a high-level language like Java or C# that will score the point value of 4 cards using the following first way to accumulate points.
A) Combinations of cards that add up to exactly 15 are worth 2 points for each combo.  You can use 2-4 cards in the combo.
I would like you to create a reusable library to do this easily. Keep in mind that there will be additional ways to score points and we’ll add additional methods later.
Notes:
Face Cards (Jack, Queen, King): All three have a value of 10.  Therefore, a 5 paired with any of them will equal 15.
Ace: This is valued at 1
Numbered Cards: All valued at the number shown.
Example Test Cases:
Cards ("6", "7", "8", "9"): Total of 4 pts.  There are 2 sets of cards that equal 15 (6,9) and (7,8).  Two points for each of these gives us 4 points.
Cards to use: ("5", "9", "Jack", "10")
Cards to use: ("2", "Queen", "3", "3")
Cards to use: ("5", "5", "King", "5") => 8
Cards to use: ("6", "2", "Ace", "8") => 2
"""

face = {
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 1
}

from itertools import combinations

cardinput = ("6", "2", "Ace", "8")
cardinput = ("5", "5", "King", "5")
cardinput = ("2", "Queen", "3", "3")
cardinput = ("5", "9", "Jack", "10")
result = 0

for size in [2, 3, 4]:
    a = combinations(cardinput, size)
    y = [i for i in a]

    print('y', y)

    # map combination into sum
    for combination in y:
        sum = 0
        for card in combination:
            if card in face:
                sum += face[card]
            else:
                sum += int(card)

        # if sum == 15 increase counter by 2
        if sum == 15:
            result += 2

print(result)


