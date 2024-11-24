def hex_to_rgb(hex_color):

    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
    return r, g, b


def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def average_colors(*colors):

    total_r, total_g, total_b = 0, 0, 0
    num_colors = len(colors)

    for color in colors:
        r, g, b = hex_to_rgb(color)
        total_r += r
        total_g += g
        total_b += b

    avg_r = total_r // num_colors
    avg_g = total_g // num_colors
    avg_b = total_b // num_colors

    return rgb_to_hex(avg_r, avg_g, avg_b)


colors = ['#ff5733', '#33ff57', '#3357ff']
average_color = average_colors(*colors)
print("Средний цвет:", average_color)