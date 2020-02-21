class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_items = []
        self.exits = []
    def __str__(self):
        output = f"{self.name}\n{self.description}"
        # for exit in self.exits:
        #     output += f'\nExit to the {exit}'
        return output
    exits = []
    linked_items = []