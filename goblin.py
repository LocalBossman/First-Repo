from character import Character

class Goblin (Character):
    def __init__(self):
        super().__init__()
        print("This is the enemy class")

        self.max_health = 75
        self.stats = {
            "name": "goblin",
            "strength": 3,
            "health": 75.0
        }

        self.inventory = ["gold"]

    def print_stats(self):
        print("Your stats are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    print(f"{print_stats}")

