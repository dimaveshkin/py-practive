import json
import codecs

MENU_INDENTATION_LEVEL = 4


def get_menu_item_by_id(menu_list, menu_id):
    menu = [menu for menu in menu_list if menu['id'] == menu_id]
    return menu[0]


def build_tree_string(menu_id, title, indent_level, options, tree_trunk="", program_name=""):
    if indent_level != 0:
        indent_str = list(indent_level * MENU_INDENTATION_LEVEL * " ")

        for i in range(0, indent_level):
            change_index = i * MENU_INDENTATION_LEVEL
            indent_str[change_index + 1] = u"┃"

        indent_str = "".join(indent_str)
    else:
        indent_str = ""

    if program_name != "":
        program_name = "| PROGRAM: " + program_name

    if menu_id != "":
        menu_id = " [" + menu_id + "] "
    else:
        menu_id = " "

    return "{0} {1} {2}{3}{4} {5}\n".format(indent_str, tree_trunk, options, menu_id, title.strip(), program_name)[3:]


def build_menu_tree(menu_list, menu_id="EQ", title="Master Menu", indent=0, options="", tree_trunk=""):
    menu = get_menu_item_by_id(menu_list, menu_id)

    result_str = build_tree_string(menu["id"], title, indent, options, tree_trunk)

    for i, item in enumerate(menu["items"]):
        sub_menu = item["subMenu"]
        new_options = [item["option"]]
        if len(options) > 0:
            new_options.insert(0, options)
        new_options = "-".join(new_options)
        item_title = item["title"]
        next_indent_level = indent + 1
        tree_trunk_symb = u"┝" if i != len(menu["items"]) - 1 else u"┕"

        if len(sub_menu) > 0:
            result_str += build_menu_tree(menu_list, sub_menu, item_title, next_indent_level, new_options,
                                          tree_trunk_symb)
        else:
            program = item.get("program", {
                "name": ""
            })

            result_str += build_tree_string("", item_title, next_indent_level, new_options, tree_trunk_symb, program["name"])

    return result_str


with open("menu.json") as json_data, codecs.open("list.txt", "w", "utf-8") as menu_list_file:
    data = json.load(json_data)
    menu_list_file.write(build_menu_tree(data))

