# web-search

联网搜索，支持多种web搜索，便于后续大模型和知识库使用

## 安装

你可以使用pip来安装这个包：

```bash
pip install web-search
```

## 使用方法

以下是基本的使用示例：

```python
from web_search import WebSearch

# bing搜索必须传
cookie = "xxx"


# 创建搜索实例
searcher = WebSearch()

# 执行搜索
results = searcher.search("python programming", cookie=cookie)
for result in results:
    print(f"logo：{result['logo']}")
    print(f"网站：{result['website']}")
    print(f"标题：{result['title']}")
    print(f"链接：{result['link']}")
    print(f"摘要：{result['detail']}")
    print(f"日期：{result['date']}")
    print("-" * 50)

# 获取搜索建议
suggestions = searcher.get_suggestions("python prog")
print("Suggestions:", suggestions)
```

## 功能特点

- 简单易用的API
- 支持自定义搜索参数
- 提供搜索建议功能
- 适配大模型和知识库使用场景

## 开发

### 安装开发依赖

```bash
pip install -e .
```

### 运行测试

```bash
python -m unittest discover tests
```

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。
