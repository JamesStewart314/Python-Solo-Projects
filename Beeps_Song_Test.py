# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 or higher - 02/12/2024
# \ ----------------------------------------------------------------------------------------- / #

import winsound, time

from typing import Callable, Final

# Notes
P = 0 ; C = 1 ; CS = 2 ; D = 3 ; DS = 4
E = 5 ; F = 6 ; FS = 7 ; G = 8 ; GS = 9
A = 10 ; AS = 11 ; B = 12

EN = 100  # eighth note
QN = 200  # quarter note
HN = 400  # half note
FN = 800  # full note


class Player:
    frequency: Final[float] = 32.7032

    @staticmethod
    def play(octave, note, duration) -> None:
        if note == 0:
            time.sleep(duration / 1000)
            return None
        
        time.sleep(0.010)
        winsound.Beep(int((Player.frequency) * (2 ** (octave + note / 12))), duration)

    @staticmethod
    def _song_test() -> None:

        first_part: list[Callable[[], None]] = [
            lambda: Player.play(2, 5, 300),
            lambda: Player.play(3, 7, 200),
            lambda: Player.play(3, 7, 200),
            lambda: Player.play(3, 6, 150),
            lambda: Player.play(3, 6, 150),
            lambda: Player.play(2, 5, 300)
        ]

        second_part: list[Callable[[], None]] = [
                lambda: Player.play(2, 6, 750),
                lambda: Player.play(2, 10, 200),

                lambda: Player.play(2, 6, 750),
                lambda: Player.play(2, 10, 150),

                lambda: Player.play(2, 7, 200),
                lambda: Player.play(2, 5, 200),
                lambda: Player.play(2, 6, 300),
                lambda: Player.play(2, 4, 200),
                lambda: Player.play(2, 6, 200),

                lambda: Player.play(1, 12, 200),

                lambda: Player.play(2, 2, 300),

                lambda: Player.play(1, 12, 200),
        ]

        Player.play(1, 1, 300)  # to avoid delay

        for _ in range(2):
            for song in first_part:
                song()
            
            Player.play(0, 0, 1000)
        
        Player.play(2, 4, 300)
        Player.play(3, 6, 200)
        Player.play(3, 6, 200)
        Player.play(3, 5, 150)
        Player.play(3, 5, 150)
        Player.play(2, 4, 300)

        Player.play(0, 0, 100)

        Player.play(2, 2, 600)

        Player.play(0, 0, 700)

        for _ in range(2):
            for song in second_part:
                song()
        
        Player.play(0, 0, 250)


if __name__ == '__main__':
    Player._song_test()
