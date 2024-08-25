class Shot:
    STRIKE_MARK = "X"

    def __init__(self,pin):
        self.pin = pin

    def score(self):
        return 10 if self.is_strike() else int(self.pin)

    def is_strike(self):
        return self.pin == Shot.STRIKE_MARK
