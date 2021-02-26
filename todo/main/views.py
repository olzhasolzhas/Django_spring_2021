from django.shortcuts import render
import datetime


class User(object):
    def __init__(self, id, created, due_on, owner, mark):
        self.id = id
        self.created = created
        self.due_on = due_on
        self.owner = owner
        self.mark = mark


# all users
user1 = User(1, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=2), 'admin', True)
user2 = User(2, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=2), 'admin', False)
user3 = User(3, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=2), 'admin', False)
user4 = User(4, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=2), 'admin', False)
user5 = User(5, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=2), 'admin', False)
users = (user1, user2, user3, user4, user5)


def todo_list(request):
    context = {'title': 'TODO', 'users': users}
    return render(request, 'todos/todo_list.html', context=context)


def completed(request):
    context = {'title': 'Completed TODO', 'users': users}
    return render(request, 'todos/1/completed/completed_todo_list.html', context=context)
