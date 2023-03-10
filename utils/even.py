class Even:
    def __init__(self, num: int):
        self.num = num

    def check(self) -> bool:
        return not (self.num & 1)
