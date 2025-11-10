from clases import Movie

class MovieManager:
    def __init__(self):
        self.peliculas = []

    def añadir_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def peliculas_por_productora(self, productora):
        return [p for p in self.peliculas if p.productora == productora]

    def peliculas_con_cadena_titulo(self, cadena):
        cadena = cadena.lower()
        return [p for p in self.peliculas if cadena in p.titulo.lower()]

    def numero_peliculas_mayores_duracion_media(self):
        if not self.peliculas:
            return 0
        media = sum(p.minutos for p in self.peliculas) / len(self.peliculas)
        return sum(1 for p in self.peliculas if p.minutos > media)

    def ordenar_por_duracion(self):
        self.peliculas.sort()



list_movies = [
Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Tim Robbins, Morgan Freeman", "Drama", 142, "Castle Rock Entertainment"),
Movie("The Godfather", 1972, "Francis Ford Coppola", "Marlon Brando, Al Pacino","Drama", 175, "Paramount Pictures"),
Movie("The Dark Knight", 2008, "Christopher Nolan", "Christian Bale, Heath Ledger","Action", 152, "Warner Bros. Pictures"),
Movie("The Lord of the Rings: The Return of the King", 2003, "Peter Jackson", "Elijah Wood, Viggo Mortensen", "Adventure", 201, "New Line Cinema"),
Movie("Pulp Fiction", 1994, "Quentin Tarantino", "John Travolta, Uma Thurman","Crime", 154, "Miramax Films"),
Movie("Forrest Gump", 1994, "Robert Zemeckis", "Tom Hanks, Robin Wright", "Drama",142, "Paramount Pictures"),
Movie("Inception", 2010, "Christopher Nolan", "Leonardo DiCaprio, Joseph Gordon-Levitt", "Action", 148, "Warner Bros. Pictures"),
Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "Keanu Reeves, Laurence Fishburne", "Action", 136, "Warner Bros. Pictures"),
Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "Jodie Foster, Anthony Hopkins", "Crime", 118, "Orion Pictures"),
Movie("The Departed", 2006, "Martin Scorsese", "Leonardo DiCaprio, Matt Damon","Crime", 151, "Warner Bros. Pictures"),
Movie("The Prestige", 2006, "Christopher Nolan", "Christian Bale, Hugh Jackman","Drama", 130, "Warner Bros. Pictures"),
Movie("The Green Mile", 1999, "Frank Darabont", "Tom Hanks, Michael Clarke Duncan","Drama", 189, "Castle Rock Entertainment"),
Movie("The Godfather: Part II", 1974, "Francis Ford Coppola", "Al Pacino, Robert De Niro", "Drama", 202, "Paramount Pictures"),
Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson","Elijah Wood, Ian McKellen", "Adventure", 178, "New Line Cinema"),
Movie("The Lord of the Rings: The Two Towers", 2002, "Peter Jackson", "Elijah Wood, Viggo Mortensen", "Adventure", 179, "New Line Cinema"),
Movie("The Dark Knight Rises", 2012, "Christopher Nolan", "Christian Bale, Tom Hardy","Action", 164, "Warner Bros. Pictures"),
Movie("The Lord of the Rings: The Two Towers", 2002, "Peter Jackson", "Elijah Wood,Viggo Mortensen", "Adventure", 179, "New Line Cinema"),
Movie("One Flew Over the Cuckoo's Nest", 1975, "Milos Forman", "Jack Nicholson, Louise Fletcher", "Drama", 133, "Fantasy Films"),
Movie("Goodfellas", 1990, "Martin Scorsese", "Robert De Niro, Ray Liotta", "Crime",146, "Warner Bros. Pictures")
]

# Crear instancia de MovieManager
manager = MovieManager()

# Añadir todas las películas de la lista
for peli in list_movies:
    manager.añadir_pelicula(peli)

# 1. Películas de una productora concreta
print("Películas de Warner Bros. Pictures:")
for p in manager.peliculas_por_productora("Warner Bros. Pictures"):
    print(p)

# 2. Películas que contienen 'Dark' en el título
print("\nPelículas que contienen 'Dark' en el título:")
for p in manager.peliculas_con_cadena_titulo("Dark"):
    print(p)

# 3. Número de películas que superan la duración media
num_mayores = manager.numero_peliculas_mayores_duracion_media()
print(f"\nNúmero de películas con duración mayor que la media: {num_mayores}")

# 4. Ordenar películas por duración y mostrar las 5 primeras
manager.ordenar_por_duracion()
print("\nLas 5 películas más cortas ordenadas por duración:")
for p in manager.peliculas[:5]:
    print(f"{p.titulo} - {p.minutos} minutos")