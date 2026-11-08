from math import ceil, floor

box_paint_count = int(input())
rolls_wallpaper_count = int(input())
gloves_pair_price = float(input())
brush_price = float(input())

BOX_PAINT_PRICE = 21.50
ROLL_WALLPAPER_PRICE = 5.20
GLOVES_PAIR_NEEDED = ceil(rolls_wallpaper_count * 0.35)
BRUSHES_NEEDED = floor(box_paint_count * 0.48)

total_cost = (BOX_PAINT_PRICE * box_paint_count) + (gloves_pair_price * GLOVES_PAIR_NEEDED) + (rolls_wallpaper_count * ROLL_WALLPAPER_PRICE) + (brush_price * BRUSHES_NEEDED)
delivery = total_cost / 15

print(f"This delivery will cost {delivery:.2f} lv.")