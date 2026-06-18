#pragma once
// 地图名称汉化映射表（英文 -> 简体国服译名）
// 数据源为内嵌资源 MapsList(ID 104)，loadMaps() 加载时按此表替换显示名。
// 未命中的名称保留英文原样。岛屿层(island)与街道层(streetName)已填充；
// 地图层(mapName)分批补充。
using namespace System;
using namespace System::Collections::Generic;

ref class MapTranslations {
public:
	static Dictionary<String^, String^>^ islandMap;
	static Dictionary<String^, String^>^ streetMap;
	static Dictionary<String^, String^>^ mapMap;

	static void Init() {
		if (islandMap != nullptr) return; // 幂等：只初始化一次

		islandMap = gcnew Dictionary<String^, String^>();
		streetMap = gcnew Dictionary<String^, String^>();
		mapMap = gcnew Dictionary<String^, String^>();

		// ===== 岛屿 / 大区 (12) =====
		islandMap[L"maple"] = L"枫叶岛";
		islandMap[L"victoria"] = L"维多利亚岛";
		islandMap[L"ossyria"] = L"傲斯里亚大陆";
		islandMap[L"elin"] = L"神木地区";
		islandMap[L"jp"] = L"和风村";
		islandMap[L"singapore"] = L"新加坡";
		islandMap[L"MasteriaGL"] = L"玛斯特利亚";
		islandMap[L"Episode1GL"] = L"序章";
		islandMap[L"HalloweenGL"] = L"万圣节活动";
		islandMap[L"weddingGL"] = L"婚礼";
		islandMap[L"event"] = L"活动";
		islandMap[L"etc"] = L"其他";

		// ===== 街道 / 区域 (95) =====
		streetMap[L"Adobis's Mission I"] = L"阿多比斯的任务 I";
		streetMap[L"Alcadno Research Institute"] = L"阿卡德诺研究所";
		streetMap[L"Altaire Camp"] = L"阿尔泰营地";
		streetMap[L"Amoria"] = L"阿莫利亚";
		streetMap[L"Aqua Road"] = L"水下世界";
		streetMap[L"Aquarium"] = L"水族馆";
		streetMap[L"Aran's Past"] = L"阿兰的过去";
		streetMap[L"Ariant"] = L"阿里安特";
		streetMap[L"Ariant Castle"] = L"阿里安特城堡";
		streetMap[L"Ariant Coliseum"] = L"阿里安特竞技场";
		streetMap[L"Badlands"] = L"荒地";
		streetMap[L"Bigger Ben"] = L"大本钟";
		streetMap[L"Black Road"] = L"黑色之路";
		streetMap[L"Camp Conference Room"] = L"营地会议室";
		streetMap[L"Cave of Life"] = L"生命之洞";
		streetMap[L"Crimsonwood  Keep"] = L"红木要塞";
		streetMap[L"Crimsonwood Mountain"] = L"红木山";
		streetMap[L"Cruising"] = L"航行中";
		streetMap[L"Deep Place of Temple"] = L"神殿深处";
		streetMap[L"Dungeon"] = L"地牢";
		streetMap[L"During the Ride"] = L"乘船途中";
		streetMap[L"El Nath"] = L"埃尔纳斯";
		streetMap[L"Ellin Forest"] = L"神木森林";
		streetMap[L"Empress' Road"] = L"女皇之路";
		streetMap[L"Empress's Road"] = L"女皇之路";
		streetMap[L"Entrance to MV's Lair"] = L"通往MV巢穴的入口";
		streetMap[L"Fairytale Land"] = L"童话之地";
		streetMap[L"Florina Road"] = L"芙罗莉娜海滩";
		streetMap[L"Forest of Poison Haze"] = L"毒雾森林";
		streetMap[L"Happy Village"] = L"幸福村";
		streetMap[L"Haunted House"] = L"鬼屋";
		streetMap[L"Herb Town"] = L"草药村";
		streetMap[L"Hidden Chamber"] = L"隐藏密室";
		streetMap[L"Hidden Street"] = L"隐藏街道";
		streetMap[L"In Flight"] = L"飞行中";
		streetMap[L"Initiation"] = L"新手入门";
		streetMap[L"Kerning City Subway"] = L"奇宁市地铁";
		streetMap[L"Kerning City Town Street"] = L"奇宁市街道";
		streetMap[L"Kerning Square"] = L"奇宁广场";
		streetMap[L"Korean Folk Town"] = L"韩国民俗村";
		streetMap[L"Last Mission"] = L"最后的任务";
		streetMap[L"Leafre"] = L"利弗尔";
		streetMap[L"Line 3 Construction Site"] = L"三号线施工现场";
		streetMap[L"Ludibrium"] = L"天空之城";
		streetMap[L"Magatia"] = L"马加提亚";
		streetMap[L"Malaysia"] = L"马来西亚";
		streetMap[L"Maple 7th Day Market"] = L"枫之谷七日市场";
		streetMap[L"Maple Road"] = L"枫叶之路";
		streetMap[L"Masteria"] = L"玛斯特利亚";
		streetMap[L"Memory Keeper"] = L"记忆守护者";
		streetMap[L"MesoGears"] = L"齿轮城";
		streetMap[L"Mini Dungeon"] = L"迷你地牢";
		streetMap[L"Monster Carnival"] = L"怪物嘉年华";
		streetMap[L"Mu Lung"] = L"武陵";
		streetMap[L"Mu Lung Dojo"] = L"武陵道场";
		streetMap[L"Mushroom Castle"] = L"蘑菇城堡";
		streetMap[L"Neinheart's Job Introduction"] = L"奈因哈特的职业介绍";
		streetMap[L"Neo City"] = L"新都市";
		streetMap[L"New Leaf City Town Street"] = L"新叶城街道";
		streetMap[L"Omega Sector"] = L"欧米伽区域";
		streetMap[L"On a Voyage"] = L"航行中";
		streetMap[L"Opening"] = L"开场";
		streetMap[L"Orbis"] = L"奥尔比斯";
		streetMap[L"Orbis Park"] = L"奥尔比斯公园";
		streetMap[L"Party Quest"] = L"组队任务";
		streetMap[L"Penguin Port in Emergency"] = L"紧急状态的企鹅港";
		streetMap[L"Phantom Forest"] = L"幻影森林";
		streetMap[L"Premium Road"] = L"高级之路";
		streetMap[L"Rainbow Street"] = L"彩虹街道";
		streetMap[L"Shadow Zone"] = L"暗影区域";
		streetMap[L"Sharenian"] = L"沙伦尼安";
		streetMap[L"Sheep Ranch"] = L"绵羊牧场";
		streetMap[L"Singapore"] = L"新加坡";
		streetMap[L"Snow Island"] = L"雪之岛";
		streetMap[L"Space Gaga"] = L"太空嘎嘎";
		streetMap[L"Space Mine"] = L"太空矿场";
		streetMap[L"Sunset Road"] = L"日落之路";
		streetMap[L"Tera Forest"] = L"泰拉森林";
		streetMap[L"The 2nd Monster Carnival"] = L"第二届怪物嘉年华";
		streetMap[L"The Burning Road"] = L"燃烧之路";
		streetMap[L"The Burning Sands"] = L"燃烧沙漠";
		streetMap[L"The Lair of MV"] = L"MV的巢穴";
		streetMap[L"The Nautilus"] = L"鹦鹉螺号";
		streetMap[L"Time Lane"] = L"时间通道";
		streetMap[L"Town of Ariant"] = L"阿里安特镇";
		streetMap[L"Treasure Dungeon"] = L"宝藏地牢";
		streetMap[L"Unique Road"] = L"独特之路";
		streetMap[L"Victoria Island"] = L"维多利亚岛";
		streetMap[L"Victoria Road"] = L"维多利亚之路";
		streetMap[L"Warning Street"] = L"警告街道";
		streetMap[L"Witch Tower"] = L"女巫之塔";
		streetMap[L"Zenumist Research Institute"] = L"泽诺米斯特研究所";
		streetMap[L"Zipangu"] = L"和风村";

		// ===== 地图 (mapName) 分批补充 =====
		// 后续批次在此填充 mapMap[...] = ...
	}

	static String^ Island(String^ en) {
		Init();
		if (en == nullptr) return en;
		String^ cn;
		if (islandMap->TryGetValue(en->Trim(), cn)) return cn;
		return en;
	}

	static String^ Street(String^ en) {
		Init();
		if (en == nullptr) return en;
		String^ cn;
		if (streetMap->TryGetValue(en->Trim(), cn)) return cn;
		return en;
	}

	static String^ Map(String^ en) {
		Init();
		if (en == nullptr) return en;
		String^ cn;
		if (mapMap->TryGetValue(en->Trim(), cn)) return cn;
		return en;
	}
};
