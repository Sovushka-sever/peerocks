import json
from itertools import chain

from django.shortcuts import (
    render,
)
from django.views import (
    View,
)

from recipes.models import Recipe, UserRecipe, CookStep, RecipeProduct


class Task1View(View):
    """
    Вывести список всех рецептов. Список должен содержать информацию о самом рецепте, авторе
    """

    def get(self, request, **kwargs):

        queryset_recipe_all = Recipe.objects.all()
        result = []
        for query in queryset_recipe_all:
            author = UserRecipe.objects.filter(recipe=query).values_list('user').distinct()
            result.append((query, list(author)))

        data = {
            'response': result,
        }

        return render(request, 'task.html', {'json_data': data})


class Task2View(View):
    """
    Вывести детальную информацию рецепта. Нужно получить информацию о самом рецепте, о шагах приготовления, списке
    необходимых продуктов для приготовления
    """

    def get(self, request, **kwargs):

        queryset_cookstep_all = CookStep.objects.all().values_list()
        queryset_recipeproduct_all = RecipeProduct.objects.all().values_list()


        all_list = list(chain(queryset_cookstep_all, queryset_recipeproduct_all))

        # (query1 | query2).distinct()

        data = {
            'response': all_list,
        }

        return render(request, 'task.html', {'json_data': data})


class Task3View(View):
    """
    Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 3',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})


class Task4View(View):
    """
    Вывести объединенный список TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонке - Автор или Пользователь.
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 4',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})


class Task5View(View):
    """
    Все продукты указаны для приготовления одной порции блюда. Необходимо вывести список необходимых продуктов для
    приготовления самостоятельно выбранного блюда в количестве 5-ти порций
    """

    def get(self, request, **kwargs):
        data = {
            'response': 'some data task 5',
        }

        return render(request, 'task.html', {'json_data': json.dumps(data)})



