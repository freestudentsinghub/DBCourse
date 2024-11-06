from src.get_request import (get_employee_data, get_vacancies_data)
from src.data_base_control import create_database, save_data_to_database_emp, save_data_to_database_vac
from config import config
from src.DBManager import DBManager


def main():
    params = config()

    data_emp = get_employee_data()
    data_vac = get_vacancies_data()
    create_database('hhdatabase', params)
    save_data_to_database_emp(data_emp, 'hhdatabase', params)
    save_data_to_database_vac(data_vac, 'hhdatabase', params)
    db_manager = DBManager(params)



if __name__ == '__main__':
    main()