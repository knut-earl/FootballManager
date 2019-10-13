import random


class Player:
    """
    player is on a single team, with other players
    players paly in a game for a team
    """

    def __init__(self, name, skill):
        self.name = name

        # player skill rankings
        self.skill = skill

    def __str__(self):
        return '{}, Skill: {}, Salary: {}'.format(
            self.name, self.skill, self.salary())

    # salary
    def salary(self):
        return 5000 + self.skill * 100


def generate_player():
    first_names = [
        'Olivia', 'Liam', 'Emma', 'Noah', 'Ava', 'Elijah', 'Sophia', 'Oliver', 'Isabella', 'Lucas', 'Amelia', 'Mason',
        'Mia', 'Ethan', 'Charlotte', 'Logan', 'Harper', 'James', 'Aria', 'Aiden', 'Luna', 'Sebastian', 'Evelyn',
        'Jackson', 'Mila', 'Benjamin', 'Ella', 'Carter', 'Avery', 'Mateo', 'Scarlett', 'Alexander', 'Ellie', 'Grayson',
        'Abigail', 'Leo', 'Layla', 'Michael', 'Emily', 'Levi', 'Camila', 'Jacob', 'Sofia', 'Daniel', 'Chloe', 'Jack',
        'Lily', 'Wyatt', 'Zoey', 'Jayden', 'Madison', 'Luke', 'Riley', 'Owen', 'Penelope', 'Julian', 'Grace', 'William',
        'Aurora', 'Henry', 'Nora', 'Gabriel', 'Victoria', 'Jaxon', 'Elizabeth', 'Muhammad', 'Stella', 'Josiah', 'Bella',
        'David', 'Violet', 'Matthew', 'Hannah', 'Asher', 'Nova', 'Ezra', 'Hazel', 'Lincoln', 'Everly', 'Isaiah',
        'Aubrey', 'John', 'Elena', 'Eli', 'Eleanor', 'Adam', 'Paisley', 'Samuel', 'Maya', 'Anthony', 'Skylar', 'Isaac',
        'Emilia', 'Joseph', 'Addison', 'Nathan', 'Eliana', 'Ryan', 'Leah', 'Massaih',
    ]

    first_name = random.choice(first_names)
    last_name = random.choice(first_names)

    full_name = '{} {}'.format(first_name, last_name)

    # generate skill
    skill = 10 + random.randint(0, 90)
    return Player(full_name, skill)