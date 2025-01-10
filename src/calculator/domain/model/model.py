from dataclasses import dataclass


@dataclass
class Operands:
    left: int
    right: int

    def __hash__(self):
        return hash(self.left + self.right)

    def __eq__(self, value):
        if not isinstance(value, Operands):
            return False
        return self.left == value.left and self.right == value.right
