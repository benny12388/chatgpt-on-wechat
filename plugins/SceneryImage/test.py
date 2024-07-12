import requests

# 新的JSON格式接口地址
api_url = "https://api.vvhan.com/api/wallpaper/views?type=json"

# 发送请求获取JSON响应
response = requests.get(api_url)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON格式的响应数据
    image_data = response.json()
    if image_data.get("success"):
        # 获取图片URL
        image_url = image_data.get("url")
        # 发送请求下载图片
        response = requests.get(image_url)
        if response.status_code == 200:
            # 打开文件准备写入
            with open('1.jpg', 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download image, status code: {response.status_code}")
    else:
        print("API response does not indicate success.")
else:
    print(f"Failed to fetch image data, status code: {response.status_code}")
