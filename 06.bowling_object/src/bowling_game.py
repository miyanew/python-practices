from bowling_frame import Frame


class Game:
    def __init__(self, roll_sequence):
        self.frames = self._build_frames(roll_sequence)

    def calc_score(self):
        return sum(f.calc_score(self.frames) for f in self.frames)

    def _build_frames(self, roll_sequence):
        frames = []
        current_frame = None
        for roll in roll_sequence.split(","):
            if (current_frame is None) or (not current_frame.is_addable()):
                current_frame = Frame(len(frames)+1)
                frames.append(current_frame)
            current_frame.add(roll)
        return frames
