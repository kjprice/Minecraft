CMD_TEMPLATE = "fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {block}"
CMD_TEMPLATE_FULL_RELATIVE = "fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {block} {other}"
CMD_TEMPLATE_FULL_ABSOLUTE = "fill ~{x1} {y1} ~{z1} ~{x2} {y2} ~{z2} {block} {other}" # Y Values are absolute
X_OFFSET = 10
MAX_DISTANCE = 31
MAX_FILL = 32768

SEA_LEVEL = 63

# Max Vertical Height
MIN_Y = -60
MAX_Y = 256