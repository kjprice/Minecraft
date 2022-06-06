from ..minecraft_function.minecraft_function import MinecraftFunction

class EquipNetherite(MinecraftFunction):
    def __init__(self):
        super().__init__('powers/equip_netherite')
    def build(self):
        self.run('# Giving netherite to all players')
        self.run('replaceitem entity @a slot.weapon.mainhand 1 netherite_sword')
        self.run('replaceitem entity @a slot.weapon.offhand 1 shield')
        self.run('replaceitem entity @a slot.armor.chest 1 netherite_chestplate')
        self.run('replaceitem entity @a slot.armor.legs 1 netherite_leggings')
        self.run('replaceitem entity @a slot.armor.feet 1 netherite_boots')
        self.run('replaceitem entity @a slot.armor.head 1 netherite_helmet') 
        self.run('replaceitem entity @a slot.hotbar 1 netherite_sword')
        self.run('replaceitem entity @a slot.weapon.mainhand 1 netherite_sword')
        self.run('replaceitem entity @a slot.hotbar 2 netherite_pickaxe')
        self.run('replaceitem entity @a slot.hotbar 3 netherite_shovel')
        self.run('replaceitem entity @a slot.hotbar 4 netherite_axe')
        self.run('replaceitem entity @a slot.hotbar 5 netherite_hoe')


