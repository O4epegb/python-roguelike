from equipment_slots import EquipmentSlots

class Equippable:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0):
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus

    def to_json(self):

        return {
            'slot': self.slot.value,
            'power_bonus': self.power_bonus,
            'defense_bonus': self.defense_bonus,
            'max_hp_bonus': self.max_hp_bonus
        }

    @staticmethod
    def from_json(json_data):
        slot = EquipmentSlots(json_data.get('slot'))
        power_bonus = json_data.get('power_bonus')
        defense_bonus = json_data.get('defense_bonus')
        max_hp_bonus = json_data.get('max_hp_bonus')

        equippable = Equippable(slot, power_bonus, defense_bonus, max_hp_bonus)

        return equippable
