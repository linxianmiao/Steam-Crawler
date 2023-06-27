import requests as requests
import re
import json
import csv


if __name__ == "__main__":
    curators = []
    offset = 0
    max_offset = 1000
    with open('out_put.csv', 'w', encoding='utf-8', errors='ignore') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['clanID', 'name', 'home_page', 'youtube', 'twitter', 'facebook', 'twitch', 'total_followers'])
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
                if curator['curator_description'].find('AI') == -1 and curator['name'].find('AI') == -1:
                    continue
                row = []
                curators.append(curator['clanID'])
                row.append(curator['clanID'])
                row.append(curator['name'])
                row.append(curator['link'])
                if curator.get('youtube', None) is not None:
                    row.append(curator['youtube']['url'])
                else:
                    row.append('null')

                if curator.get('twitter', None) is not None:
                    row.append(curator['twitter']['url'])
                else:
                    row.append('null')

                if curator.get('facebook_page', None) is not None:
                    row.append(curator['facebook']['url'])
                else:
                    row.append('null')
                    
                if curator.get('twitch', None) is not None:
                    row.append(curator['twitch']['url'])
                else:
                    row.append('null')
                row.append(curator.get('total_followers', 0))
                writer.writerow(row)
            offset = offset + 50


