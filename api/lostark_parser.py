import locale
import re

nl = ' '


def parse_get_skill_info(data: dict):
    return f"""
    {" | ".join(map(lambda skill_info: f"{skill_info['Name']} [{skill_info['Level']}] {skill_info['Tri']}", data["Skill"]["Skill"]))} 
"""


def parse_server(data: dict):
    return f"""{data["Basic"]["Server"]}"""


def parse_class(data: dict):
    return f"""{data["Basic"]["Class"]["Name"]}"""


def parse_guild(data: dict):
    return f"""{data["Basic"]["Guild"]}"""


def parse_title(data: dict):
    return f"""{data["Basic"]["Title"]}"""


def parse_name(data: dict):
    return f"""{data["Basic"]["Name"]}"""


def parse_character_level(data: dict):
    return f"""{data["Basic"]["Level"]["Battle"]}"""


def parse_item_level(data: dict):
    return f"""{data["Basic"]["Level"]["Item"]}"""


def parse_skill_point(data: dict):
    return f"""{data["Skill"]["SkillPoint"]["Used"]}/{data["Skill"]["SkillPoint"]["Total"]}"""


def parse_expedition_level(data: dict):
    return f"""{data["Basic"]["Level"]["Expedition"]}"""


def parse_wisdom_level(data: dict):
    return f"""{data["Basic"]["Wisdom"]["Level"]}"""


def parse_attack(data: dict):
    return f"""{data["Basic"]["Stat"]["Attack"]}"""


def parse_card(data: dict):
    return f"""{list(data["Card"])[-1]["Name"]}"""


def parse_health(data: dict):
    return f"""{data["Basic"]["Stat"]["Health"]}"""


def parse_critical(data: dict):
    return f"""{data["Basic"]["Stat"]["Critical"]}"""


def parse_specialty(data: dict):
    return f"""{data["Basic"]["Stat"]["Specialty"]}"""


def parse_agility(data: dict):
    return f"""{data["Basic"]["Stat"]["Agility"]}"""


def parse_proficiency(data: dict):
    return f"""{data["Basic"]["Stat"]["Proficiency"]}"""


def parse_endurance(data: dict):
    return f"""{data["Basic"]["Stat"]["Endurance"]}"""


def parse_engrave(data: dict):
    return f"""{nl.join(list(map(lambda d: d[0] + d[-1], data["Basic"]["Engrave"])))}"""


def parse_sub_character(data: dict):
    regex_level = "\.\d{2}"
    return f"""
{" | ".join(map(lambda sub_character: f"Lv. {re.sub(regex_level, '', sub_character['Level'].replace('Lv.', ''))} {sub_character['Name']}", data["CharacterList"]))} 
        """


def parse_ability_stone(data: dict):
    return f"""
{nl.join(map(lambda ability: f"[{ability['EngraveName']}] 활성도 {ability['Effect']}", data["Items"]["어빌리티 스톤"]["Engrave"]))}
        """


def parse_island_heart(data: dict):
    return f"""{data["Collections"][0]["섬의 마음"]}"""


def parse_start(data: dict):
    return f"""{data["Collections"][1]["오르페우스의 별"]}"""


def parse_giant_heart(data: dict):
    return f"""{data["Collections"][2]["거인의 심장"]}"""


def parse_art(data: dict):
    return f"""{data["Collections"][3]["위대한 미술품"]}"""


def parse_mokoko(data: dict):
    return f"""{data["Collections"][4]["모코코 씨앗"]}"""


def parse_a_sailing_adventure(data: dict):
    return f"""{data["Collections"][5]["항해 모험물"]}"""


def parse_Signs_of_Ignaea(data: dict):
    return f"""{data["Collections"][6]["이그네아의 징표"]}"""


def parse_the_leaves_of_the_world_water(data: dict):
    return f"""{data["Collections"][7]["세계수의 잎"]}"""


def parse_jewelry_to_string(jewl):
    return (jewl["JewlName"] + " " + jewl["SkillName"]).replace("염의 보석", "").replace("화의 보석", "").replace("레벨 ", "")


def parse_get_jewelry_info(data: dict):
    return " | ".join(list(map(parse_jewelry_to_string, data["Jewl"])))


def parse_get_equipment_info(data: dict):
    result = ""
    try:
        result += f"무기 : {data['Items']['무기']['Name']} ({data['Items']['무기']['Quality']}) | "
    except KeyError:
        result += "무기 : 없음 | "

    try:
        result += f"투구 : {data['Items']['머리 방어구']['Name']} ({data['Items']['머리 방어구']['Quality']}) | "
    except KeyError:
        result += "투구 : 없음 | "

    try:
        result += f"견갑 : {data['Items']['어깨 방어구']['Name']} ({data['Items']['어깨 방어구']['Quality']}) | "
    except KeyError:
        result += "견갑 : 없음 | "

    try:
        result += f"상의 : {data['Items']['상의']['Name']} ({data['Items']['상의']['Quality']}) | "
    except KeyError:
        result += "상의 : 없음 | "

    try:
        result += f"하의 : {data['Items']['하의']['Name']} ({data['Items']['하의']['Quality']}) | "
    except KeyError:
        result += "하의 : 없음 | "

    try:
        result += f"장갑 : {data['Items']['장갑']['Name']} ({data['Items']['장갑']['Quality']}) | "
    except KeyError:
        result += "장갑 : 없음 | "

    return result


def parse_get_week_gold_info(data: dict):
    locale.setlocale(locale.LC_ALL, '')

    gold_list = data["Gold"]["GoldList"]
    character = lambda \
            gold: f"{gold['Name']} {format(parse_week_gold_calculator(parse_level_str_to_int(gold['Level'])), ',d')} {gold['Level']} "

    total_gold = 0
    for gold in gold_list:
        total_gold += parse_week_gold_calculator(
            int(gold['Level'].replace('Lv.', '').replace(',', '').replace('.', '')) / 100)

    character_list = " | ".join(list(map(character, gold_list)))
    return f"""
{character_list} 

 | 
 | 총 획득골드 : {format(total_gold, ",d")}
"""


def parse_level_str_to_int(level_str):
    return int(int(level_str.replace('Lv.', '').replace(',', '').replace('.', '')) / 100)


def parse_week_gold_calculator(level):
    if level >= 1560:
        return 19500
    if level >= 1550:
        return 19000
    if level >= 1540:
        return 18500
    if level >= 1520:
        return 17500
    if level >= 1500:
        return 15000
    if level >= 1490:
        return 13500
    if level >= 1475:
        return 13500
    if level >= 1460:
        return 10700
    if level >= 1445:
        return 8700
    if level >= 1430:
        return 6700
    if level >= 1415:
        return 4200
    if level >= 1370:
        return 3000
    else:
        return 0


def parse_get_accessories_info(data: dict):
    result = ""

    try:
        result += f"반지 : {data['Items']['반지1']['Name']} {data['Items']['반지1']['Plus']} | "
    except KeyError:
        result += f"반지 : 없음 | "

    try:
        result += f"반지 : {data['Items']['반지2']['Name']} {data['Items']['반지2']['Plus']} | "
    except KeyError:
        result += f"반지 : 없음 | "

    try:
        result += f"목걸이 : {data['Items']['목걸이']['Name']} {data['Items']['목걸이']['Plus']} | "
    except KeyError:
        result += f"목걸이 : 없음 | "

    try:
        result += f"귀걸이 : {data['Items']['귀걸이1']['Name']} {data['Items']['귀걸이1']['Plus']} | "
    except KeyError:
        result += f"귀걸이 : 없음 | "

    try:
        result += f"귀걸이 : {data['Items']['귀걸이2']['Name']} {data['Items']['귀걸이2']['Plus']} | "
    except KeyError:
        result += f"귀걸이 : 없음 | "

    try:
        result += f"팔찌 : {data['Items']['팔찌']['Name']} | "
        result += f"{parse_bracelet_option_to_string(data)} | "
    except KeyError:
        ""

    return result


def parse_bracelet_option_to_string(data: dict):
    hyphen = lambda s: " - " + s
    return "".join(list(map(hyphen, data["Items"]["팔찌"]["Plus"])))
