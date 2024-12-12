from datetime import datetime
    
class Post:
    def __init__(self, platform: str , post: str , author: str , date: datetime):
        self.platform = platform
        self.post = post
        self.author = author
        self.date = date

# Example usage
