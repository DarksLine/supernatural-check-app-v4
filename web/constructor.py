from random import randint
import json


class User:
    def __init__(self, number=None):
        self.user_number = number


class Psychic:
    def __init__(self, number=None):
        self.guess_number = number

    def predict_number(self):
        number = randint(10, 99)
        self.guess_number = number


class Psy:
    # Создать и вернуть список экстрасенсов
    @classmethod
    def create_psychic(cls, count_psychics):
        list_psychics = []
        for person in range(count_psychics):
            list_psychics.append(Psychic())

        return list_psychics

    # Получить результаты предположений
    @classmethod
    def get_predict_psychics(cls, list_psychic):
        for obj in list_psychic:
            obj.predict_number()


# Класс-миксин для подсчета процента достоверности предсказаний
class PercentMixin:
    @classmethod
    def percent(cls, request, predict, mind):
        success = request.session["success"]
        for element in predict:
            if predict.get(element) == mind:
                success[element] = success[element] + 1

        percent = {'num1': 0, 'num2': 0, 'num3': 0}
        for element in percent:
            percent[element] = int((success.get(element) / request.session["iter"]) * 100)
        request.session["success"] = success
        return percent


class Storage:
    @classmethod
    def check_data(cls, request):
        if 'save_data' in request.session:
            return True

    @classmethod
    def create(cls, request, count_psychic):
        object_data = ''
        request.session['save_data'] = {
            'count_psy': count_psychic,
            'list_person': object_data
        }

    @classmethod
    def get_n_psychics(cls, request):
        return request.session['save_data']['count_psy']

    #############################################################
    @classmethod
    def save_list(cls, request, psy_list):
        data_list = json.dumps(psy_list)
        request.session['save_data']['list_person'] = data_list
    #############################################################

    @classmethod
    def update_list(cls, request, number):
        data_list = request.session['save_data']['list_person']
        psy_list = json.loads(data_list)

        psy_list.append(User(number))

        data_list_update = json.dumps(psy_list)
        request.session['save_data']['list_person'] = data_list_update

    @classmethod
    def get_complete_list(cls, request):
        master_list = []

        data_list = request.session['save_data']['list_person']
        current_list = json.loads(data_list)

        master_list.append(current_list)
        return master_list
