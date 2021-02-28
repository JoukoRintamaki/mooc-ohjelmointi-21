def tee_tuple(x: int, y: int, z: int):
    teeTuple = (min(x, y, z), max(x, y, z), x+y+z)
    return teeTuple


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))
