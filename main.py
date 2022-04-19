def cook_book():
    rec_dict = {}
    with open('recipes.txt', 'r', encoding='utf-8') as rec_book:
        rec_list = rec_book.readlines()

    rec_list = (''.join(rec_list)).split('\n')

    ind1 = 0
    ind2 = 1
    for line in rec_list:
        if ind1 == 0:
            rec_i = line
            rec_dict[rec_i] = []
            ind1 = 1
            ind2 = 0
            continue
        if ind2 == 0:
            ind1 = int(line)+1
            ind2 = 1
            continue
        if ind1 > 1:
            list_res = line.split(' | ')
            rec_dict[rec_i] += [{'ingredient_name': list_res[0], 'quantity': int(list_res[1]), 'measure': list_res[2]}]
        ind1 -= 1
    return rec_dict

def get_shop_list(dishes, pc):
    cb = cook_book()
    shop_list = {}
    for dish in dishes:
        for ingr in cb[dish]:
            if ingr['ingredient_name'] in shop_list:
                shop_list[ingr['ingredient_name']][quantity] += ingr['quantity'] * pc
            else:
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * pc}
    return shop_list

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

print(get_shop_list(dishes, person_count))
