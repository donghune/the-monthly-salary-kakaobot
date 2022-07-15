import requests

from api import lostark_parser


def get_basic(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return f"""
{lostark_parser.parse_title(data)} | {lostark_parser.parse_name(data)} 

직업 : {lostark_parser.parse_class(data)}
템/전/원 : {lostark_parser.parse_item_level(data)} / {lostark_parser.parse_character_level(data)} / {lostark_parser.parse_expedition_level(data)} 
서버/길드 : {lostark_parser.parse_server(data)} / {lostark_parser.parse_class(data)} 
전투 특성 : {lostark_parser.parse_engrave(data)} 
스킬포인트 : {lostark_parser.parse_skill_point(data)} 
각인 : {lostark_parser} 
공격력/체력 : {lostark_parser.parse_attack(data)} / {lostark_parser.parse_health(data)} 
카드 : {lostark_parser.parse_card(data)} 
섬마: {lostark_parser.parse_island_heart(data)} 미술품: {lostark_parser.parse_art(data)} 심장: {lostark_parser.parse_giant_heart(data)} 별: {lostark_parser.parse_start(data)} 
모코코: {lostark_parser.parse_mokoko(data)} 모험물: {lostark_parser.parse_a_sailing_adventure(data)} 징표: {lostark_parser.parse_Signs_of_Ignaea(data)} 잎: {lostark_parser.parse_the_leaves_of_the_world_water(data)} 
"""


def get_sub_character(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_sub_character(data)


def get_jewelry(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_jewelry_info(data)


def get_equipment(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_equipment_info(data)


def get_accessories(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_accessories_info(data)


def get_week_gold(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_week_gold_info(data)


def get_skill(username):
    res = requests.get('http://152.70.248.4:5000/userinfo/' + username)
    data = res.json()
    return lostark_parser.parse_get_skill_info(data)
