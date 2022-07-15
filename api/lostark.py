import requests

from api import lostark_parser


def get_character_info_all(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return {
        "basic": lostark_parser.parse_basic(data),
        "level": lostark_parser.parse_level(data),
        "sub_character": lostark_parser.parse_sub_character(data),
        "stat": lostark_parser.parse_stat(data),
        "engrave": lostark_parser.parse_engrave(data),
        "ability_stone": lostark_parser.parse_ability_stone(data),
        "jewelry": lostark_parser.parse_get_jewelry_info(data),
        "equipment": lostark_parser.parse_get_equipment_info(data),
        "week_gold": lostark_parser.parse_get_week_gold_info(data),
        "accessories": lostark_parser.parse_get_accessories_info(data),
        "skill": lostark_parser.parse_get_skill_info(data),
        "collections": lostark_parser.parse_get_collections(data),
    }


def get_character_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return {
        "basic": lostark_parser.parse_basic(data),
        "level": lostark_parser.parse_level(data),
        "sub_character": lostark_parser.parse_sub_character(data),
        "stat": lostark_parser.parse_stat(data),
        "engrave": lostark_parser.parse_engrave(data),
        "ability_stone": lostark_parser.parse_ability_stone(data)
    }


def get_jewelry_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_jewelry_info(data)


def get_equipment_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_equipment_info(data)


def get_week_gold_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_week_gold_info(data)


def get_accessories_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_accessories_info(data)


def get_skill_info(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_skill_info(data)


def get_collections(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_collections(data)
