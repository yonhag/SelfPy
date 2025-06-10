from random import randint

HANGMAN_STATES = {
    1: "x-------x",
    2: """x-------x
    |
    |
    |
    |
    |""",
    3: """x-------x
    |       |
    |       0
    |
    |
    |""",
    4: """x-------x
    |       |
    |       0
    |       |
    |
    |""",
    5: r"""x-------x
    |       |
    |       0
    |      /|\
    |
    |""",
    6: r"""x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""",
    7: r"""x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""
}

def main():
    print('Welcome to the game Hangman')
    print(r"""  _    _                                        
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
    print(randint(5, 10))

def print_hangman_state(state: int):
    print(HANGMAN_STATES[state])




if __name__ == '__main__':
    main()