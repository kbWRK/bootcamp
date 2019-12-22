class Employee:
    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self._salary_to_pay = 0
        self.time = 0

    def register_time(self, time):
        if time > 8:
            self._salary_to_pay += 8 * self.rate_per_hour
            self._salary_to_pay += (time - 8) * 2 * self.rate_per_hour
        else:
            self._salary_to_pay += time * self.rate_per_hour

    def pay_salary(self):
        result = self._salary_to_pay
        self._salary_to_pay = 0
        return result
class PremiumEmployee(Employee):
    def __init__(self , name, last_name, rate_per_hour):
        super().__init__(name, last_name, rate_per_hour)
        self._bonuses = 0

    def given_bonus(self,bonus):
        self._bonuses += bonus

    def
# if __name__ == "__main__":
#     employee = PremiumEmployee("jan", "nowak", 100.0)
#     employee.register_time(10)
#     print(employee.pay_salary())
#     employee.register_time(5)
#     employee.register_time(5)
#     employee.register_time(5)
#     print(employee.pay_salary())
#     print(employee.pay_salary())
#     employee.register_time(5)
#     print(employee.pay_salary())
