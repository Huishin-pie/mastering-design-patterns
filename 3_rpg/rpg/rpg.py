from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role
    from troop.troop import Troop


class RPG:

    def __init__(self, troops: List['Troop']):
        self.round: int = 1
        self.troops = troops

    def start(self) -> None:
        print("=== RPG 遊戲開始 ===")

        while not self._is_game_end():
            self._play_round()
            self.round += 1

        self._show_result()

    def _play_round(self) -> None:
        troop_index = 0
        for troop in self.troops:
            members: List['Role'] = troop.get_members()
            i = 0
            while i < len(members):
                member = members[i]

                if not member.is_alive():
                    i += 1
                    continue

                print(f"輪到 [{troop.id}]{member}。")
                member.before_select_action()

                if not member.is_alive():
                    i += 1
                    continue
                
                if member.actionable:
                    enemy = self.troops[1 - troop_index].get_members(is_alive=True)
                    ally = troop.get_ally(member)

                    is_action_available = False
                    while not is_action_available:        
                        action_skill = member.select_action()
                        is_action_available = action_skill.check_mp_enough(member)
                        if not is_action_available:
                            print("你缺乏 MP，不能進行此行動。")

                    target_selections = action_skill.get_target_selections(member, ally, enemy)
                    targets = member.select_targets(target_selections)

                    member.spend_mp(action_skill.get_mp_cost())
                    member.execute_action(action_skill, targets)

                member.state.reduce_state_round(member)

                if self._is_game_end():
                    return
                
                members = troop.get_members()
                i += 1

            troop_index += 1

    def _is_game_end(self) -> bool:
        if not self.troops[0].get_hero().is_alive():
            return True
        for troop in self.troops:
            if troop.is_annihilated():
                return True
        return False

    def _show_result(self) -> None:
        if self.troops[0].get_hero().is_alive():
            print("你獲勝了！")
        else:
            print("你失敗了！")