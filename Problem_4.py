class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if not group:
        return False

    if user in group.get_users():
        return True

    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

user1 = "user1"
sub_child.add_user(user1)

user2 = "user2"
child.add_user(user2)

child.add_group(sub_child)
parent.add_group(child)

user_to_find = "user1"
group_to_search = parent
result = is_user_in_group(user_to_find, group_to_search)
print(result)  # Output: True

user_to_find = "user2"
group_to_search = sub_child
result = is_user_in_group(user_to_find, group_to_search)
print(result)  # Output: False

user_to_find = "user2"
group_to_search = child
result = is_user_in_group(user_to_find, group_to_search)
print(result)  # Output: True

user_to_find = "Mike_Tyson"
group_to_search = parent
result = is_user_in_group(user_to_find, group_to_search)
print(result)  # Output: False

user_to_find = ""
group_to_search = parent
result = is_user_in_group(user_to_find, group_to_search)
print(result)  # Output: False