# Solution to [The Captain's Room](https://www.hackerrank.com/challenges/py-the-captains-room)


def get_room_nums() -> tuple:
    """returns tuple representing people's rooms.

    Returns:
        tuple: rooms.
    """
    _ = input() 
    return map(int, input().split())


def main():
    rooms = get_room_nums()

    room_dict = dict()
    for room in rooms:
        if room in room_dict.keys():
            room_dict[room] = room_dict[room] + 1
        else:
            room_dict[room] =1

    print( min(room_dict, key = room_dict.get))


if __name__ == "__main__":
    main()

