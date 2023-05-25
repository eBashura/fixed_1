# Создать файл classes09.py. Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода.

class vaccum_cleaner:
    def __init__(self, brand, model, master):
        self.__brand = brand
        self.__model = model
        self.__master = master

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        self.__master = new_master

    def vacuum_cleaner_on(self):
        print(f'{self.model} is working now!')

    def vacuum_cleaner_off(self):
        print(f'{self.model} is not working now, charge it please!')


class washing_machine:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def washing_machine_speed_of_work(self):
        print(f'{self.model} speed of work is 900!')

    def washing_machine_error(self):
        print(f'{self.model} is damaged, call the service center +375-44-111-222-3 !')


class dishwasher(washing_machine):
    def __init__(self, brand, model, year, working_mode):
        super().__init__(brand, model, year)
        self.__working_mode = working_mode

    @property
    def working_mode(self):
        return self.__working_mode

    @working_mode.setter
    def working_mode(self, new_working_mode):
        self.__working_mode = new_working_mode

    def dishwasher_start(self):
        print(f'{self.model} starts working! Please, wait 60 min till the end!')

    def dishwasher_finish(self):
        print(f'{self.model} finished washing the dishes! Please take them away!')


class robot_vac_clean(vaccum_cleaner):
    def __init__(self, brand, model, master, way_of_cleaning):
        super().__init__(brand, model, master)
        self.__way_of_cleaning = way_of_cleaning

    @property
    def way_of_cleaning(self):
        return self.__way_of_cleaning

    @way_of_cleaning.setter
    def way_of_cleaning(self, new_way_of_cleaning):
        self.__way_of_cleaning = new_way_of_cleaning

    def robot_vac_clean_low_battery_level(self):
        print(f'{self.model} has low battery level! Please, charge it now!')

    def robot_vac_clean_finished_charging(self):
        print(f'{self.model} is fully charged!')


class microwave:
    def __init__(self, brand, model, engine_power):
        self.__brand = brand
        self.__model = model
        self.__engine_power = engine_power

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def engine_power(self):
        return self.__engine_power

    @engine_power.setter
    def engine_power(self, new_engine_power):
        self.__engine_power = new_engine_power

    def microvawe_timer(self):
        print(f'{self.model} timer set for 10 min! Please, wait!')

    def microvawe_finished_defrosting_food(self):
        print(f'{self.model} has finished defrosting food! Turn it off!')


vaccum_cleaner = vaccum_cleaner('Samsung', model='B-170', master='Evgeny')
washing_machine = washing_machine('Bosch', model='A-90', year=2022)
dishwasher = dishwasher('Beko', model='S-177', year=2019, working_mode=5)
robot_vac_clean = robot_vac_clean('Apple', model='E-69', master='Olya', way_of_cleaning='wet')
microwave = microwave('Philips', model='Z-95', engine_power=1600)

vaccum_cleaner.vacuum_cleaner_on()
washing_machine.washing_machine_error()
dishwasher.dishwasher_start()
robot_vac_clean.robot_vac_clean_finished_charging()
microwave.microvawe_finished_defrosting_food()
