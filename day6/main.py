with open("day6/input.txt") as f:
    message = f.readlines()[0]

class RollingWindow:
    def __init__(self, length: int) -> None:
        self.array = []
        self.length = length
    
    def push(self, item):
        self.array.append(item)
        if len(self.array) > self.length:
            self.pop() 

    def pop(self):
        self.array = self.array[1:]

    def check_for_repetition(self):
        return len(self.array) == len(set(self.array))
        


def find_packet_start(message: str, window_length: int):
    cache = RollingWindow(window_length)

    for i in range(window_length):
        cache.push(message[i])

    for i, char in enumerate(message[window_length:]):

        if not char in cache.array:
            if cache.check_for_repetition():
                return i+window_length+1

        cache.push(char)
    
print("Day 6, Part 1")
print(find_packet_start(message, 3))
print("Day 6, Part 2")
print(find_packet_start(message, 13))