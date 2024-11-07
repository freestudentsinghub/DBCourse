import psycopg2



class DBManager:

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname="hh", **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        self.cur.execute(
            """
        SELECT employers.employer_name, COUNT(vacancy.employer_id)
        FROM employers
        JOIN vacancy ON employers.employer_id = vacancy.employer_id
        GROUP BY employers.employer_name
        ORDER BY COUNT(vacancy.employer_id) DESC;"""
        )

        return self.cur.fetchall()

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        self.cur.execute(
            """
        SELECT employers.employer_name, vacancy_name, salary, vacancy_url
        FROM vacancy
        JOIN employers ON employers.employer_id = vacancy.employer_id
        ORDER BY salary DESC;"""
        )

        return self.cur.fetchall()

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        self.cur.execute(
            """
        SELECT AVG(salary) FROM vacancy;"""
        )

        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        self.cur.execute(
            """
        SELECT vacancy_name, salary 
        FROM vacancy
        WHERE salary > (SELECT AVG(salary) FROM vacancy);"""
        )

        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, conn, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        with self.conn.cursor() as self.cur:
            query = """SELECT * FROM vacancy WHERE vacancy_name ILIKE %s"""

            self.cur.execute(query, (f"%{keyword}%",))

            return self.cur.fetchall()


# params = config()
# db_manager = DBManager(params)
# companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()

# all_vacancies = db_manager.get_all_vacancies()

# avg_salary = db_manager.get_avg_salary()

# vacancy_salary = db_manager.get_vacancies_with_higher_salary()

# vacancy_with_keybord =
# db_manager.get_vacancies_with_keyword(conn=psycopg2.connect(dbname='hhdatabase', **params), keyword='Флорист')
#
# for vacancy in vacancy_with_keybord:
#     print(vacancy)
