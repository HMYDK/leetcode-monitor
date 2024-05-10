### 项目简介
该项目用于查询LeetCode用户每日提交数，并支持将结果发送到指定地址。 

### 项目说明
- 获取LeetCode用户提交数据
- 将结果发送到指定终端
- 支持github action定时执行，发送监控消息
- 支持docker部署，实现自定义时间发送监控消息

### 目前支持的消息终端：
- ✅指定webhook url
- ✅telegram bot


### 使用方法
1.克隆项目

`git clone https://github.com/HMYDK/leetcode-monitor.git`

2.修改users列表，添加要查询的用户

`修改config.json文件中的users列表`

3.修改`config.json`中最后发送结果的webhook地址

4.运行脚本

`python monitor.py`

5.借助github action定时执行程序，发送监控消息

- 修改`.github/workflows/python-app.yml`中的`cron`



### 注意事项
- LeetCode官方API可能会限制请求频率，请勿频繁调用
- 需要提前准备好钉钉机器人webhook地址

### 示例输出
![image](https://github.com/HMYDK/leetcode-monitor/assets/27269137/9867d903-2b67-413c-b67f-463fa51fce37)


### 贡献
欢迎大家对项目进行贡献，包括：
- 提出新的功能建议
- 修复代码中的bug
- 完善项目文档

### 许可
本项目采用MIT开源许可证，欢迎自由使用和修改。
