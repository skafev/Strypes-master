import re

messages = [
    "Да се научим да работим в колектив. Професии в областта на медицината, биологията, химията, археологията.",
    "Да се научим да поемаме отговорност и преодоляваме трудностите чрез разум. Самостоятелен бизнес, търговски представител, програмист.",
    "Да се научим да ценим и малките успехи в живота. Професии свързани с пътуване, туризъм, усъвършенстване на технологии, търговия.",
    "Да се научим на прецизност в професията. Професии свързани с конструиране, техника, строг ред и дисциплина, спорт.",
    "Да се научим да комуникираме с другите. Професии свързани с преподаване, научна и административна дейност, журналистика и реклама.",
    "Да се научим на безкористност, човеколюбие, безпристрастност. Професии свързани с изкуство, дизайн, художествена гимнастика, поезия, психология.",
    "Да се научим да анализираме. Професии свързани с точна изработка – гравьор, скулптор, градинар, хирург.",
    "Да се научим на взискателност, целеустременост, постоянство. Професии свързани с риск – криминалист, съдебен медик, траурен агент, банкер, медиум.",
    "Да се научим на състрадание, толерантност, благотворителност. Професии свързани с нетрадиционно мислене чрез духовно израстване – пионери във всяка една област, хора, които променят разбиранията ни за света и човечеството.",
]

def reduce_to_digit(number):
    while number > 9:
        number = number // 10 + number % 10
    return number


if __name__ == "__main__":
    # while-True
    while True:
        birth_date = input("Input you birth date [DD.MM.YYYY]:")
        if re.match("^\d{2}\.\d{2}\.\d{4}$", birth_date):
            break
        print("Error: Invalid date. Try again.")
    d, m, y = birth_date.split(".")
    print(f"{m}/{d}/{y}")

    # while-else
    l = birth_date.split(".")
    result = ""
    pos = 0
    while pos < len(l) - 1:
        result += l[pos] + "."
        pos += 1
    else:
        result += l[pos]
    print(result)

    # for-else
    l = birth_date.split(".")
    result = ""
    for i, e in enumerate(l):
        if i < len(l) - 1:
            result += e + "."
    else:
        result += e
    print(result)

    sum = 0
    pos = 0
    while pos < len(birth_date):
        ch = birth_date[pos]
        if ch.isdigit():
            sum += int(ch)
        pos += 1
    my_digit = reduce_to_digit(sum)
    print(f"{my_digit}: {messages[my_digit - 1]}")
