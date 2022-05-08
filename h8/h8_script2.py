import json

from h8_script1 import Person
from typing import List, Dict


def create_persons_from_dict(ldict: List[Dict]) -> List[Person]:
    return [Person(**item) for item in ldict]


def read_file(file_name):
    with open(file_name) as f:
        people = json.load(f)
    return people


if __name__ == '__main__':
    people_data = read_file('h8_people.json')
    people = create_persons_from_dict(people_data)
    for person in people:
        print(person)