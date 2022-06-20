from .MinecraftAddons.MinecraftFunctions.create_all_functions import create_all
from .Projects.collage.family_collage import FamilyCollage
from .Projects.java_edition.java_edition_pack import JavaEditionPack
from .MinecraftStructures import minecraft_structure

# TODO(kjprice): Create multiple versions of the family collage where each have different namespaces...
# - IE "xs", "xl", etc
FamilyCollage()
JavaEditionPack()

create_all()