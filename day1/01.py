import requests

print("欢迎使用中国移动商城搜索功能")
while True:
    key = input("请输入关键字(输入'q'或'Q'退出): ")

    if key == 'q' or key == 'Q':
        break

    try:
        res = requests.post(
            url="https://jf.10086.cn/cmcc-web-shop/search/query",
            data={
                "sortColumn": "default",
                "sortType": "DESC",
                "pageSize": "60",
                "pageNum": "1",
                "firstKeyword": key,
                "integral": "",
                "province": ""
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
            }
        )
        res.raise_for_status()  # 检查请求是否成功
        print(res.json())
    except requests.RequestException as e:
        print(f"搜索过程中发生错误: {e}")

print("结束使用中国移动商城搜索功能")