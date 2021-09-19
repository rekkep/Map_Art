import math
from PIL import Image
from skimage import io, color

newpath = os.path.dirname(os.path.realpath(__file__)) + '\map_art_placement.data'
if not os.path.exists(newpath):
    os.makedirs(newpath)
file_block = os.path.dirname(os.path.realpath(__file__)) + '\map_art_placement.data/block_placement.json' #file for blocks
file_coordinates = os.path.dirname(os.path.realpath(__file__)) + '\map_art_placement.data/coordinates.json' #file for coordinates
file_picture = 'Map_Art.png' #file for picture
t = open(file_block, "w")
c = open(file_coordinates, "w")
pic_i = Image.open(file_picture)
i = pic_i.convert('RGB')
all_pixels = []

#RGB from minecraft blocks
brighter = [(127, 178, 56), (247, 233, 163), (199, 199, 199), (255, 0, 0), (160, 160, 255), (167, 167, 167), (0, 124, 0), (255, 255, 255), (164, 168, 184), (151, 109, 77), (112, 112, 112), (64, 64, 255), (143, 119, 72), (255, 252, 245), (216, 127, 51), (178, 76, 216), (102, 153, 216), (229, 229, 51), (127, 204, 25), (242, 127, 165), (76, 76, 76), (153, 153, 153), (76, 127, 153), (127, 63, 178), (51, 76, 178), (102, 76, 51), (102, 127, 51), (153, 51, 51), (25, 25, 25), (250, 238, 77), (92, 219, 213), (74, 128, 255), (0, 217, 58), (129, 86, 49), (112, 2, 0), (209, 177, 161), (159, 82, 36), (149, 87, 108), (112, 108, 138), (186, 133, 36), (103, 117, 53), (160, 77, 78), (57, 41, 35), (135, 107, 98), (87, 92, 92), (122, 73, 88), (76, 62, 92), (76, 50, 35), (76, 82, 42), (142, 60, 46), (37, 22, 169), (189, 48, 499), (148, 63, 97), (92, 25, 29), (22, 126, 134), (58, 142, 140), (86, 44, 62), (20, 180, 133), (100, 100, 100), (216, 175, 147), (127, 167, 150)]

#coresponding blocks
id_block = ["slime_block", "bone_block", "mushroom_stem", "redstone_block", "packed_ice", "iron_block", "azalea_leaves[persistent= true]", "white_wool", "clay", "coarse_dirt", "cobblestone", "cobblestone_stairs[facing=west,waterlogged=true]", "crafting_table", "sea_lantern", "pumpkin", "magenta_wool", "light_blue_wool", "yellow_wool", "melon", "pink_wool", "gray_wool", "light_gray_wool", "prismarine", "purple_wool", "blue_wool", "brown_wool", "moss_block", "red_wool", "coal_block", "gold_block", "prismarine_bricks", "lapis_block", "emerald_block", "spruce_planks", "netherrack", "white_terracotta", "orange_terracotta", "magenta_terracotta", "light_blue_terracotta", "yellow_terracotta", "lime_terracotta", "pink_terracotta", "gray_terracotta", "light_gray_terracotta", "cyan_terracotta", "purple_terracotta", "blue_terracotta", "brown_terracotta", "green_terracotta", "red_terracotta", "black_terracotta", "crimson_nylium", "crimson_planks", "crimson_hyphae", "warped_nylium", "warped_planks", "warped_hyphae", "warped_wart_block", "deepslate", "raw_iron_block", "glow_lichen[down=true]"]


#get diferent RGB values for diferent heights
default = []
darker = []

for blocks in range(len(brighter)):
    m21 = 180 / 255
    m23 = 220 / 255
    R, G, B = brighter[blocks]
    darker_blocks = math.floor(R * m21), math.floor(G * m21), math.floor(B * m21)
    darker.append(darker_blocks)
    default_blocks = math.floor(R * m23), math.floor(G * m23), math.floor(B * m23)
    default.append(default_blocks)

#convert RGB in L*a*b*
default_lab = color.rgb2lab(default)
darker_lab = color.rgb2lab(darker)
brighter_lab = color.rgb2lab(brighter)

pic_width = 128
pic_height = 128
percent = 0

#resizind Image
size = (pic_width, pic_height)
resized_image = i.resize(size)
pixels = resized_image.load()
width, height = resized_image.size

#get RGB info from image
def write_blocks(percent):
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    #RGB pixel in RGB map block
    for pixel in range(len(all_pixels)):
        #R, G, B = all_pixels[pixel]
        R, G, B = color.rgb2lab(all_pixels[pixel])
        distance(R, G, B)
        print(str('%.2f' % (percent * 100)) + "%")
        percent += 1/16384


def distance(P_R, P_G, P_B):
    #distance between point RGB and mapcolor RGB
    all_brighter_dist = []
    for blocks in range(len(brighter_lab)):
        #B_R, B_G, B_B = brighter[blocks]
        B_R, B_G, B_B = brighter_lab[blocks]
        brighter_dist = math.sqrt((P_R - B_R) ** 2 + (P_G - B_G) ** 2 + (P_B - B_B) ** 2)
        all_brighter_dist.append(brighter_dist)
        sort_brighter_dist = sorted(all_brighter_dist)
    #find lowest distance between point RGB and mapcolor RGB
        lowest_brighter_dist = sort_brighter_dist[0], 1

    all_default_dist = []
    for blocks in range(len(default)):
        #d_R, d_G, d_B = default[blocks]
        d_R, d_G, d_B = default_lab[blocks]
        default_dist = math.sqrt((P_R - d_R) ** 2 + (P_G - d_G) ** 2 + (P_B - d_B) ** 2)
        all_default_dist.append(default_dist)
        sort_default_dist = sorted(all_default_dist)
    #find lowest distance between point RGB and mapcolor RGB
        lowest_default_dist = sort_default_dist[0], 0

    all_darker_dist = []
    for blocks in range(len(darker)):
        #D_R, D_G, D_B = darker[blocks]
        D_R, D_G, D_B = darker_lab[blocks]
        darker_dist = math.sqrt((P_R - D_R) ** 2 + (P_G - D_G) ** 2 + (P_B - D_B) ** 2)
        all_darker_dist.append(darker_dist)
        sort_darker_dist = sorted(all_darker_dist)
    #find lowest distance between point RGB and mapcolor RGB
        lowest_darker_dist = sort_darker_dist[0], -1

    all_sorted = lowest_darker_dist, lowest_default_dist, lowest_brighter_dist
    sort_all_sorted = sorted(all_sorted)
    all_lowest_dist, y = sort_all_sorted[0]
    if y == 0:
        block_id = all_default_dist.index(all_lowest_dist)
    elif y == -1:
        block_id = all_darker_dist.index(all_lowest_dist)
    else:
        block_id = all_brighter_dist.index(all_lowest_dist)



    #write blocks and coordinates to json
    t.write('"' + str(id_block[block_id]) + '",\n') #json blocks
    c.write(str(y) + ',\n') #json y coordinates

t.write("[\n")
c.write("[\n")
write_blocks(percent)
t.write("]\n")
c.write("]\n")
t.close()
c.close()
