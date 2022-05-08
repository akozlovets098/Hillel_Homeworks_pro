from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, dob: date, profession: str, fav_color: str):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.profession = profession
        self.fav_color = fav_color

    def __str__(self):
        return f'{self.first_name} {self.last_name} was born on {self.dob}, works as {self.profession} ' \
               f'and likes {self.fav_color} color'
