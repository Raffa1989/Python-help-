**ЗАДАЧА №1. Словари.**
-
Вы работаете в автосалоне и храните данные об автомобиле в словаре:
```py
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
} 
```
Ваша программа должна принимать ключ в качестве входных данных и выводить соответствующее значение.


**ЗАДАЧА №2. Функции словаря.**
-
Вы работаете с данными, отражающими рейтинг экономической свободы по странам.
Каждое название страны и ранг хранятся в словаре, где ключом является название страны.
```py
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
```
Завершите программу, чтобы взять название страны в качестве входных данных и вывести соответствующий рейтинг экономической свободы.
Если указанное название страны отсутствует в данных, выведите «Not found».
Используйте метод словаря get(), который позволяет указать значение по умолчанию.


**ЗАДАЧА №3. Кортежи**
-
Вам предоставляется список контактов, где каждый контакт представлен кортежем с именем и возрастом контакта.
Завершите программу, чтобы получить строку на вход, найти имя в списке контактов и вывести возраст контакта в формате, представленном ниже:

**Sample Input**
John

**Sample Output**
John is 31

Если контакт не найден, программа должна вывести «Not found».
