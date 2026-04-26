from __future__ import annotations

from io import BytesIO
from pathlib import Path
from textwrap import shorten

from PIL import Image, ImageOps
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "menu" / "Sagarmatha_Momo_Picture_Menu.pdf"
OUTPUT_VERTICAL = ROOT / "assets" / "menu" / "Sagarmatha_Momo_Picture_Menu_Vertical_A4.pdf"
LOGO = ROOT / "assets" / "products" / "compressed" / "sagarmathaMomoLogo-compressed.webp"

PAGE_SIZE = A4
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE

BG = HexColor("#fff7ec")
CARD_BG = white
ACCENT = HexColor("#c85f1d")
ACCENT_DARK = HexColor("#7d3512")
TEXT = HexColor("#2e241d")
MUTED = HexColor("#6f5a49")
LINE = HexColor("#ead8c1")


MENU = [
    {
        "category": "Snacks",
        "items": [
            {
                "name": "Samosas",
                "image": "assets/products/Samosas.jpeg",
                "description": "Crisp pastries filled with seasoned potatoes, peas, and warm spices.",
            },
            {
                "name": "Chicken 65",
                "image": "assets/products/Chicken65.jpeg",
                "description": "Crispy chicken with chili, herbs, and bold appetizer flavor.",
            },
            {
                "name": "Gobi Manchurian",
                "image": "assets/products/GobiManchurian.jpeg",
                "description": "Crispy cauliflower in a savory-spicy house sauce.",
            },
            {
                "name": "Chicken Chilly",
                "image": "assets/products/ChickenChilly.jpeg",
                "description": "Boneless chicken cooked with onion, bell pepper, jalapeno, and chili sauce.",
            },
            {
                "name": "Paneer Chilly",
                "image": "assets/products/PaneerChilly.jpeg",
                "description": "Paneer cubes tossed with peppers, jalapeno, and savory-spicy sauce.",
            },
        ],
    },
    {
        "category": "Momos",
        "items": [
            {
                "name": "Sadheko Momo",
                "image": "assets/products/SadhekoMomo.jpeg",
                "description": "Steamed momo tossed with herbs, ginger, green onion, and house tomato sauce.",
            },
            {
                "name": "Steamed Momo",
                "image": "assets/products/Steamed_Momo.jpeg",
                "description": "Classic steamed momo served hot with the house dipping sauce.",
            },
            {
                "name": "Fried Momo",
                "image": "assets/products/Fried_Momo.jpg",
                "description": "Golden fried momo with a crisp outside and savory filling.",
            },
            {
                "name": "Bhaktapur Jhol Momo",
                "image": "assets/products/Bhaktaput_Jhol_Momo.jpg",
                "description": "Steamed momo in a chilled, tangy soybean and spice jhol.",
            },
            {
                "name": "Crispy Saucy Momo",
                "image": "assets/products/Crispy_Saucy_Momo.jpg",
                "description": "Crispy fried momo glazed with house tomato-based sweet and flavorful sauce in mild, medium, or spicy heat.",
            },
            {
                "name": "Tato Jhol Momo",
                "image": "assets/products/TatoJholMomo.jpeg",
                "description": "Steamed momo served in a warm tomato-based soup.",
            },
            {
                "name": "Chilly Momo",
                "image": "assets/products/ChillyMomo.jpeg",
                "description": "Fried momo sauteed with onion, peppers, and chili sauce.",
            },
        ],
    },
    {
        "category": "Curries",
        "items": [
            {
                "name": "Chicken Curry",
                "image": "assets/products/ChickenCurry.jpeg",
                "description": "Bone-in chicken curry with onion, tomato, garlic, ginger, and house spices.",
            },
            {
                "name": "Boneless Chicken Curry",
                "image": "assets/products/ChickenCurry.jpeg",
                "description": "Boneless chicken in a savory onion-tomato curry with balanced heat.",
            },
            {
                "name": "Chicken Shahi Korma",
                "image": "assets/products/ChickenShahiKorma.jpeg",
                "description": "Mild creamy chicken curry with cashew notes and delicate spices.",
            },
            {
                "name": "Aloo Bodi Tama",
                "image": "assets/products/AlooBodiTama.jpeg",
                "description": "Traditional Nepali curry with potatoes, black-eyed peas, and bamboo shoot.",
            },
            {
                "name": "Aloo Cauli",
                "image": "assets/products/AlooCauli.jpeg",
                "description": "Homestyle curry of potatoes and cauliflower cooked until tender.",
            },
        ],
    },
    {
        "category": "Rice and Noodles",
        "items": [
            {
                "name": "Chicken Biryani",
                "image": "assets/products/Biryani.jpg",
                "description": "Fragrant basmati rice layered with seasoned chicken, herbs, and spices.",
            },
            {
                "name": "Fried Rice",
                "image": "assets/products/FriedRice.jpeg",
                "description": "Stir-fried rice with vegetables, spring onion, and savory seasoning.",
            },
            {
                "name": "Chowmein",
                "image": "assets/products/Chowmein.jpeg",
                "description": "Street-style noodles tossed with vegetables and house seasoning.",
            },
        ],
    },
    {
        "category": "Desserts",
        "items": [
            {
                "name": "Kheer",
                "image": "assets/products/Kheer.jpeg",
                "description": "Traditional rice pudding with a creamy and lightly sweet finish.",
            },
            {
                "name": "Lal Mohan",
                "image": "assets/products/LalMohan.jpeg",
                "description": "Soft milk-based sweet soaked in syrup for a richer dessert.",
            },
            {
                "name": "Rasmalai",
                "image": "assets/products/Rasmalai.jpeg",
                "description": "Soft cheese patties served in sweetened milk.",
            },
        ],
    },
    {
        "category": "Sides",
        "items": [
            {
                "name": "Special Paratha",
                "image": "assets/products/SpecialParatha.jpeg",
                "description": "Flaky layered flatbread that pairs especially well with curries.",
            },
            {
                "name": "Fries",
                "image": "assets/products/Fries.jpeg",
                "description": "Golden fried potato strips for an easy shareable side.",
            },
            {
                "name": "Basmati Rice",
                "image": "assets/products/BasmatiRice.jpeg",
                "description": "Steamed basmati rice for curries and sauced dishes.",
            },
            {
                "name": "Radish Pickle",
                "image": "assets/products/RadishPickel.jpeg",
                "description": "Sharp and tangy pickle that brightens savory plates.",
            },
            {
                "name": "Raita",
                "image": "assets/products/Raita.jpeg",
                "description": "Cooling yogurt side that balances spicier dishes.",
            },
        ],
    },
    {
        "category": "Drinks",
        "items": [
            {
                "name": "Mango Lassi",
                "image": "assets/products/MangoLassi.jpeg",
                "description": "Smooth yogurt drink blended with mango for a sweet finish.",
            },
            {
                "name": "Soda",
                "image": "assets/products/compressed/Soda-compressed.webp",
                "description": "Classic bottled soda choices to pair with savory dishes.",
            },
            {
                "name": "Bottled Water",
                "image": "assets/products/compressed/water-compressed.webp",
                "description": "Simple bottled refreshment.",
            },
        ],
    },
]


def wrap_text(text: str, font_name: str, font_size: int, max_width: float, max_lines: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""

    for word in words:
        trial = word if not current else f"{current} {word}"
        if stringWidth(trial, font_name, font_size) <= max_width:
            current = trial
            continue

        if current:
            lines.append(current)
            current = word
        else:
            lines.append(word)
            current = ""

        if len(lines) == max_lines:
            break

    if len(lines) < max_lines and current:
        lines.append(current)

    joined = " ".join(words)
    if " ".join(lines) != joined:
        last = lines[-1] if lines else ""
        lines[-1] = shorten(last + " " + " ".join(words[len(" ".join(lines).split()):]), width=max(12, len(last)), placeholder="...")

    return lines[:max_lines]


def image_reader_for_box(path: Path, width: int, height: int) -> ImageReader:
    with Image.open(path) as img:
        prepared = ImageOps.exif_transpose(img).convert("RGB")
        fitted = ImageOps.fit(prepared, (max(1, width), max(1, height)), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        buffer = BytesIO()
        fitted.save(buffer, format="JPEG", quality=90)
        buffer.seek(0)
        return ImageReader(buffer)


def draw_cover(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(BG)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    hero = image_reader_for_box(ROOT / "assets" / "products" / "SadhekoMomo.jpeg", int(PAGE_WIDTH * 0.88), int(PAGE_HEIGHT * 0.38))
    pdf.drawImage(hero, 34, PAGE_HEIGHT * 0.5 - 30, width=PAGE_WIDTH * 0.88, height=PAGE_HEIGHT * 0.38, mask="auto")

    pdf.setFillColor(CARD_BG)
    pdf.roundRect(40, 54, PAGE_WIDTH - 80, PAGE_HEIGHT * 0.34, 18, fill=1, stroke=0)
    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(1)
    pdf.roundRect(40, 54, PAGE_WIDTH - 80, PAGE_HEIGHT * 0.34, 18, fill=0, stroke=1)

    logo = image_reader_for_box(LOGO, 130, 130)
    pdf.drawImage(logo, 58, 225, width=86, height=86, mask="auto")

    pdf.setFillColor(ACCENT_DARK)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(160, 288, "Sagarmatha Momo")

    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 17)
    pdf.drawString(160, 264, "Picture Menu")

    pdf.setFillColor(TEXT)
    pdf.setFont("Helvetica", 13)
    cover_lines = [
        "Large photos and simple descriptions",
        "to make browsing easy and comfortable.",
        "",
        "Includes momos, curries, rice dishes,",
        "snacks, desserts, sides, and drinks.",
    ]
    y = 236
    for line in cover_lines:
        pdf.drawString(160, y, line)
        y -= 19

    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 11)
    pdf.drawString(36, 34, "Prepared from the current Sagarmatha Momo website menu and item photos.")
    pdf.showPage()


def draw_item_card(pdf: canvas.Canvas, item: dict[str, str], x: float, y: float, width: float, height: float) -> None:
    pdf.setFillColor(CARD_BG)
    pdf.roundRect(x, y, width, height, 16, fill=1, stroke=0)
    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(1)
    pdf.roundRect(x, y, width, height, 16, fill=0, stroke=1)

    padding = 12
    image_height = height * 0.64
    img_path = ROOT / item["image"]
    img_reader = image_reader_for_box(img_path, int(width - padding * 2), int(image_height))
    pdf.drawImage(
        img_reader,
        x + padding,
        y + height - padding - image_height,
        width=width - padding * 2,
        height=image_height,
        mask="auto",
    )

    text_left = x + 14
    name_y = y + height - padding - image_height - 26
    pdf.setFillColor(ACCENT_DARK)
    pdf.setFont("Helvetica-Bold", 13)
    name_lines = wrap_text(item["name"], "Helvetica-Bold", 13, width - 28, 2)
    for idx, line in enumerate(name_lines):
        pdf.drawString(text_left, name_y - idx * 15, line)

    desc_y = name_y - (len(name_lines) * 15) - 5
    pdf.setFillColor(TEXT)
    pdf.setFont("Helvetica", 9)
    desc_lines = wrap_text(item["description"], "Helvetica", 9, width - 28, 3)
    for idx, line in enumerate(desc_lines):
        pdf.drawString(text_left, desc_y - idx * 11, line)


def chunk_items(items_per_page: int) -> list[tuple[str, list[dict[str, str]]]]:
    pages: list[tuple[str, list[dict[str, str]]]] = []
    for section in MENU:
        items = section["items"]
        for start in range(0, len(items), items_per_page):
            pages.append((section["category"], items[start : start + items_per_page]))
    return pages


def draw_menu_pages(pdf: canvas.Canvas, items_per_page: int = 6) -> None:
    margin_x = 26
    top_band = 64
    bottom_margin = 24
    gutter_x = 14
    gutter_y = 14
    columns = 2
    rows = 3
    card_width = (PAGE_WIDTH - margin_x * 2 - gutter_x) / columns
    card_height = (PAGE_HEIGHT - top_band - bottom_margin - gutter_y * (rows - 1)) / rows

    for category, items in chunk_items(items_per_page):
        pdf.setFillColor(BG)
        pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        pdf.setFillColor(ACCENT_DARK)
        pdf.setFont("Helvetica-Bold", 24)
        pdf.drawString(margin_x, PAGE_HEIGHT - 36, category)
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica", 11)
        pdf.drawString(margin_x, PAGE_HEIGHT - 54, "Picture-first layout with larger text for easy reading.")

        positions = []
        for row in range(rows):
            for col in range(columns):
                x = margin_x + col * (card_width + gutter_x)
                y = PAGE_HEIGHT - top_band - card_height - row * (card_height + gutter_y)
                positions.append((x, y))

        for item, (x, y) in zip(items, positions):
            draw_item_card(pdf, item, x, y, card_width, card_height)

        pdf.showPage()


def main() -> None:
    for output_path in (OUTPUT, OUTPUT_VERTICAL):
        output_path.parent.mkdir(parents=True, exist_ok=True)

    vertical_pdf = canvas.Canvas(str(OUTPUT_VERTICAL), pagesize=PAGE_SIZE)
    vertical_pdf.setTitle("Sagarmatha Momo Picture Menu Vertical A4")
    vertical_pdf.setAuthor("OpenAI Codex")
    vertical_pdf.setSubject("Picture-forward menu PDF")
    draw_cover(vertical_pdf)
    draw_menu_pages(vertical_pdf, items_per_page=6)
    vertical_pdf.save()
    print(OUTPUT_VERTICAL)


if __name__ == "__main__":
    main()
