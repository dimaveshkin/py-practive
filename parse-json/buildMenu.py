import json
from pprint import pprint as pp

MENU_INDENTATION = 4
result_str = ''


def get_menu_item_by_id(list, id):
    menu = [menu for menu in data if menu['id'] == id]
    return menu[0]


def buildMenuTree(list, id="EQ", title="Master Menu", indent=0, options=""):
    menu = get_menu_item_by_id(list, id)

    result_str = " ".join([indent * MENU_INDENTATION * " ",
                           options,
                           menu["id"],
                           title.strip(),
                           "\n"])

    for item in menu["items"]:
        subMenu = item["subMenu"]
        if len(subMenu) > 0:
            title = item["title"]
            options = "-".join([options, item["option"]])
            result_str += buildMenuTree(list, subMenu, title, indent + 1, options)

    return result_str


with open("menu.json") as json_data, open("list.txt", "w") as list:
    data = json.load(json_data)
    list.write(buildMenuTree(data))

