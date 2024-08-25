from itertools import islice
from bowling_shot import Shot


class Frame:
    LAST_FRAME_NUM = 10

    def __init__(self, number):
        self.shots = []
        self.number = number

    def is_addable(self):
        return (
            (not self.shots)
            or (len(self.shots) == 1 and not self._is_strike())
            or self._is_last_frame()
        )

    def add(self, pin):
        self.shots.append(Shot(pin))

    def calc_score(self, frames):
        score = sum(s.score() for s in self.shots)
        if self.number < Frame.LAST_FRAME_NUM:
            next_frames = frames[self.number :]
            if self._is_strike():
                score += self._strike_bonus(next_frames)
            elif self._is_spare():
                score += self._spare_bonus(next_frames[0])
        return score

    def _is_strike(self):
        return self.shots and self.shots[0].is_strike()

    def _is_spare(self):
        return (not self._is_strike()) and sum(s.score() for s in self.shots) == 10

    def _is_last_frame(self):
        return self.number == Frame.LAST_FRAME_NUM

    def _strike_bonus(self, next_frames):
        next_shots = (s.score() for frame in next_frames for s in frame.shots)
        return sum(islice(next_shots, 2))

    def _spare_bonus(self, next_frame):
        return next_frame.shots[0].score()
