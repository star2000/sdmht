import csv
from pathlib import Path

import yaml


def 读取数据(path: str, idk: str = '编号') -> list[dict[str, str]]:
    text = Path(path).read_text('utf-8')
    reader = csv.DictReader(text.splitlines(), delimiter=';')
    return sorted([row for row in reader if row[idk]], key=lambda x: x[idk])


def 保存数据(path: str, data: list[dict[str, str]], idk: str = '编号') -> None:
    data = sorted(data, key=lambda x: x[idk])
    writer = csv.DictWriter(
        Path(path).open('w', encoding='utf-8'),
        data[0].keys(),
        delimiter=';',
        lineterminator='\n',
    )
    writer.writeheader()
    writer.writerows(data)


技能何时触发 = {
    '0': '发动时',
    '1': '移动时',
    '2': '护盾值增加时',
    '3': '攻击时',
    '6': '己方回合开始时',
    '8': '任意附属神离场时',
    '11': '攻击命中时',
    '15': '游戏开始时',
    '19': '己方抽卡时',
    '20': '被攻击时',
    '21': '离场时',
    '22': '生命值减少时',
    '24': '装填弹幕时',
    '25': '己方任意单位被命中的同时暴露时',
    '26': '生命值增加时',
    '27': '己方每获得一张卡时',
    '28': '己方迷雾被解除时',
    '29': '己方使用神迹卡时',
    '30': '主神生命值低于触发辅助时',
    '31': '敌方回合开始时',
    '32': '效果值中合体素材单位同时在场时',
    '35': '己方回合开始且不处于迷雾时',
    '36': '己方回合开始且自身伙伴卡ID的单位在场时',
    '37': '任意单位离场时',
    '38': '攻击解除敌方单位迷雾时',
    '40': '攻击前',
    '50': '敌方使用神迹卡时',
    '51': '己方回合开始且周围8格存在单位时',
    '52': '敌方使用弹幕卡时',
    '61': '己方手牌数量变化时',
    '64': '编号为选择范围的召唤物登场时',
    '65': '任意附属神完全离场时',
    '67': '任意单位获得雷印时',
    '68': '敌方每获得一张卡时',
    '69': '装填编号为选择范围的弹幕卡时',
    '70': '任意单位完全离场时',
    '73': '护盾值变化时',
    '74': '己方回合开始且自身护盾为0时',
    '75': '己方回合开始且己方场上存在触发辅助个编号为选择范围的单位时',
    '76': '被攻击离场时',
    '77': '完全离场时',
    '78': '敌方附属神离场时',
}
技能对敌我方 = {
    '-1': '',
    '0': '敌方',
    '1': '己方',
    '2': '全场',
}
技能选择规则 = {
    '0': '所有',
    '1': '选择',
    '2': '随机',
    '3': '镜像',
}
技能目标类型 = {
    '0': '',
    '1': '无单位的位置',
    '2': '不处于迷雾的单位',
    '3': '处于迷雾的单位',
    '4': '单位',
    '5': '玩家',
    '6': '自身',
    '7': '单位',
    '8': '位置',
    '9': '另一附属神',
    '10': '主神',
    '11': '攻击自身的单位',
    '20': '攻击命中的单位',
    '21': '有迷雾的位置',
    '22': '无迷雾的位置',
    '25': '无单位的位置',
    '26': '手牌',
    '31': '牌堆中的弹幕卡',
    '32': '自身左上到右下位置内的单位',
    '33': '秘术卡',
    '34': '召唤物',
    '35': '附属神',
    '36': '附属神',
    '37': '编号为选择范围的单位',
    '38': '父技能的目标',
    '39': '阵营编号为选择范围的单位',
    '40': '手牌中的神迹卡',
    '41': '封足的单位',
    '42': '手牌中的弹幕卡',
}

技能效果类型 = {
    '-1': '',
    '1': '生命值+效果值',
    '2': '生命上限+效果值',
    '3': '基础攻击力+效果值',
    '4': '基础移动力+效果值',
    '5': '护盾值+效果值',
    '6': '召唤编号为效果值的单位',
    '7': '覆盖范围类型为选择范围的迷雾，0单2圆5十6横7竖17全',
    '8': '解除范围类型为选择范围的迷雾，0单2圆5十6横7竖17全',
    '9': '解除迷雾',
    '12': '抽效果值张卡',
    '13': '弹幕卡吟唱时间+效果值',
    '14': '清除',
    '19': '坚壁',
    '20': '攻击力=效果值%的生命值（向下取整）',
    '21': '获得效果值编号列表里的每张卡',
    '22': '生命值+效果值（无视护盾与圣盾）',
    '23': '舍弃所有手牌',
    '25': '挂buff',
    '27': '随机移动至迷雾区域（无迷雾时原地不动）',
    '28': '迷雾反转',
    '29': '获得编号为效果值的技能',
    '30': '祈愿倒计时+效果值',
    '31': '祈愿倒计时上限+效果值',
    '33': '解除随机2格迷雾（优先无单位）',
    '34': '解除十字区域迷雾',
    '35': '替换此技能为完全离场的附属神技能',
    '37': '获得效果值编号列表的随机一张神迹卡',
    '39': '行动点消耗+效果值',
    '59': '替换为编号为效果值的弹幕卡',
    '60': '消耗素材单位，合体为最后一个编号的单位',
    '72': '反击',
    '73': '弃效果值张牌',
    '74': '随机获得效果值编号列表里的buff',
    '75': '攻击消耗选择范围点行动点',
    '77': '行动点+效果值',
    '78': '在随机格迷雾内以效果值点生命值复活（不超过生命上限）',
    '79': '获得一张品质为效果值的神迹卡，1传说2稀有3普通',
    '80': '变化为效果值编号的神',
    '82': '获得一张品质为效果值的弹幕卡，1传说2稀有3普通',
    '83': '使用的神迹卡行动点消耗+效果值',
    '84': '攻击力等于手牌数',
    '88': '弹幕卡攻击力+效果值',
    '92': '无效化对手的神迹卡',
    '93': '复制对方使用的神迹卡，复制的卡消耗为0',
    '96': '场地上每拥有一个单位，恢复1点行动点',
    '97': '获得效果值编号列表里的随机一张弹幕卡',
    '98': '生命值+效果值%的攻击力（向下取整）',
    '99': '所有手牌行动点消耗+效果值',
    '101': '获得本局内使用过的所有秘术，行动点消耗变为0',
    '102': '获得一张随机秘术卡',
    '103': '净化',
    '104': '按效果值列表中的概率随机获得一张对应概率的编号的卡',
    '105': '生命值+攻击命中数量乘以效果值',
    '107': '本局内的编号为选择范围的卡永久+1攻击力(无视获得状态)',
    '108': '按效果值里的概率随机触发一个对应编号的技能',
    '109': '生命值无法降低到1点以下',
    '110': '自身受到的伤害降低效果值点',
    '111': '目标失去等同于自身攻击力的生命值',
    '113': '按顺序获得效果值列表里的技能，全部获得完毕后无法继续获得',
    '114': '攻击力=效果值%的护盾值（向下取整）',
    '115': '护盾上限+效果值',
    '116': '生命值+效果值乘以敌方单位的数量',
    '117': '基础攻击力+效果值%的编号为选择范围的单位的攻击力（向下取整）',
    '118': '按顺序施放效果值列表里的技能，全部施放完毕后则无法施放',
    '119': '重置疯乱',
    '120': '编号为选择范围的卡行动点消耗+效果值',
    '122': '生命值+效果值%的编号为选择范围的单位的攻击力（向下取整）',
    '124': '完全离场',
    '125': '攻击不可解除迷雾',
    '126': '抽效果值张弹幕卡',
    '127': '基础攻击力+按效果值列表中的概率随机判定一个值',
    '128': '攻击自身的单位完全离场',
    '129': '获得本局使用弹幕卡数量的效果值编号的卡',
    '130': '生命值+效果值%的自身护盾值（向下取整）',
    '131': '基础攻击力+效果值%的选择范围编号的单位的攻击力（向下取整）',
    '132': '随机召唤效果值列表里的一个单位',
    '133': '获得消耗在效果值列表里的随机一张弹幕卡',
}

技能增益类型 = {
    '1': '迷雾不可被解除，持续1回合',
    '2': '迷雾不可被解除',
    '3': '圣盾',
    '4': '攻击力+2，持续1回合',
    '5': '攻击力-10，持续1回合',
    '6': '移动力+3，持续1回合',
    '7': '移动力+2，持续1回合',
    '8': '封刃，持续1回合',
    '9': '封足，持续1回合',
    '10': '生命值-2',
    '11': '生命值+10，持续2回合',
    '13': '攻击力+2，持续2回合',
    '15': '封足，持续2回合',
    '17': '攻击力+1，持续1回合',
    '18': '攻击力+2，持续1回合',
    '19': '移动力=0',
    '22': '攻击力+3，持续1回合',
    '24': '移动力+1，持续1回合',
    '28': '封刃，持续1回合',
    '31': '封足，持续1回合',
    '32': '封刃，持续1回合',
    '34': '迷雾不可被解除，持续1回合',
    '35': '封足，持续1回合',
    '36': '生命值+5，持续3回合',
    '37': '攻击力+1',
    '38': '攻击力+3，持续1回合',
    '39': '攻击力+4，持续1回合',
    '40': '攻击力+2，持续1回合',
    '41': '雷印',
    '43': '攻击力-2，持续1回合',
    '44': '攻击力-6，持续1回合',
    '45': '攻击力+1，持续1回合',
    '46': '攻击力-5，持续1回合',
    '47': '攻击力-3，持续2回合',
    '48': '攻击力-5，持续2回合',
    '50': '攻击力=3，持续1回合',
    '51': '无敌',
    '53': '生命值+8，持续3回合',
    '54': '攻击力+5，持续1回合',
    '55': '攻击力+1，持续2回合',
    '56': '攻击力+2，持续2回合',
    '57': '攻击力+2，持续2回合',
    '58': '攻击力+2，持续2回合',
    '59': '攻击力+2，持续2回合',
    '60': '攻击力+3，持续2回合',
    '61': '攻击力+3，持续2回合',
    '62': '攻击力+3，持续2回合',
    '63': '攻击力+10，持续1回合',
    '64': '攻击力-10，持续1回合',
    '65': '生命值+2，持续3回合',
    '67': '攻击力+6，持续1回合',
    '68': '生命值+10，持续2回合',
    '69': '攻击力+2，持续1回合',
    '70': '迷雾不可被解除，持续1回合',
    '71': '封足，持续2回合，不可被净化',
    '72': '封足，持续2回合',
    '75': '攻击力-2，持续1回合',
    '76': '生命值-3，持续3回合',
    '78': '封刃，持续1回合',
    '79': '攻击力-10，持续1回合，不可被净化',
    '80': '诅咒，持续1回合',
    '81': '攻击力-3，持续1回合',
    '82': '封刃，持续1回合，不可被净化',
    '83': '攻击力+3，持续1回合',
    '84': '攻击力-2，持续2回合',
    '85': '攻击力-2，持续1回合',
    '86': '攻击力+4，持续1回合',
}

技能编号描述字典: dict[str, set[str]] = {}
主神数据 = 读取数据('src/assets/data/ron_cfg_card_main.csv')
for 主神 in 主神数据:
    for i in ['技能1', '技能2', '技能3']:
        技能编号描述字典.setdefault(主神[i], set()).add(f"主神 {主神['编号']} : {主神['描述']}")

附属神数据 = 读取数据('src/assets/data/ron_cfg_card_sub.csv')
for 附属神 in 附属神数据:
    技能编号描述字典.setdefault(附属神['技能'], set()).add(f"附属神 {附属神['编号']} : {附属神['描述']}")

弹幕卡数据 = 读取数据('src/assets/data/ron_cfg_card_bullet.csv')
for 弹幕卡 in 弹幕卡数据:
    技能编号描述字典.setdefault(弹幕卡['技能'], set()).add(f"弹幕卡 {弹幕卡['编号']} : {弹幕卡['描述']}")

神迹卡数据 = 读取数据('src/assets/data/ron_cfg_card_effect.csv')
for 神迹卡 in 神迹卡数据:
    技能编号描述字典.setdefault(神迹卡['技能'], set()).add(f"神迹卡 {神迹卡['编号']} : {神迹卡['描述']}")


技能数据路径 = 'src/assets/data/ron_cfg_skill.csv'
技能编号名 = '技能ID'
技能数据 = 读取数据(技能数据路径, 技能编号名)

for 技能 in 技能数据:
    技能编号描述字典.setdefault(技能[技能编号名], set()).add(f"技能 {技能[技能编号名]} : {技能['技能描述']}")

l1 = 0
l2 = sum(len(_) for _ in 技能编号描述字典.values())
while l1 != l2:
    l1 = sum(len(_) for _ in 技能编号描述字典.values())
    for 技能 in 技能数据:
        if 技能[技能编号名] in 技能编号描述字典:
            for 子技能 in 技能['附带技能'].split(','):
                技能编号描述字典.setdefault(
                    子技能, 技能编号描述字典[技能[技能编号名]]).add(f"父技能: {技能[技能编号名]}:")
                if 技能[技能编号名] == 子技能:
                    raise Exception(f"技能 {技能[技能编号名]} 的子技能是自身")
        if 技能['效果类型'] in ['29', '108', '113', '118']:
            for 子技能 in 技能['效果值'].split(','):
                技能编号描述字典.setdefault(
                    子技能, 技能编号描述字典[技能[技能编号名]]).add(f"父技能: {技能[技能编号名]}:")
                if 技能[技能编号名] == 子技能:
                    raise Exception(f"技能 {技能[技能编号名]} 的子技能是自身")
        if 技能['效果类型'] in ['80']:
            子技能 = next((_['技能1'] for _ in 主神数据 if _['编号'] == 技能['效果值']), None)
            if not 子技能:
                子技能 = next(_['技能'] for _ in 附属神数据 if _['编号'] == 技能['效果值'])
            技能编号描述字典.setdefault(
                子技能, 技能编号描述字典[技能[技能编号名]]).add(f"父技能: {技能[技能编号名]}:")
            if 技能[技能编号名] == 子技能:
                raise Exception(f"技能 {技能[技能编号名]} 的子技能是自身")

    l2 = sum(len(_) for _ in 技能编号描述字典.values())

for k in list(技能编号描述字典.keys()):
    if k == '' or int(k) <= 10000:
        del 技能编号描述字典[k]

for k in 技能编号描述字典.keys():
    print(k)
    技能 = next(_ for _ in 技能数据 if _['技能ID'] == k)
    print(技能)
    何时触发描述 = 技能何时触发[技能['何时触发']]
    对敌我方描述 = 技能对敌我方[技能['对敌我方']]
    选择规则描述 = 技能选择规则[技能['选择规则']]
    目标类型描述 = 技能目标类型[技能['目标类型']]
    效果类型描述 = 技能效果类型[技能['效果类型']]
    描述 = f"猜测: {何时触发描述},{对敌我方描述},{选择规则描述},{目标类型描述},{效果类型描述}".replace(
        '效果值', 技能['效果值']).replace('选择范围', 技能['选择范围']).replace('触发辅助', 技能['触发辅助']).replace('+-', '-')
    if 技能['效果类型'] == '25':
        增益类型描述 = 技能增益类型[技能['效果值']]
        描述 += f",{增益类型描述}"
    if 技能['回合最大使用次数'] not in ['-1', 技能['单场最大使用次数']]:
        描述 += f",每回合至多可用{技能['回合最大使用次数']}次"
    if 技能['单场最大使用次数'] != '-1':
        描述 += f",单局游戏至多可用{技能['单场最大使用次数']}次"
    技能编号描述字典[k].add(描述)


yaml.dump({int(k): sorted(list(v)) for k, v in 技能编号描述字典.items()}, open('mixins/check-skill.yaml',
          'w', encoding='utf-8'), allow_unicode=True)
