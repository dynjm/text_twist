"""
game based on text twist
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class TextTwist(toga.App):

    def startup(self):
        
        # initialize self.main_window and self.main_box
        self.main_box = toga.Box()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
        
        self.game_view() # allows game_view function to be done aka view game screen
        
    def game_view(self):
        
        # initialize game view box/game screen
        gameview_box = toga.Box(style=Pack(direction=COLUMN)) # initialize game view box/game screen
        
        # initialize header section (timer, points, pause)
        
        timer_label = toga.Label('Timer')
        points_label = toga.Label('Points')
        
        header_box = toga.Box(style=Pack(direction=ROW))
        header_box.add(timer_label, points_label)
        

        # initialize letters section, 8 letters
        
        letters_box = toga.Box(style=Pack(direction=ROW))
        letters_array = []
        
        for i in range(8):
            letter_button = toga.Button('')
            letters_array.append(letter_button)
            letters_box.add(letter_button)
            
        
        # initialize current answer section
        
        c_answer_label = toga.Label('Answer: ')
        self.answer_input = toga.TextInput()
        
        c_answer_box = toga.Box(style=Pack(direction=ROW))
        c_answer_box.add(c_answer_label)
        c_answer_box.add(self.answer_input)
        
        
        # initialize buttons section
        
        answer_button = toga.Button( 'Answer', style=Pack(padding=5))
        shuffle_button = toga.Button( 'Shuffle', style=Pack(padding=5))
        hint_button = toga.Button( 'Hint', style=Pack(padding=5))
        pause_button = toga.Button( 'Pause', style=Pack(padding=5))
        
        buttons_box = toga.Box(style=Pack(direction=ROW))
        buttons_box.add(answer_button, shuffle_button, hint_button, pause_button)
        
        
        # initialize answers section
        
        left_answer_box = toga.Box(style=Pack(direction=COLUMN))
        center_answer_box = toga.Box(style=Pack(direction=COLUMN))
        right_answer_box = toga.Box(style=Pack(direction=COLUMN))
        
        answer_box = toga.Box(style=Pack(direction=ROW))
        answer_box.add(left_answer_box, center_answer_box, right_answer_box)
        
        
        # finalize gameview_box
        
        gameview_box.add(header_box)
        gameview_box.add(letters_box)
        gameview_box.add(c_answer_box)
        gameview_box.add(buttons_box)
        
        # main window is now game screen
        self.main_box.add(gameview_box)


def main():
    return TextTwist()
