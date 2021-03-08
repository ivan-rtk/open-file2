def create_cook_book():
    keys = ['ingridient_name', 'quantity', 'measure']
    cook_book_dict = {}
    with open('recipies.txt', encoding='utf-8') as text:
        lines = []
        for line in text:
            line = line.strip()
            if line:
                lines.append(line)
            continue
        lines = iter(lines)
        for name in lines:
            cook_book_dict[name] = []
            num = next(lines)
            for _ in range(int(num)):
                sostav_line = next(lines)
                ingrid = sostav_line.split(' | ')
                z = zip(keys, ingrid)
                sostav_dict = {k: v for (k, v) in z}
                cook_book_dict[name].append(sostav_dict)
                continue
            continue
    return cook_book_dict

def get_shop_list_by_dishes(dishes, person_count):
    keys = ['measure', 'quantity']
    cook_book_dict = create_cook_book()
    dishes_dict = {}
    for d in dishes:
        for i in cook_book_dict:
            if i == d:
                for j in cook_book_dict[i]:
                    ingridient = j['ingridient_name']
                    dishes_dict[ingridient] = []
                    t = j['measure'], int(j['quantity'])*person_count
                    z = zip(keys, t)
                    ration = {k: v for (k, v) in z}
                    dishes_dict[ingridient].append(ration)
    print(dishes_dict)

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'],3)