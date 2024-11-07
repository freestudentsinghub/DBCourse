import json

import requests

employer_ids = [
    99966,
    78638,
    780654,
    1864790,
    9498120,
    5331842,
    11509664,
    1121474,
    7865,
    2477306,
]


def get_employee_data():
    """
    функция для получения данных о компаниях с сайта HH.ru
    """
    employers = []
    for employer_id in employer_ids:
        url_emp = f"https://api.hh.ru/employers/{employer_id}"
        employer_info = requests.get(
            url_emp,
        ).json()
        employers.append(employer_info)

    with open("employers_data.json", "w", encoding="utf-8") as json_file:
        json.dump(employers, json_file, ensure_ascii=False, indent=4)

    return employers


def get_vacancies_data():
    """
    функция для получения данных о вакансиях с сайта HH.ru
    """
    vacancy = []
    for vacacies_id in employer_ids:
        url_vac = f"https://api.hh.ru/vacancies?employer_id={vacacies_id}"
        vacancy_info = requests.get(url_vac, params={"page": 0, "per_page": 100}).json()
        vacancy.extend(vacancy_info["items"])

    with open("vacancy_data.json", "w", encoding="utf-8") as json_file:
        json.dump(vacancy, json_file, ensure_ascii=False, indent=4)

    return vacancy


# print(get_employee_data())
