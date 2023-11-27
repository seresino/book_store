
class Book():

    def __init__(self, id, title, author_name):
        # set attributes corresponding to column names
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"
    
    def dashed_string(self):
        return f"{self.id} - {self.title} - {self.author_name}"