def move_items(num_items: int, start: list, end: list):
    items = start.pop(-num_items:)
    end.append(items)
    return start, end

if __name__=="__main__":
    print(move_items(2, [1,2,3], [4,5,6]))
