import requests as requests
import re
import json


if __name__ == "__main__":
    not_ai_curators = []
    curators = []
    offset = 0
    max_offset = 1000
    while offset <= max_offset:

        strhtml = requests.get(f'https://store.steampowered.com/curators/ajaxgetcurators//?query=&start={offset}&count=50&dynamic_data=&filter=all&appid=0')
        result_html = strhtml.json()['results_html']

        g_rgTopCurators_origin = re.findall(r'var g_rgTopCurators = \[\{\".*\}\]\;', result_html)[0]
        start = len('var g_rgTopCurators = ')
        end = 1
        l = len(g_rgTopCurators_origin)
        g_rgTopCurators = g_rgTopCurators_origin[start:l - end]
        g_rgTopCurators = json.loads(g_rgTopCurators)
        for curator in g_rgTopCurators:
            if curator['curator_description'].find('AI') == -1:
                not_ai_curators.append(curator['clanID'])
                print(curator['name'] + ' is not AI game curator')
                continue
            curators.append(curator['clanID'])
        offset = offset + 50
    print('结束，一共有' + str(len(curators)) + '个AI游戏策展人')
    print('结束，一共有' + str(len(not_ai_curators)) + '不是AI游戏策展人')
    print(curators)



