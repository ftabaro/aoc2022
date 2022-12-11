"""
Day 11 puzzle 1
"""

import re
from typing import Pattern, Optional, Tuple


class Monkey:
    """
    A class to model the monkey doing shenanigans!
    """
    def __init__(self):
        self._name = None
        self._items = None
        self._test_value = None
        self.operation = None
        self._dest_monkeys = {
            True: None,
            False: None
        }
        self.throws = 0

    @property
    def name(self):
        """
        Getter method for the name attribute
        """
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = int(name)

    @property
    def items(self):
        """
        Getter method for items attribute
        """
        return self._items

    @items.setter
    def items(self, items: str):
        """
        Setter method for items attribute
        """
        if self._items is None and isinstance(items, str):
            self._items = [int(item.strip()) for item in items.split(', ')]

    @property
    def test_value(self):
        """
        Getter method for test_value attribute
        """
        return self._test_value

    @test_value.setter
    def test_value(self, test_value: str):
        """
        Setter method for the test_value attribute
        """
        self._test_value = int(test_value)

    @property
    def dest_monkeys(self):
        """
        Getter method for dest_monkeys attribute
        """
        return self._dest_monkeys

    @dest_monkeys.setter
    def dest_monkeys(self, dest_monkeys: Tuple[str, str]):
        key = dest_monkeys[0]
        key = eval(key)

        value = dest_monkeys[1]
        value = int(value)

        self._dest_monkeys[key] = value

    def add_item(self, item: int):
        """
        A method to receive items one by one adding them to the end of the 
        _items list
        """
        self._items.append(item)

    def inspect_item(self, cap: int):
        """
        A method to perform the inspection calculating the new worry level of 
        items
        """
        while len(self._items) > 0:
            old_worry_level = self._items.pop(0)

            operation = self.operation.replace("old", str(old_worry_level))
            new_worry_level = eval(operation)
            new_worry_level = int(new_worry_level)
            
            # find reminder from least common multiple
            new_worry_level %= cap

            outcome = new_worry_level % self.test_value
            outcome = outcome == 0

            dest_monkey = self.dest_monkeys[outcome]
            
            self.throws += 1
            yield (new_worry_level, dest_monkey)


def get_match(pattern: Pattern[str], line: str) -> Optional[dict]:
    """
    A function to get group dictionaries from a pattern and a target line. 
    Returns none if no match are found.
    """
    match = re.match(pattern, line)
    if match is not None:
        return match.groupdict()
    return None


def main(path: str) -> int:
    """
    Solution to day 11 puzzle 1
    """

    monkey_line = re.compile(r'^Monkey (?P<monkey_name>[0-9]+):$')

    starting_items_line = re.compile(
        r'^Starting items: (?P<starting_items>.*)$'
    )

    operation_line = re.compile(r'^Operation: new = (?P<operation>.*)$')

    test_line = re.compile(r'^Test: divisible by (?P<test_value>[0-9]+)$')

    test_eval_line = re.compile(
        r'^If (?P<test_outcome>true|false): throw to monkey (?P<dest_monkey>[0-9]+)$'
    )

    monkeys = {}

    with open(path, encoding="utf-8") as fin:
        monkey = Monkey()
        for line in fin:
            line = line.strip()
            if line.startswith("Monkey"):
                match = get_match(monkey_line, line)
                monkey.name = match["monkey_name"]

            elif line.startswith("Starting"):
                match = get_match(starting_items_line, line)
                monkey.items = match["starting_items"]

            elif line.startswith("Operation"):
                match = get_match(operation_line, line)
                monkey.operation = match["operation"]

            elif line.startswith("Test"):
                match = get_match(test_line, line)
                monkey.test_value = match["test_value"]

            elif line.startswith("If"):
                match = get_match(test_eval_line, line)
                test_outcome = match["test_outcome"]
                test_outcome = test_outcome[0].upper() + test_outcome[1:]
                dest_monkey = match["dest_monkey"]
                monkey.dest_monkeys = (test_outcome, dest_monkey)

            elif line == "":
                monkeys[monkey.name] = monkey
                monkey = Monkey()

    # find least common multiple!
    lcm = 1
    for monkey in monkeys.values():
        lcm *= monkey.test_value

    current_round = 0 
    while current_round < 10000:
        for monkey in monkeys.values():
            for item, dest_monkey in monkey.inspect_item(lcm):
                monkeys[dest_monkey].add_item(item)

        current_round += 1
    
    all_throws = list(
        sorted(
            map(
                lambda monkey: monkey.throws,
                monkeys.values()
            ), reverse=True
        )
    )
    ret = all_throws[0] * all_throws[1]
    print(ret)
    return ret


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
