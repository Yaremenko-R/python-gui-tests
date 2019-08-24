from random import randrange


def test_del_some_group(app):
    if app.group.get_group_list() == 0:
        app.group.add_new_group("new group")
    old_list = app.group.get_group_list()
    index = randrange(len(old_list))
    app.group.del_some_group(index)
    new_list = app.group.get_group_list()
    old_list.remove(old_list[index])
    assert sorted(old_list) == sorted(new_list)