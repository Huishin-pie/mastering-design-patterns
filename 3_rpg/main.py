from contextlib import contextmanager
from functools import lru_cache
import traceback
from typing import List, Optional, Tuple

from role.ai import AI
from role.ai_strategy.strategy_seed import StrategySeed
from role.hero import Hero
from role.role import Role
from rpg.rpg import RPG
from skill.one_punch_action.one_punch_cheerup import OnePunchCheerup
from skill.one_punch_action.one_punch_normal import OnePunchNormal
from skill.one_punch_action.one_punch_petrochemical import OnePunchPetrochemical
from skill.one_punch_action.one_punch_poisoned import OnePunchPoisoned
from skill.skill_fireball import SkillFireball
from skill.skill_one_punch import SkillOnePunch
from skill.skill_waterball import SkillWaterball
from skill.skill_self_healing import SkillSelfHealing
from skill.skill_self_explosion import SkillSelfExplosion
from skill.skill_cheerup import SkillCheerUp
from skill.skill_curse import SkillCurse
from skill.skill_petrochemical import SkillPetrochemical
from skill.skill_poison import SkillPoison
from skill.skill_summon import SkillSummon
from state.state_normal import StateNormal
from troop.troop import Troop
import sys
import builtins
import os


@lru_cache(maxsize=None)
def _skill_from_name(name: str):
    factories = {
        '火球': lambda: SkillFireball(),
        '水球': lambda: SkillWaterball(),
        '自我治療': lambda: SkillSelfHealing(),
        '自爆': lambda: SkillSelfExplosion(),
        '鼓舞': lambda: SkillCheerUp(),
        '詛咒': lambda: SkillCurse(),
        '石化': lambda: SkillPetrochemical(),
        '下毒': lambda: SkillPoison(),
        '召喚': lambda: SkillSummon(StrategySeed()),
        '一拳攻擊': lambda: SkillOnePunch(
            OnePunchNormal(
                OnePunchCheerup(
                    OnePunchPetrochemical(
                        OnePunchPoisoned()
                    )
                )
            )
        ),
    }
    factory = factories.get(name)
    if not factory:
        raise ValueError(f"未知技能名稱: {name}")
    return factory()

def parse_test_input(text: str):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return None

    t1, t2, choices = [], [], []
    section = None
    target_map = {'t1': t1, 't2': t2}

    def _parse_member(parts: list[str], troop_label: str):
        if len(parts) < 4:
            raise ValueError(f"{troop_label}成員資料不足: {' '.join(parts)}")
        name = parts[0]
        hp, mp, st = map(int, parts[1:4])
        skill_objs = [_skill_from_name(x) for x in parts[4:]] if len(parts) > 4 else []
        return (name, hp, mp, st, skill_objs)

    for ln in lines:
        if ln.startswith('#軍隊-1-開始'):
            section = 't1'
            continue
        if ln.startswith('#軍隊-1-結束'):
            section = None
            continue
        if ln.startswith('#軍隊-2-開始'):
            section = 't2'
            continue
        if ln.startswith('#軍隊-2-結束'):
            section = 'choices'
            continue

        if section in ('t1', 't2'):
            parts = ln.split()
            target_map[section].append(_parse_member(parts, '軍隊一' if section == 't1' else '軍隊二'))
        else:
            choices.append(ln)

    return (t1, t2, choices)


def make_input_feeder(choices: list[str]):
    original_input = builtins.input

    data = list(choices)

    def feeder(prompt: str = '') -> str:
        if data and (prompt.startswith("選擇行動：") or prompt.startswith("選擇 ")):
            val = data.pop(0)
            print(f"{prompt}{val}")
            return val
        return original_input(prompt)

    return feeder, original_input

@contextmanager
def patched_input(choices: List[str]):
    feeder, original = make_input_feeder(choices)
    builtins.input = feeder
    try:
        yield
    finally:
        builtins.input = original

def load_text(path: Optional[str]) -> str:
    if not path:
        raise FileNotFoundError("請在命令列提供測試資料路徑，例如: python main.py .\\test_case\\case.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"未找到測試資料檔案: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def build_members(items: List[Tuple[str, int, int, int, List[object]]], allow_hero: bool) -> List['Role']:
    members: List['Role'] = []
    for name, hp, mp, st, skill_objs in items:
        if allow_hero and name in ("Hero", "英雄"):
            members.append(Hero(hp, mp, st, StateNormal(), skill_objs))
        else:
            members.append(AI(hp, mp, st, name, StateNormal(), skill_objs, StrategySeed()))
    return members

def build_troop(troop_id: int, items: List[Tuple[str, int, int, int, List[object]]], allow_hero: bool) -> 'Troop':
    members = build_members(items, allow_hero)
    troop = Troop(troop_id, members)
    for m in members:
        m.troop = troop
    return troop

def main(argv: Optional[List[str]] = None):
    try:
        args = sys.argv if argv is None else argv
        path = args[1] if len(args) > 1 else None

        text = load_text(path)
        parsed = parse_test_input(text)
        if parsed is None:
            raise ValueError("測試資料格式錯誤")

        t1, t2, choices = parsed
        troop_1 = build_troop(1, t1, allow_hero=True)
        troop_2 = build_troop(2, t2, allow_hero=False)

        with patched_input(choices):
            rpg_game = RPG([troop_1, troop_2])
            rpg_game.start()

    except Exception:
        traceback.print_exc()
if __name__ == "__main__":
    main()
