#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Timelapse 汉化脚本：仅替换 UI 显示文本，跳过会被代码读取的输入框/下拉框默认值。"""
import re

# ---- MainForm.h：控件显示文本（英文原文 -> 中文）----
DICT_H = {
    # 菜单
    "File": "文件", "Open Settings": "打开配置", "Save Settings": "保存配置",
    "&Close MapleStory": "关闭冒险岛(&C)", "MapleStory": "冒险岛",
    "Embed MS Window": "嵌入游戏窗口", "Hide MS Window": "隐藏游戏窗口",
    "Pause MS": "暂停游戏", "Inject Dll": "注入DLL", "Help": "帮助", "&About": "关于(&A)",
    # 主面板状态
    "MS Version: 83\\r\\nPrivate Servers": "游戏版本: 83\\r\\n私服",
    "Timelapse Trainer": "Timelapse 修改器", "Waiting...": "等待中...",
    "Map Name:": "地图名称:", "Char Foothold:": "角色踏板:", "Char Animation:": "角色动作:",
    "Walls:": "墙体:", "Test": "测试", "Inactive": "未激活", "Active": "已激活",
    "CharName": "角色名", "Buff Count:": "Buff数量:", "NPC Count": "NPC数量",
    "Mouse Pos:": "鼠标坐标:", "Thread ID: ": "线程ID: ", "Breath Count:": "呼吸数:",
    "Mesos:": "金币:", "Job:": "职业:", "Portal Count": "传送门数量",
    "Item Count:": "物品数量:", "Mob Count: ": "怪物数量: ", "People Count:": "玩家数量:",
    "Attack Count:": "攻击数量:", "Char Pos:": "角色坐标:", "Map ID: ": "地图ID: ",
    "Channel:": "频道:", "World:": "世界:", "EXP:": "经验:", "Level: ": "等级: ", "Info:": "信息:",
    # 标签页
    "Main": "主面板", "Log": "日志", "Auto Login": "自动登录", "Options": "选项",
    "Transparency:": "透明度:", "Bots": "脚本",
    # 自动 Buff
    "Auto Buff": "自动Buff", "Enable All": "全部启用", "Disable All": "全部禁用",
    "Remove Selected": "移除选中", "Clear All": "全部清空", "Add": "添加",
    "Name:": "名称:", "Interval [s]:": "间隔[秒]:", "Name": "名称", "Key": "按键",
    "Interval [ms]": "间隔[毫秒]",
    # 自动换频/商城
    "Auto CC/CS": "自动换频/商城",
    "Exit Cash Shop \\r\\nDelay (ms):": "退出商城\\r\\n延迟(毫秒):",
    "Auto Cash Shop": "自动进商城", "Random Channel": "随机频道", "Specific Channel": "指定频道",
    "Mobs": "怪物", "Cash Shop": "商城", "Attacks": "攻击", "People": "玩家",
    "Change Channel": "换频道", "Time (secs)": "时间(秒)", "Function": "函数方式", "Packet": "封包方式",
    # 自动出售
    "Auto Sell": "自动出售", "Sell All When Inv Full (heuristics)": "背包满时全部出售(智能)",
    "Delay[ms]:": "延迟[毫秒]:",
    # 自动捡物 / 攻击 / 血蓝
    "Items >": "物品 >", "MP <": "MP <", "Auto Loot": "自动捡物", "Mobs >": "怪物 >",
    "HP <": "HP <", "Auto Attack": "自动攻击", "Auto HP": "自动HP", "Auto MP": "自动MP",
    # 功能 I
    "Hacks I": "功能 I", "Physics Hacks": "物理类", "No Walking Friction": "无行走摩擦",
    "Map Hacks": "地图类", "No Blue Boxes": "无碰撞框", "No Map Background": "无地图背景",
    "No Map Tiles": "无地图贴图", "Infinite Chat": "无限聊天", "Map Speed Up": "地图加速",
    "No Map Fade Effect": "无地图淡出效果", "No Map Objects": "无地图物件",
    "Movement Hacks": "移动类", "Mouse Fly [CS]": "鼠标飞行[CS]", "Click Teleport": "点击瞬移",
    "Interval [ms]:": "间隔[毫秒]:", "Mouse Teleport": "鼠标瞬移", "Swim In Air": "空中游泳",
    "Mob Hacks": "怪物类", "Mob Auto Aggro": "怪物自动聚怪", "No Mob Reaction": "怪物无反应",
    "Mob Disarm": "怪物缴械", "Mob Freeze": "冻结怪物", "No Mob Death Effect": "无怪物死亡效果",
    "No Mob Knockback": "怪物无击退", "Item Hacks": "物品类", "Tubi": "Tubi丢物",
    "Instant Drop Items": "瞬间丢弃物品", "Item Vac": "物品吸取", "Instant Loot Items": "瞬间捡取物品",
    "Character Hacks": "角色类", "Delay:": "延迟:", "Blinks:": "闪烁:", "Misses:": "闪避:",
    "Miss Godmode": "闪避无敌", "Attack Delay": "攻击延迟", "Blink Godmode": "闪烁无敌",
    "No Attack Delay": "无攻击延迟", "No Player Name Tag": "无角色名牌", "Full Godmode": "完全无敌",
    "Jump Down Any Tile": "任意地块下跳", "No Skill Effects": "无技能特效", "No Breath": "无呼吸",
    "No Player Knockback": "角色无击退", "Full Accuracy": "完全命中", "No Player Death": "角色不死",
    "Unlimited Attack": "无限攻击",
    # 功能 II
    "Hacks II": "功能 II", "Enable Spawn Control": "启用刷怪控制",
    "Get Current Location": "获取当前坐标", "Spawn Control:": "刷怪控制:", "Map ID:": "地图ID:",
    "Delete": "删除", "Teleport to (x,y)": "瞬移到(x,y)", "Loop": "循环", "Teleport": "瞬移",
    "Add to List": "添加到列表", "Vacs": "吸怪", "CSEAX Vac": "CSEAX吸怪", "pVac": "pVac吸怪",
    "Fangor Vac": "Fangor吸怪", "Vac Jump Left": "吸怪左跳", "Vac Jump Right": "吸怪右跳",
    "Vac Left": "向左吸怪", "ZZ Vac": "ZZ吸怪", "Full Map Attack": "全图攻击",
    "Vac Right": "向右吸怪", "Vac Force Right": "强制向右吸怪", "Foothold No:": "踏板编号:",
    "Get Foothold": "获取踏板", "Range Y:": "范围Y:", "Range X:": "范围X:", "Wall Vac": "靠墙吸怪",
    "When Items >": "当物品 >", "Kami Loot": "Kami捡物", "When Mobs >": "当怪物 >",
    # 过滤器
    "Filters": "过滤器", "Log Mobs": "记录怪物", "Clear": "清空", "WhiteList": "白名单",
    "BlackList": "黑名单", "Search:": "搜索:", "Add by ID:": "按ID添加:",
    "Filters Mobs on Spawn": "刷怪时过滤怪物", "Enable Mob Filter": "启用怪物过滤",
    "Log Items": "记录物品", "Mesos <=": "金币 <=", "Enable Item Filter": "启用物品过滤",
    # 封包
    "Packets": "封包", "Send": "发送", "Spam Delay\\r\\n [ms]:": "连发延迟\\r\\n[毫秒]:",
    "Spam": "连发", "Remove": "移除", "Block Header": "拦截封包头", "Enable Log": "启用日志",
    "Send Packet": "发送封包", "Recv": "接收", "Receive Packet": "接收封包",
    "Multi Packet": "多封包", "Defined Packets": "预设封包",
    # 杂项 / 一键功能
    "In USE slot:": "在消耗栏位:", "Nearest": "最近", "To Town:": "回城:",
    "Use Return Scroll": "使用返回卷轴", "Revive": "复活", "Restore 127 Health": "恢复127血量",
    "Auto Distributes Per \\r\\nEach Level till AP < 5\\r\\n": "每级自动分配\\r\\n直到AP < 5\\r\\n",
    "Till Level:": "直到等级:", "Auto AP": "自动加点", "Suicide": "自杀",
    "Drop 50,000 Mesos": "丢弃50,000金币", "Drop 1000 Mesos": "丢弃1000金币",
    "Get On Mount": "上坐骑", "Drop 10 Mesos": "丢弃10金币", "Drop 10,000 Mesos": "丢弃10,000金币",
    "Map Rusher": "跑图", "Delay [ms]:": "延迟[毫秒]:", "Destination Map ID:": "目标地图ID:",
    "Map Rush": "开始跑图",
    # 自动登录
    "Skip Logo": "跳过Logo", "Username:": "用户名:", "Character:": "角色:", "Password:": "密码:",
}

# 这些控件名前缀的 Text 会被业务代码读取(按键名/数值/世界名等)，绝对不能翻译
SKIP_PREFIX = ("tb", "combo")

def fix_h(path):
    raw = open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig" if bom else "utf-8", errors="replace")
    pat = re.compile(r'(this->(\w+)->(?:Text|ToolTipText|HeaderText) = L")((?:[^"\\]|\\.)*)(")')
    cnt = [0]
    def repl(m):
        head, name, val, tail = m.group(1), m.group(2), m.group(3), m.group(4)
        if name.startswith(SKIP_PREFIX):
            return m.group(0)
        # 跑图状态标签带大量尾随空格，单独归一化处理
        if val.rstrip() == "Status: Waiting...":
            cnt[0] += 1
            return head + "状态: 等待中..." + tail
        if val in DICT_H:
            cnt[0] += 1
            return head + DICT_H[val] + tail
        return m.group(0)
    out = pat.sub(repl, text)
    data = out.encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    open(path, "wb").write(data)
    print("MainForm.h 替换 %d 处 (BOM=%s)" % (cnt[0], bom))

# ---- MainForm.cpp：弹窗 / 运行时标题（英文 -> 中文），窄字符串补 L 前缀 ----
DICT_CPP = {
    "A save file has been detected, load save?": "检测到存档文件，是否载入？",
    "Save File": "存档文件",
    "Error: Attack Interval textbox cannot be empty": "错误：攻击间隔输入框不能为空",
    "Error: Loot Interval textbox cannot be empty": "错误：捡物间隔输入框不能为空",
    "Error: Buff Interval textbox cannot be empty": "错误：Buff间隔输入框不能为空",
    "Error: CS Delay textbox cannot be empty": "错误：商城延迟输入框不能为空",
    "Error: Attack delay textbox cannot be empty": "错误：攻击延迟输入框不能为空",
    "Error: The teleport x and y textboxes cannot be empty": "错误：瞬移的X和Y输入框不能为空",
    "Error: Spawn Control Map ID, x, and y textboxes cannot be empty": "错误：刷怪控制的地图ID、X、Y输入框不能为空",
    "Error: Map ID cannot be 0": "错误：地图ID不能为0",
    "Error: Two spawn points can not exist for the same map ID.": "错误：同一地图ID不能存在两个刷怪点。",
    "Warning: Bans": "警告：可能导致封号",
    "Please enter mesos value ranging from 0 to 50,000. Default: 0": "请输入0到50,000之间的金币值。默认：0",
    "Item ID not found": "未找到物品ID",
    "Mob ID not found": "未找到怪物ID",
    "Error: Couldn't load map data": "错误：无法加载地图数据",
    "Error! Empty string was returned": "错误！返回了空字符串",
    "Timelapse Trainer - PID: ": "Timelapse 修改器 - PID: ",
}

def fix_cpp(path):
    raw = open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig" if bom else "utf-8", errors="replace")
    cnt = 0
    for eng, chn in DICT_CPP.items():
        src = '"' + eng + '"'
        dst = 'L"' + chn + '"'
        n = text.count(src)
        if n:
            text = text.replace(src, dst)
            cnt += n
    data = text.encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    open(path, "wb").write(data)
    print("MainForm.cpp 替换 %d 处 (BOM=%s)" % (cnt, bom))

if __name__ == "__main__":
    fix_h("Timelapse/MainForm.h")
    fix_cpp("Timelapse/MainForm.cpp")
    print("完成")
