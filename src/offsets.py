from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B47B
    hp_current: int = 0x253
    hp_max: int = 0x257
    atk: int = 0x25B
    def_: int = 0x25F
    magic: int = 0x263
    gold: int = 0x27B
    inventory_ptr: int = 0x29B
    battle_flag: int = 0x2D3
    timer: int = 0x2EB
    items_base: int = 0x2A4B56B

CURRENT_OFFSETS = Offsets()
