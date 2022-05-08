import json
from h8_script1 import Person
from typing import List, Dict
from datetime import date


def convert_persons_to_dict(perslist: List[Person]) -> List[Dict]:
    return [person.__dict__ for person in perslist]


def save_ldict_to_json(ldict: List[Dict], newfile_name) -> None:
    with open(newfile_name, 'w') as f:
        json.dump(ldict, f)


if __name__ == '__main__':
    person1 = Person('Jane', 'Randall', '1989.12.2', 'writer', 'black')
    person2 = Person('John', 'Austin', '1975.9.4', 'musician', 'white')
    person3 = Person('Kate', 'Adams', '1998.12.28', 'waiter', 'purple')
    person4 = Person('Ben', 'Linkoln', '1991.10.13', 'teacher', 'red')
    people = [person1, person2, person3, person4]
    people_dict = convert_persons_to_dict(people)
    save_ldict_to_json(people_dict, 'h8_people_from_dict.json')

