class Video():

    def __init__(self, title: str, description: str, length: int):
        self.title = title
        self.description = description
        self.length = length
        
    def clickLike(self, name: str):
        print(f"{name} 對影片 \"{self.title}\" 按讚")