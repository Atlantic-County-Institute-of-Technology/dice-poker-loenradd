# Leonard DeMarco, 1/13/26 - 2/2/26, Dice Poker

import random
import os
import display

class Dice:
    def __init__(self):
        self.faces = 6
        self.cur_val = int

    def roll(self):  # Rolls the dice.
        self.cur_val = random.randint(1, self.faces)

    def get_val(self):  # Returns dice value.
        return self.cur_val


class DiceHandler:

    def __init__(self):
        self.keep_list = []
        self.full_kept = []
        self.dice_array = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.dice_array_vals = [0, 0, 0, 0, 0]
        self.keep_display_list = ["   [NOT KEPT]  ", "   [NOT KEPT]  ", "   [NOT KEPT]  ", "   [NOT KEPT]  ", "   [NOT KEPT]  "]

    def roll_all(self):  # Rolls all dice, except for the dice included in full_kept list.
        for i in range(len(self.dice_array)):
            if not (i in self.full_kept):
                self.dice_array[i].roll()
                self.dice_array_vals[i] = self.dice_array[i].get_val()

    def show(self):
        return self.dice_array_vals

    def keep(self, die: int):  # Keeps a dice. Adds it to keep_list, which will eventually be added to full_kept.
        if not die in self.full_kept:
            if die in self.keep_list:
                self.keep_list.remove(die)
            else:
                self.keep_list.append(die)

    def keep_display(self, die: int):  # Displays "kept" or "not kept" underneath the dice.
        if not die in self.full_kept:  
            if die in self.keep_list:
                self.keep_display_list[die] = "     [KEPT]    "
            else:
                self.keep_display_list[die] = "   [NOT KEPT]  "


    def update_full_keep(self):  # Updates the full_keep list. This ensures that the user cannot unkeep dice after the round has elapsed.
        self.full_kept += self.keep_list
        self.keep_list = []


    def dice_val_graphic(self):  # Displays the dice graphics.
        return display.display_dice(self.dice_array_vals)

    def score(self):  # Calculates score.
        amount_of_each = [0, 0, 0, 0, 0, 0]
        for i in range(len(amount_of_each)):
            amount_of_each[i] = self.dice_array_vals.count(i+1)
        if 5 in amount_of_each:
            return 8
        elif 4 in amount_of_each:
            return 7
        elif 3 in amount_of_each:
            if 2 in amount_of_each:
                return 6
            else:
                return 5
        elif 2 in amount_of_each:
            if amount_of_each.count(2) == 2:
                return 4
            else:
                return 3
        elif amount_of_each.count(1) == 5 and amount_of_each[5] != 1:
            return 2
        else:
            return 1

    def score_text(self, id):  # Returns the name of the dice hand based on the ID provided from score().
        match id:
            case 8:
                return "                              FIVE OF A KIND"
            case 7:
                return "                              FOUR OF A KIND"
            case 6:
                return "                                 FULL HOUSE"
            case 5:
                return "                              THREE OF A KIND"
            case 4:
                return "                                 TWO PAIRS"
            case 3:
                return "                               TWO OF A KIND"
            case 2:
                return "                                  STRAIGHT"
            case 1:
                return "                               HIGH DIE ONLY"


def main():
    # my epic ascii
    print(
'    ,gggggggggggg,        ,a8a,     ,gggg,   ,ggggggg,\n'
'dP\"\"\"88\"\"\"\"\"\"Y8b,     ,8\" \"8,  ,88\"\"\"Y8b,dP\"\"\"\"\"\"Y8b                         \n'
'Yb,  88       `8b,    d8   8b d8\"     `Yd8\'    a  Y8\n'
' `\"  88        `8b    88   88d8\'   8b  d88     \"Y8P\'\n'
'     88         Y8    88   8,8I    \"Y88P`8baaaa\n'
'     88         d8    Y8   8I8\'        ,d8P\"\"\"\"\n'
'     88        ,8P    `8, ,8d8         d8\"\n'
'     88       ,8P8888  \"8,8\"Y8,        Y8,\n'
'     88______,dP\'`8b,  ,d8b,`Yba,,_____`Yba,,_____,\n'
'    888888888P\"    \"Y88P\" \"Y8 `\"Y8888888 `\"Y8888888\n'
'\n'
'\n'
' ,ggggggggggg,    _,gggggg,_     ,ggg,        gg   ,ggggggg, ,ggggggggggg,   \n'
'dP\"\"\"88\"\"\"\"\"\"Y8,,d8P\"\"d8P\"Y8b,  dP\"\"Y8b       dP ,dP\"\"\"\"\"\"Y8dP\"\"\"88\"\"\"\"\"\"Y8, \n'
'Yb,  88      `8,d8\'   Y8   \"8b,dYb, `88      d8\' d8\'    a  YYb,  88      `8b\n'
' `\"  88      ,8d8\'    `Ybaaad88P\'`\"  88    ,dP\'  88     \"Y8P\'`\"  88      ,8P\n'
'     88aaaad8P\"8P       `\"\"\"\"Y8      88aaad8\"    `8baaaa         88aaaad8P\"\n'
'     88\"\"\"\"\"   8b            d8      88\"\"\"\"Yb,  ,d8P\"\"\"\"         88\"\"\"\"Yb,\n'
'     88        Y8,          ,8P      88     \"8b d8\"              88     \"8b\n'
'     88        `Y8,        ,8P\'      88      `8iY8,              88      `8i\n'
'     88         `Y8b,,__,,d8P\'       88       Yb`Yba,,_____,     88       Yb,\n'
'     88           `\"Y8888P\"\'         88        Y8 `\"Y8888888     88        Y8\n'
'                                                                             \n'
)
    input("Press Enter to Start")
    start_game()


def start_game():

    game = True

    game_round = 3

    round_start = True  # If true, dice will be rolled at the start of the round. Important for the while loop.
    dice = DiceHandler()
    scorer = 0
    while game:
        os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
        if round_start:
            round_start = False
            dice.roll_all()
            scorer = dice.score()

        if game_round <= 0 or scorer == 8:  # Endgame. Happens if there are no more game rounds or if you end up with Five Of A Kind.
            game = False
            print(dice.dice_val_graphic())
            print(dice.score_text(scorer))
            match input("[!] Would you like to play again? y/n :"):
                    case "y":
                        start_game()
                    case _:
                        quit()
        else:

            print(dice.dice_val_graphic())
            print("".join(dice.keep_display_list))  # Turns keep_display_list into a neat string. Why does join() work like that, I hate it.
            print(dice.score_text(scorer))

            try:
                kept_dice = int(input("\nChoose the dice you would like to keep. Input anything else to continue. : "))
                
                if kept_dice < 1 or kept_dice > 5:  # tomfoolery prevention
                    input("[!] Please select a valid die.")
                    continue
                else:
                    dice.keep(kept_dice-1)
                    dice.keep_display(kept_dice-1)
            except ValueError:
                match input("[!] Are you sure? y/n :"):
                    case "y":
                        dice.update_full_keep()
                        round_start = True
                        game_round -= 1
                        continue
                    case _:
                        continue


if __name__ == '__main__':
    main()