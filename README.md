# DBCourse
## Курсовая работа "Поиск вакансий с подключением БД"

### В данном проекте мы разработали программу, котрая получает данный с сайта hh.ru по 10 компаниям 
### и спроектировали таблицы в БД PostgreSQL и загрузили полученные данные в созданные таблицы.

###  Так же реализовали класс с функциям, которые работают с таблицами

get_companies_and_vacancies_count()
 — получает список всех компаний и количество вакансий у каждой компании.

get_all_vacancies()
 — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.

get_avg_salary()
 — получает среднюю зарплату по вакансиям.


get_vacancies_with_higher_salary()
 — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.


get_vacancies_with_keyword()
 — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.

Все они находяться в модуле DBManager.py

В модуле get_request.py реализованны функции, которые получают данные с сайта hh.ru

В модуле data_base_control.py реализованны функции, которые создают таблицы и записывают в них данные

