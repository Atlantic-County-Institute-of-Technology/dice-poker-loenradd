# Leonard DeMarco, 1/13/26 - 0/0/26, Dice Poker

import random
import os
import display

class Dice:
    def __init__(self):
        self.faces = 6
        self.cur_val = int
        self.dice_array = []
        self.dice_array_vals = []


    def roll(self):
        self.cur_val = random.randint(1, self.faces)

    def get_val(self):
        return self.cur_val

    def create_array(self):
        for i in range(self.max_dice):
            self.dice_array.append(Dice())


class DiceHandler:

    def __int__(self):
        self.keep_list = []
        self.dice_array = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.dice_array_vals = [0, 0, 0, 0, 0]

    def roll_all(self):
        for i in range(len(self.dice_array)):
            if not (i in self.keep):
                self.dice_array[i].roll()
                self.dice_array_vals[i] = self.dice_array[i].get_val()

    def show(self):
        return self.dice_array_vals

    def keep(self, die: int):
        if die in self.keep_list:
            self.keep_list.remove(die)
        else:
            self.keep_list.append(die)

    def dice_val_graphic(self):
        return display.display_dice(self.dice_array_vals)

    def score(self):
        amount_of_each = [0, 0, 0, 0, 0, 0]
        for i in range(len(self.dice_array_vals)):
            amount_of_each[i] = self.dice_array_vals(i + 1)
        if 5 in amount_of_each:
            return "FIVE OF A KIND"
        elif 4 in amount_of_each:
            return "FOUR OF A KIND"
        elif 3 in amount_of_each:
            return "THREE OF A KIND"
        elif 2 in amount_of_each:
            check = amount_of_each.count(2)
            print(check)
            if check == 2:
                return "TWO PAIRS"
            else:
                return "TWO OF A KIND"
        else:
            return "STRAIGHT"


luigi ="x.:..::..:.Xx:+:+x:&$&.$&$x;&;X&&$&&XXxxxx:...:xxxxxxx;:+xX$XXX$$XXXX$&;++$&&x:;:+&&+$&&xX     \n" \
"$;:;+::+;:;;:.:....&&$..$$&&x$xxx+xXXxxx;..;....xxxx$$+&&$;+;+X&&$xx;+;&&$$&&&+x++xx$$+x$&    \n"\
"x..........;xxxx+$$&&&X$&&&X$&&$XxxXxxxx+..+++:.xxxxx$&&&$$&&$Xx+x$&&&&&&&&&$X;x$&&x:+&$&&     \n"\
"$:::;::+:::+x;xxx&&&&$.:&&&&&&&&&&$xxxxxxxx+;+xxxxxxxxX&&&&&&&&&&&&&&&&&&&&x&&&&&&&&&&&&&&     \n"\
"$:..x..x;..++x$X&&&&&&$&&&&&&&&&&$$xxxxx$x;;;;xxx+++xxx&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&     \n"\
"x.;...:.:.+Xx.x&&&&&$x..&&&&&&&&&$$X+;$;::;:::;::;X:+xxx&&&XX$&$X&&&&&$X&&&&&$&$X&&&&&$xx$     \n"\
"X:::+::.:::$x:x&&&&&&&x.&&&&&&&&&$$x:....;;...+;.....xx&&&$$$$XX$&$xX$$$X$XX$$$$$$&$$$$$$$     \n"\
"x.......&$$$$$$$$&$$Xx:;X$$$:.:;x.:$+:..X&x..:$&....;;.x&$$X$$$XX$$$X$$XX$$X$X$$X$$$$X$XX$     \n"\
"x:::+::;&x$+xxxx$&&xXx:;x$$x$.::.:;;X:..;...........:;..;;;x$$$xX$+$X$$x$$$X$X$$$XX$$X&$X$     \n"\
"x;.:x..x$xXx+xXx&&&xXx..$$$x$;x;;..;+&&$;::.....:&&x:...XXXXXXxxxxxxxxxxxxxxxxxxXxxxxxxxxx     \n"\
".x::$&&&x+xxx;X$$&$$$x;;X$$$X$$&&&X:X&&&&x;::::X&&&&.X&++X++XXxxXxxxX+;;++x$$$$$$$$$$$$$$$     \n"\
"xxxx$$&&&&$x$$$X$$x&$$&&&$X$$$&&&&$$$$x$&&$+;x&&x+X&&&+++++++++++++Xxx+x$$$$$$$$$$$XXXXXXX     \n"\
"::...:x$$$$&$$$$X$$$$&&&&$$X$$&$&&$X;$$x;::......x$$$$$$$$$$$$X$$$$XX&$Xxxxxxxx+++++;;xx+x     \n"\
"&&$$$$$$$$&&&XX$$X$&&$$&&X$xx&&&x&&&&XXx;;;::.::;xxxxxxxxxxxxxxxxxXXX$$&&&&&$&&&&&$$$XXXXX     \n"\
"&$$&&&&$$$$&&$$X$$X&&&&$$+$&&&xxX+:...x$xx:...+xx$.....;xxx+xx+x;xxxx$$x$$$X&&&X&&&&$&&&$&     \n"\
"&$&&&&XXxxx&&Xx...X&&$xxxxxxxxx:......X$xxxxxxxxX$:......;+++++++x;xx$$;$$$x$$$x$$$$X$&$$&     \n"\
"&&&&&&&&&&$xX&$&&$xxx;;$X;+xx:.......;$$Xxx..:$xx$$........;+;:++;;++xxX$$$;$$$+$$$Xx$$$x$     \n"\
"&&&&&&&&&&$xxxxxxx;+xx+++:.........x&$$$$$$:.;$$$$$$X..........;++++++++;;x;X$$;$$$Xx$$$;$     \n"\
"xx&&xx+++++XX++++++++;;...........;&$$$$$$$X;$$$$$$$$+;:.........;;++++++++++++xxxxxxxxx;$     \n"\
"+++;;++;:+;;;;;;:;;;:............:;&$$$$$$$$&$$$$$$$$X:;:............;;:+++++++;+x$x.;xxxx     \n"\
"xxx;;+xxx;:xxx+;;;:..............:;&$$$$$$x;:x$$$$$$$X;...............;;;;;;::;+x::;;;;;:+     \n"\
":::;;::::&+.:::;;.................x&$$$$$X:::::$$$$$$X.................;;;;;;;;;;x:+:;:;x$     \n"\
":::&$+:::$$:::;Xx............xXXx+XXXXXXXXXXXXXXXXXXXXx;xXXx...........:XXXXXXXXXxx$$$X;$&     \n"\
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$     "
def main():
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

    round_start = True
    dice = DiceHandler()
    while game:

        if round_start:
            round_start = False
            dice.roll_all()
            os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
        if game_round <= 0:
            game = False
            print(dice.dice_val_graphic())
            print(dice.score())
            print("ok leave now")
            quit()
        else:

            print(luigi)
            print("".join(cur_dice))
            print(dice.score())

            try:
                kept_dice = int(input("\nChoose the dice you would like to keep. Input anything else to continue. : "))
                if kept_dice < 1 or kept_dice > dice.max_dice:
                    input("[!] Please select a valid die.")
                    continue
                else:
                    dice.keep(kept_dice)
            except ValueError:
                match input("[!] Are you sure? y/n :"):
                    case "y":
                        round_start = True
                        game_round -= 1
                        continue
                    case _:
                        continue


if __name__ == '__main__':
    main()