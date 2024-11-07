import psycopg2

from src.config import config
from src.data_base_control import (create_database, save_data_to_database_emp,
                                   save_data_to_database_vac)
from src.DBManager import DBManager
from src.get_request import get_employee_data, get_vacancies_data


def main():
    params = config()

    data_emp = get_employee_data()
    data_vac = get_vacancies_data()
    create_database("hh", params)
    save_data_to_database_emp(data_emp, "hh", params)
    save_data_to_database_vac(data_vac, "hh", params)
    db_manager = DBManager(params)

    print(
        "Привет. Выберите, что хотите увидеть:\n"
        "1 - список всех компаний и количество вакансий у каждой компании.\n"
        "2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n"
        "3 - среднюю зарплату по вакансиям\n"
        "4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
        "5 - список всех вакансий, в названии которых содержатся переданные в метод слова, например python."
    )

    user_input = input("Введите число: ")
    if user_input == 1:
        companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
        print(
            f"Список всех компаний и количество вакансий у каждой компании {companies_and_vacancies_count}"
        )

    elif user_input == 2:
        all_vacancies = db_manager.get_all_vacancies()
        print(
            f"Список всех вакансий "
            f"с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию {all_vacancies}"
        )

    elif user_input == 3:
        avg_salary = db_manager.get_avg_salary()
        print(f"Среднюю зарплату по вакансиям {avg_salary}")

    elif user_input == 4:
        vacancy_salary = db_manager.get_vacancies_with_higher_salary()
        print(
            f"Список всех вакансий, у которых зарплата выше средней по всем вакансиям {vacancy_salary}"
        )

    elif user_input == 5:
        vacancy_with_keybord = db_manager.get_vacancies_with_keyword(
            conn=psycopg2.connect(dbname="hh", **params), keyword="Флорист"
        )

        for vacancy in vacancy_with_keybord:
            print(
                f"Список всех вакансий,"
                f" в названии которых содержатся переданные в метод слова, например python {vacancy}"
            )
    else:
        print("Не верный запрос")


if __name__ == "__main__":
    main()
