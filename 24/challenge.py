from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        if not isinstance(merged_prs, list):
            raise ValueError("Expected merged_prs to be of type list")
        self._merged_prs_set = set(merged_prs)

    def verify(self, value):
        return value in self._merged_prs_set

    @property
    def pretty_title(self):
        return "PCC{} - {}".format(self.number, self.title)

class BiteChallenge(Challenge):
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self._result = result

    def verify(self, value):
        return value == self._result

    @property
    def pretty_title(self):
        return "Bite {}. {}".format(self.number, self.title)

