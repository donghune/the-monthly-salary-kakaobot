import locale
import re

nl = '|'


def parse_get_skill_info(data: dict):
    return f"""
    {nl.join(map(lambda skill_info: f"{skill_info['Name']} [{skill_info['Level']}] {skill_info['Tri']}", data["Skill"]["Skill"]))} 
"""


def parse_basic(data: dict):
    return f"""
`서버` \t:\t {data["Basic"]["Server"]}|
`클래스` \t:\t {data["Basic"]["Class"]["Name"]}|
`길드` \t:\t {data["Basic"]["Guild"]}|
`칭호` \t:\t {data["Basic"]["Title"]}|
        """


def parse_level(data: dict):
    return f"""
`캐릭터` \t:\t {data["Basic"]["Level"]["Battle"]}|
`아이템` \t:\t {data["Basic"]["Level"]["Item"]}|
`원정대` \t:\t {data["Basic"]["Level"]["Expedition"]}|
`영지` \t:\t {data["Basic"]["Wisdom"]["Level"]}|
        """


def parse_sub_character(data: dict):
    regex_level = "\.\d{2}"
    return f"""
{nl.join(map(lambda sub_character: f"Lv. {re.sub(regex_level, '', sub_character['Level'].replace('Lv.', ''))} {sub_character['Name']}", data["CharacterList"]))} 
        """


def parse_stat(data: dict):
    return f"""
`공격력` \t:\t {data["Basic"]["Stat"]["Attack"]}|
`최대 생명력` \t:\t {data["Basic"]["Stat"]["Health"]}|
`치명` \t:\t {data["Basic"]["Stat"]["Critical"]}|
`특화` \t:\t {data["Basic"]["Stat"]["Specialty"]}|
`신속` \t:\t {data["Basic"]["Stat"]["Agility"]}|
`제압` \t:\t {data["Basic"]["Stat"]["Proficiency"]}|
`인내` \t:\t {data["Basic"]["Stat"]["Endurance"]}|
        """


def parse_engrave(data: dict):
    return f"""
{nl.join(data["Basic"]["Engrave"])}
        """


def parse_ability_stone(data: dict):
    return f"""
{nl.join(map(lambda ability: f"[{ability['EngraveName']}] 활성도 {ability['Effect']}", data["Items"]["어빌리티 스톤"]["Engrave"]))}
        """


def parse_get_collections(data: dict):
    return f"""
    섬의 마음 : {data["Collections"][0]["섬의 마음"]} {parse_collection_complete(data["Collections"][0]["섬의 마음"])}| 
    오르페우스의 별 : {data["Collections"][1]["오르페우스의 별"]} {parse_collection_complete(data["Collections"][1]["오르페우스의 별"])}| 
    거인의 심장 : {data["Collections"][2]["거인의 심장"]} {parse_collection_complete(data["Collections"][2]["거인의 심장"])}| 
    위대한 미술품 : {data["Collections"][3]["위대한 미술품"]} {parse_collection_complete(data["Collections"][3]["위대한 미술품"])}| 
    모코코 씨앗 : {data["Collections"][4]["모코코 씨앗"]} {parse_collection_complete(data["Collections"][4]["모코코 씨앗"])}| 
    항해 모험물 : {data["Collections"][5]["항해 모험물"]} {parse_collection_complete(data["Collections"][5]["항해 모험물"])}| 
    이그네아의 징표 : {data["Collections"][6]["이그네아의 징표"]} {parse_collection_complete(data["Collections"][6]["이그네아의 징표"])}| 
    세계수의 잎 : {data["Collections"][7]["세계수의 잎"]} {parse_collection_complete(data["Collections"][7]["세계수의 잎"])}| 
"""


def parse_collection_complete(data: dict):
    if data.split(" / ")[0] == data.split(" / ")[1]:
        return "Complete!"
    else:
        return ""


def parse_jewelry_to_string(jewl):
    return (jewl["JewlName"] + " " + jewl["SkillName"]).replace("염의 보석", "").replace("화의 보석", "").replace("레벨 ", "")


def parse_get_jewelry_info(data: dict):
    return "|".join(list(map(parse_jewelry_to_string, data["Jewl"])))


def parse_get_equipment_info(data: dict):
    result = ""
    try:
        result += f"`무기` \t:\t {data['Items']['무기']['Name']} ({data['Items']['무기']['Quality']})|"
    except KeyError:
        result += "`무기` \t:\t 없음|"

    try:
        result += f"`투구` \t:\t {data['Items']['머리 방어구']['Name']} ({data['Items']['머리 방어구']['Quality']})|"
    except KeyError:
        result += "`투구` \t:\t 없음|"

    try:
        result += f"`견갑` \t:\t {data['Items']['어깨 방어구']['Name']} ({data['Items']['어깨 방어구']['Quality']})|"
    except KeyError:
        result += "`견갑` \t:\t 없음|"

    try:
        result += f"`상의` \t:\t {data['Items']['상의']['Name']} ({data['Items']['상의']['Quality']})|"
    except KeyError:
        result += "`상의` \t:\t 없음|"

    try:
        result += f"`하의` \t:\t {data['Items']['하의']['Name']} ({data['Items']['하의']['Quality']})|"
    except KeyError:
        result += "`하의` \t:\t 없음|"

    try:
        result += f"`장갑` \t:\t {data['Items']['장갑']['Name']} ({data['Items']['장갑']['Quality']})|"
    except KeyError:
        result += "`장갑` \t:\t 없음|"

    return result


def parse_get_week_gold_info(data: dict):
    locale.setlocale(locale.LC_ALL, '')

    gold_list = data["Gold"]["GoldList"]
    character = lambda \
            gold: f"{gold['Name']} `{format(parse_week_gold_calculator(parse_level_str_to_int(gold['Level'])), ',d')}`| + {gold['Class']} {gold['Level']}| "

    total_gold = 0
    for gold in gold_list:
        total_gold += parse_week_gold_calculator(
            int(gold['Level'].replace('Lv.', '').replace(',', '').replace('.', '')) / 100)

    character_list = "|".join(list(map(character, gold_list)))
    return f"""
{character_list} 

`총 획득골드` : {format(total_gold, ",d")}
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
        result += f"`반지` \t:\t {data['Items']['반지1']['Name']} {data['Items']['반지1']['Plus']}|"
    except KeyError:
        result += f"`반지` \t:\t 없음"

    try:
        result += f"`반지` \t:\t {data['Items']['반지2']['Name']} {data['Items']['반지2']['Plus']}|"
    except KeyError:
        result += f"`반지` \t:\t 없음"

    try:
        result += f"`목걸이` \t:\t {data['Items']['목걸이']['Name']} {data['Items']['목걸이']['Plus']}|"
    except KeyError:
        result += f"`목걸이` \t:\t 없음"

    try:
        result += f"`귀걸이` \t:\t {data['Items']['귀걸이1']['Name']} {data['Items']['귀걸이1']['Plus']}|"
    except KeyError:
        result += f"`귀걸이` \t:\t 없음"

    try:
        result += f"`귀걸이` \t:\t {data['Items']['귀걸이2']['Name']} {data['Items']['귀걸이2']['Plus']}|"
    except KeyError:
        result += f"`귀걸이` \t:\t 없음"

    try:
        result += f"`팔찌` \t:\t {data['Items']['팔찌']['Name']}"
        result += f"{parse_bracelet_option_to_string(data)}"
    except KeyError:
        ""

    return result


def parse_bracelet_option_to_string(data: dict):
    hyphen = lambda s: " - " + s
    return "|".join(list(map(hyphen, data["Items"]["팔찌"]["Plus"])))
