from dao.id_generator_int import IdGeneratorInt
from dao.id_generator_uuid import IdGeneratorUuid
from dao.repository import Repository
from entity.person import Person


def print_all_persons(repo):
    # print()
    # it1 = iter(repo)
    # it2 = iter(repo)
    # try:
    #     while True:
    #         p1 = next(it1)
    #         p2 = next(it2)
    #         print(p1.get_formatted_str())
    #         print(p2.get_formatted_str())
    # except StopIteration:
    #     pass
    print()
    for p in repo:
        print(p.get_formatted_str())
    print(f'Number of persons: {len(repo)}')


if __name__ == '__main__':
    p1 = Person('Ivan', 'Petrov', 25)
    p2 = Person('Dimitar', 'Hristov', 35)
    p3 = Person('Maria', 'Georgieva', 27)
    p4 = Person('Ivan', 'Petrov', 42)
    persons = [p1, p2, p3, p4]

    id_gen = IdGeneratorUuid()
    persons_repo = Repository(id_gen)
    for p in persons:
        persons_repo.create(p)
    print_all_persons(persons_repo)

    # second: Person = persons_repo.find_by_id(2)
    # second.f_name = 'Mitko'
    # persons_repo.update(second)
    # persons_repo.delete_by_id(1)
    # print_all_persons(persons_repo)

    other_repo = Repository(id_gen)
    other_repo.create(Person('John', 'Smith', 39))
    other_repo.create(Person('Johanna', 'Harrison', 27))
    print_all_persons(other_repo)

    persons_repo += other_repo
    print_all_persons(persons_repo)

    # comparing persons
    p5, p6 = other_repo.find_all()
    print(p5, p6, p5 > p6, sep="\n")
    print(p5._Person__type_name)

    # properties demo
    p1.l_name = "Doe" # LValue
    name = p1.f_name + " " + p1.l_name # RValue
    print(name)
    del p1.l_name
