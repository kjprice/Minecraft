from ..conf import SEA_LEVEL
def tp_to_sealevel():
  return 'tp @p ~ {} ~'.format(SEA_LEVEL + 1)