### 项目简介
该项目用于查询LeetCode用户每日提交数，并支持将结果发送到钉钉群。

### 使用方法
1.克隆项目

`git clone https://github.com/dijia-light/leetcode-daily-submissions.git`

2.修改users列表，添加要查询的用户

`vim main.py`

3.安装依赖库

pip install -r requirements.txt

4.运行脚本

`python main.py`

5.将钉钉机器人地址填写到dingding_bot.py文件中的webhook变量中

### 项目说明
- 项目使用requests库发送HTTP请求，获取LeetCode用户提交数据
- 使用json库解析JSON格式的响应数据
- 使用datetime库将时间戳转换为日期格式
- 使用dingding_bot库将结果发送到钉钉群

### 注意事项
- LeetCode官方API可能会限制请求频率，请勿频繁调用
- 需要提前准备好钉钉机器人webhook地址

### 示例输出
![image](https://github.com/HMYDK/leetcode-monitor/assets/27269137/9867d903-2b67-413c-b67f-463fa51fce37)


### TODO
- 支持查询更多日期的提交数
- 支持其他编程语言的提交数查询

### 贡献
欢迎大家对项目进行贡献，包括：
- 提出新的功能建议
- 修复代码中的bug
- 完善项目文档

### 许可
本项目采用MIT开源许可证，欢迎自由使用和修改。
