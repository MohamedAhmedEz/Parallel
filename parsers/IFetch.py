from Data.Shared import SharedList


class SocialMediaFileFetcher:
    def __init__(self, shared_list: SharedList):
        self.shared_list = shared_list

    def parse(self):
        raise NotImplementedError("Subclasses must implement this method")