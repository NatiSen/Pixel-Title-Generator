import random

letter_map = {
    'I': [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11111",
    ],
    'A': [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    'M': [
        "10001",
        "11011",
        "10101",
        "10101",
        "10001",
        "10001",
        "10001",
    ],
    'F': [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "10000",
    ],
    'U': [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    'L': [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    'S': [
        "01111",
        "10000",
        "10000",
        "01110",
        "00001",
        "00001",
        "11110",
    ],
    'T': [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
    'C': [
        "01110",
        "10001",
        "10000",
        "10000",
        "10000",
        "10001",
        "01110",
    ],
    'K': [
        "10001",
        "10010",
        "10100",
        "11000",
        "10100",
        "10010",
        "10001",
    ],
    'D': [
        "11110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11110",
    ],
    'E': [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111",
    ],
    'V': [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01010",
        "00100",
    ],
    ' ': [
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
        "00000",
    ],
}

WIDTH_PER_LETTER = 6  # 5 pixels + 1 spacing
HEIGHT = 7
TEXT = "I AM FULL STACK DEV"

NUM_LETTERS = len(TEXT)

SVG_WIDTH = 880
SVG_HEIGHT = 190

MARGIN = 40  # <- Margines od krawędzi

pixel_width = (SVG_WIDTH - 2 * MARGIN) / (NUM_LETTERS * WIDTH_PER_LETTER)
pixel_height = (SVG_HEIGHT - 2 * MARGIN) / HEIGHT

PIXEL_SIZE = min(pixel_width, pixel_height)

text_width = PIXEL_SIZE * WIDTH_PER_LETTER * NUM_LETTERS
text_height = PIXEL_SIZE * HEIGHT

offset_x = (SVG_WIDTH - text_width) / 2
offset_y = (SVG_HEIGHT - text_height) / 2


def create_svg(text):
    letters = [c if c in letter_map else ' ' for c in text]

    svg = []
    svg.append(f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">')

    # Definicje gradientów (3 różne)
    svg.append('''
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ecd2bb"/>
        <stop offset="100%" stop-color="#a0aeee"/>
      </linearGradient>
      <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#a0aeee"/>
        <stop offset="100%" stop-color="#120fc7"/>
      </linearGradient>
      <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#5771ec"/>
        <stop offset="100%" stop-color="#ecd2bb"/>
      </linearGradient>
    </defs>
    ''')

    # Tło
    svg.append(f'<rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="#0d1117" />')

    x_cursor = 0
    for char in letters:
        pattern = letter_map.get(char, letter_map[' '])
        for y, row in enumerate(pattern):
            for x, c in enumerate(row):
                if c == '1':
                    px = offset_x + (x_cursor + x) * PIXEL_SIZE
                    py = offset_y + y * PIXEL_SIZE
                    gradient_id = random.choice(["grad1", "grad2", "grad3"])
                    svg.append(f'<rect x="{px}" y="{py}" width="{PIXEL_SIZE}" height="{PIXEL_SIZE}" fill="url(#{gradient_id})" />')
        x_cursor += WIDTH_PER_LETTER

    # Obramowanie
    svg.append(f'''<rect 
    x="0" y="0" 
    width="{SVG_WIDTH}" height="{SVG_HEIGHT}" 
    fill="none" 
    stroke="#ecd2bb" 
    stroke-width="2" 
    stroke-dasharray="10,5"
    rx="20" ry="20"
/>''')


    svg.append('</svg>')

    return "\n".join(svg)

svg_code = create_svg(TEXT)

with open("pixel_text_centered.svg", "w") as f:
    f.write(svg_code)

print("✅ Gotowe! Plik pixel_text_centered.svg został wygenerowany.")
