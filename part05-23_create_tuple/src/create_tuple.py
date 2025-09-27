def create_tuple(x: int, y: int, z: int):
    elements = [x,y,z]
    tupley = (min(elements), max(elements), sum(elements))
    return tupley

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))