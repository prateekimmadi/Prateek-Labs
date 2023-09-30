import time
import random
from Displays import *
from Lights import *
from Button import *
from Random_Generator import *

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class GamePlay:
    def __init__(self, num_players=1):
        self._display = LCDDisplay(sda=16, scl=17, i2cid=0)
        self.num_players = num_players
        self.random=[]
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player = 0

        self._button_green = Button(15, "green", buttonhandler=self)
        self._button_red = Button(20, "Red", buttonhandler=self)
        self._button_white = Button(21, "white", buttonhandler=self)
        self._button_yellow = Button(18, "yellow", buttonhandler=self)
        self._button_blue = Button(19, "blue", buttonhandler=self)

        self.red_led = Light(4, "red_led")
        self.white_led = Light(3, "white_led")
        self.yellow_led = Light(2, "yellow_led")
        self.blue_led = Light(1, "blue_led")

        self.list_random_sequence = [self.green_led,self.red_led,self.white_led,self.yellow_led,self.blue_led]

    def switch_to_next_player(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def play_game(self):
        while True:
            if not self._button_green.value():
                print(f"{self.players[self.current_player].name} started their turn.")
                random_sequence = generate_random_sequence()
                light_sequence(random_sequence)
                print(f"{self.players[self.current_player].name}'s turn complete. Score: {self.players[self.current_player].score}")
                self.switch_to_next_player()

def generate_random_sequence():
    return random.choices([4, 3, 2, 1], k=4)

def light_sequence(sequence):
    leds = [game.red_led, game.white_led, game.yellow_led, game.blue_led]
    for pin in sequence:
        leds[pin - 1].value(1)
        time.sleep(0.2)
        leds[pin - 1].value(0)

if __name__ == "__main__":
    num_players = 2  # You can change this to the desired number of players
    game = GamePlay(num_players)
    game.play_game()
