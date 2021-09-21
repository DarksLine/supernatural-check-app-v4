from django.shortcuts import render, redirect
from .constructor import *
from django.views.generic import View


class InitialView(View):
    @classmethod
    def get(cls, request):
        if Storage.check_data(request):
            return redirect('/testing')
        return render(request, 'initial.html')

    @classmethod
    def post(cls, request):
        count = int(request.POST['count'])
        Storage.create(request, count)
        return redirect('/testing')


class TestingView(View):
    @classmethod
    def get(cls, request):
        count_psy = Storage.get_n_psychics(request)
        list_psychics = Psy.create_psychic(count_psy)
        full_list = Psy.get_predict_psychics(list_psychics)
        Storage.save_list(request, full_list)
        return render(request, 'testing.html')

    @classmethod
    def post(cls, request):
        user_number = int(request.POST['answer'])
        Storage.update_list(request, user_number)
        return redirect('/result')


class ResultView(View):
    @classmethod
    def get(cls, request):
        master_list = Storage.get_complete_list(request)
        return render(request, 'result.html', {'dict_res': master_list})
