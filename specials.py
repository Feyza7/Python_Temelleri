class Movie():
    def __init__(self,title, director, duraction):
        self.title = title
        self. director = director
        self. duraction = duraction
        print('Movie objesi oluşturuldu')

    def __str__(self):
        return f'{self.title} by {self.director}'
    
    def __len__(self):
        return self.duraction
    
    def __del__(self):
        print('film silindi')

m = Movie('Inception','Christopher Nolan', 148)

print(str(m))
print(len(m))


