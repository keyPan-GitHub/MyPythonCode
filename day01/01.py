import requests

print("欢迎使用京东搜索引擎")
while True:
    key = input("请输入关键字: ")

    if key == 'q' or key == 'Q':
        break

    res = requests.post(
        url="https://jf.10086.cn/cmcc-web-shop/search/query",
        json={
            "sortColumn": "default",
            "sortType": "DESC",
            "pageSize": "60",
            "pageNum": "1",
            "firstKeyword": key,
            "integral": "",
            "province": ""
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}
    )

    print(res.text)
print("结束使用京东搜索引擎")
