# coding="utf-8"
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
obj = \
"""
{
"姓名":"张三",
"住处":["天朝", "挖煤国", "万恶的资本主义日不落帝国"],
"宠物":null,
"兄弟":
[
{"姓名": "李四", "年龄": 25, "宠物": "汪星人"},
{"姓名": "王五", "年龄": 23, "宠物": "喵星人"}
]
}
"""
import json
result= json.loads(obj)
result
