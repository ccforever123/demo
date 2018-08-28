import json



def search(text):

    with open('bencao.json', 'r', encoding='utf-8') as f:
        content = f.read()
    dict = json.loads(content)
    search_result = []
    for category in dict:
        for title in dict[category]:
            sub_title = dict[category][title][0]
            content =   dict[category][title][1]
            for i in range(4 - len(content)):
                content.append(['附方', '无'])
            if text in sub_title:
                search_result.append((sub_title, content))
            else:
                for i in range(len(content)):
                    if text in content[i][1]:
                        search_result.append((sub_title, content))
    for i in range(len(search_result)):
        print(search_result[i])
        print(search_result[i][0])
        print(search_result[i][1][0][1])
        print(search_result[i][1][1][1])
        print(search_result[i][1][2][1])
        print(search_result[i][1][3][1])
        print('----------------------')
    return search_result


if __name__ == '__main__':
    text = input('Input name:')
    result = search(text)
    for i in result:
        print(i)