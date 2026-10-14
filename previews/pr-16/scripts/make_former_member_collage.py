#!/usr/bin/env python3
from __future__ import annotations

import math
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUT_PNG = OUTPUT_DIR / "all_lab_members_collage_box_aspect.png"
OUT_PPTX = OUTPUT_DIR / "all_lab_members_collage_box_aspect.pptx"
OUT_MANIFEST = OUTPUT_DIR / "all_lab_members_collage_manifest.txt"

# Matches the reference box aspect ratio exactly: 1408 x 784.
CANVAS_W = 3520
CANVAS_H = 1960
MARGIN = 42
GAP = 8
BACKGROUND = (255, 255, 255)
ALLOWED_CASTES = {"grad", "postdoc", "undergrad", "tech"}


RAW_MANUAL_AVATARS = {
    "Zihou Wang": "images/people/Zihou.jpg",
    "Jiaxi Jake Zhao": "images/people/jakezhao.jpg",
    "Jiaxi Zhao": "images/people/jakezhao.jpg",
    "Jacques P Bothma": "previews/pr-6/images/people/former_people/jacques.jpg",
    "Jinny Chung": "previews/pr-6/images/people/former_people/jinnichung.jpg",
    "Yang Joon Kim": "previews/pr-6/images/people/former_people/yang.jpeg",
    "Gabriella Martini": "previews/pr-6/images/people/gabriella.jpg",
    "Josh Huang": "previews/pr-6/images/people/Josh.JPG",
    "Olivia Rourke": "previews/pr-6/images/people/Olivia.jpg",
    "Arman Karshenas": "previews/pr-6/images/people/armanKarshenas.jpg",
    "Emily Dong": "previews/pr-6/images/people/Emily.jpg",
    "Yuliana A Díaz Tirado": "previews/pr-6/images/people/Yuliana.jpeg",
    "Yuxin Yang": "previews/pr-6/images/people/Yuxin.jpg",
    "Jazmin Sandhu": "previews/pr-6/images/people/Jazmin.jpg",
    "Anisha Yeddanapudi": "previews/pr-6/images/people/Anisha.png",
    "Julian Davis": "previews/pr-6/images/people/JDavis.jpg",
    "Alicia Zhang": "previews/pr-6/images/people/AliciaZhang.png",
    "Simon Alamos": "previews/pr-6/images/people/former_people/simon.png",
    "Elizabeth Eck": "previews/pr-6/images/people/former_people/liz.jpg",
    "Pirooz Fereydouni": "previews/pr-6/images/people/former_people/pirooz.jpg",
    "Sydney Ghoreishi": "previews/pr-6/images/people/former_people/sydney.png",
    "Nicholas Lammers": "previews/pr-6/images/people/former_people/nick.jpg",
    "Jonathan Liu": "previews/pr-6/images/people/former_people/jonliu.jpg",
    "Armando Reimer": "previews/pr-6/images/people/former_people/armando.jpg",
    "Kaitlin Rhee": "previews/pr-6/images/people/former_people/kaitlin.jpg",
    "Clay Westrum": "previews/pr-6/images/people/former_people/clay.jpg",
    "Jordan Xiao": "previews/pr-6/images/people/former_people/jordanxiao.JPG",
    "Paul Talledo": "previews/pr-6/images/people/former_people/paultalledo.jpg",
    "Meghan Turner": "previews/pr-6/images/people/meghan.jpg",
    "Pranjal Srivastava": "previews/pr-6/images/people/pranjal.jpg",
}


def normalized_name(name: str) -> str:
    name = re.sub(r"\([^)]*\)", " ", name)
    name = re.sub(r"[^A-Za-z0-9]+", " ", name)
    return re.sub(r"\s+", " ", name).strip()


MANUAL_AVATARS = {normalized_name(name): path for name, path in RAW_MANUAL_AVATARS.items()}


def read_yaml(path: Path) -> list[dict]:
    """Parse the simple top-level list of key/value member records used here."""
    records: list[dict] = []
    current: dict | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            if current:
                records.append(current)
            current = {}
            line = line[2:]
        elif current is None or not line.startswith("  "):
            continue
        else:
            line = line.strip()

        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value in {">", "|"}:
            value = ""
        current[key.strip()] = value.strip("'\"")

    if current:
        records.append(current)
    return records


def image_map_from_old_yaml() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for item in read_yaml(ROOT / "_data" / "_old_former_members.yml"):
        avatar = item.get("avatar")
        name = item.get("name")
        if not avatar or not name:
            continue
        path = ROOT / "previews" / "pr-6" / "images" / "people" / "former_people" / avatar
        if path.exists():
            mapping[normalized_name(name)] = str(path.relative_to(ROOT))
    return mapping


def discover_image_by_name(name: str) -> str | None:
    key = normalized_name(name).lower().replace(" ", "")
    search_dirs = [
        ROOT / "images" / "people",
        ROOT / "previews" / "pr-6" / "images" / "people",
        ROOT / "previews" / "pr-6" / "images" / "people" / "former_people",
    ]
    candidates: list[Path] = []
    for directory in search_dirs:
        candidates.extend(p for p in directory.glob("*") if p.is_file())

    for path in candidates:
        stem = normalized_name(path.stem).lower().replace(" ", "")
        if stem == key:
            return str(path.relative_to(ROOT))

    parts = key.split()
    compact_parts = normalized_name(name).lower().split()
    if compact_parts:
        first, last = compact_parts[0], compact_parts[-1]
        for path in candidates:
            stem = normalized_name(path.stem).lower().replace(" ", "")
            if first in stem and last in stem:
                return str(path.relative_to(ROOT))
    return None


def former_people_with_images() -> tuple[list[dict], list[str]]:
    old_map = image_map_from_old_yaml()
    people: list[dict] = []
    missing: list[str] = []
    seen_paths: set[str] = set()

    for person in read_yaml(ROOT / "_data" / "former_members.yaml"):
        caste = (person.get("caste") or "").strip()
        if caste not in ALLOWED_CASTES:
            continue

        display_name = person["name"]
        key = normalized_name(display_name)
        rel_path = MANUAL_AVATARS.get(key) or old_map.get(key) or discover_image_by_name(display_name)
        if not rel_path:
            missing.append(f"{display_name} [{caste}]")
            continue

        abs_path = ROOT / rel_path
        if not abs_path.exists() or rel_path in seen_paths:
            missing.append(f"{display_name} [{caste}]")
            continue

        seen_paths.add(rel_path)
        people.append(
            {
                "name": display_name,
                "caste": caste,
                "path": abs_path,
                "rel_path": rel_path,
                "status": "former",
            }
        )

    return people, missing


def current_people_with_images() -> tuple[list[dict], list[str]]:
    people: list[dict] = []
    missing: list[str] = []

    for person in read_yaml(ROOT / "_data" / "members.yml"):
        caste = (person.get("caste") or "").strip()
        if caste not in ALLOWED_CASTES:
            continue

        display_name = person["name"]
        avatar = person.get("avatar")
        if not avatar:
            missing.append(f"{display_name} [{caste}]")
            continue

        rel_path = f"images/people/{avatar}"
        abs_path = ROOT / rel_path
        if not abs_path.exists():
            missing.append(f"{display_name} [{caste}]")
            continue

        people.append(
            {
                "name": display_name,
                "caste": caste,
                "path": abs_path,
                "rel_path": rel_path,
                "status": "current",
            }
        )

    return people, missing


def best_grid(count: int, canvas_w: int, canvas_h: int) -> tuple[int, int, int, int]:
    usable_w = canvas_w - 2 * MARGIN
    usable_h = canvas_h - 2 * MARGIN
    best = None
    for rows in range(1, count + 1):
        cols = math.ceil(count / rows)
        tile_w = (usable_w - GAP * (cols - 1)) // cols
        tile_h = (usable_h - GAP * (rows - 1)) // rows
        score = min(tile_w, tile_h) * 10000 - abs(tile_w - tile_h)
        if best is None or score > best[0]:
            best = (score, rows, cols, tile_w, tile_h)
    assert best is not None
    _, rows, cols, tile_w, tile_h = best
    return rows, cols, tile_w, tile_h


def crop_to_tile(path: Path, size: tuple[int, int]) -> Image.Image:
    img = Image.open(path)
    img = ImageOps.exif_transpose(img).convert("RGB")
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.38))


def make_collage(people: list[dict]) -> None:
    rows, cols, tile_w, tile_h = best_grid(len(people), CANVAS_W, CANVAS_H)
    content_w = cols * tile_w + (cols - 1) * GAP
    content_h = rows * tile_h + (rows - 1) * GAP
    start_x = (CANVAS_W - content_w) // 2
    start_y = (CANVAS_H - content_h) // 2

    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), BACKGROUND)
    for idx, person in enumerate(people):
        row = idx // cols
        col = idx % cols
        row_count = min(cols, len(people) - row * cols)
        row_w = row_count * tile_w + (row_count - 1) * GAP
        row_start_x = (CANVAS_W - row_w) // 2
        x = row_start_x + col * (tile_w + GAP)
        y = start_y + row * (tile_h + GAP)
        tile = crop_to_tile(person["path"], (tile_w, tile_h))
        canvas.paste(tile, (x, y))

    canvas.save(OUT_PNG, dpi=(300, 300), quality=95)


def create_minimal_pptx() -> None:
    # 14.08 x 7.84 inches in English Metric Units, matching the reference box.
    slide_w = 12874752
    slide_h = 7168896
    image_name = OUT_PNG.name

    files = {
        "[Content_Types].xml": f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="png" ContentType="image/png"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
</Types>""",
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>""",
        "ppt/_rels/presentation.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
</Relationships>""",
        "ppt/presentation.xml": f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId2"/></p:sldMasterIdLst>
  <p:sldIdLst><p:sldId id="256" r:id="rId1"/></p:sldIdLst>
  <p:sldSz cx="{slide_w}" cy="{slide_h}" type="custom"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>""",
        "ppt/slides/_rels/slide1.xml.rels": f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{escape(image_name)}"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>""",
        "ppt/slides/slide1.xml": f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree>
    <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
    <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    <p:pic>
      <p:nvPicPr><p:cNvPr id="2" name="{escape(image_name)}"/><p:cNvPicPr/><p:nvPr/></p:nvPicPr>
      <p:blipFill><a:blip r:embed="rId1"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
      <p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{slide_w}" cy="{slide_h}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>
    </p:pic>
  </p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>""",
        "ppt/slideMasters/_rels/slideMaster1.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>""",
        "ppt/slideMasters/slideMaster1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
</p:sldMaster>""",
        "ppt/slideLayouts/_rels/slideLayout1.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>""",
        "ppt/slideLayouts/slideLayout1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>""",
    }

    with zipfile.ZipFile(OUT_PPTX, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in files.items():
            archive.writestr(name, data)
        archive.write(OUT_PNG, f"ppt/media/{image_name}")


def write_manifest(people: list[dict], missing: list[str]) -> None:
    lines = [
        f"Generated: {OUT_PNG.name}",
        f"Canvas size: {CANVAS_W} x {CANVAS_H} px, 300 dpi",
        "Aspect ratio source: 1408 x 784 reference box",
        f"Included photos: {len(people)}",
        "",
    ]
    for person in people:
        lines.append(
            f"- {person['name']} [{person['status']}, {person['caste']}]: {person['rel_path']}"
        )
    if missing:
        lines.extend(["", f"Missing photo matches: {len(missing)}"])
        lines.extend(f"- {item}" for item in missing)
    OUT_MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    current_people, current_missing = current_people_with_images()
    former_people, former_missing = former_people_with_images()
    people = current_people + former_people
    missing = current_missing + former_missing
    make_collage(people)
    create_minimal_pptx()
    write_manifest(people, missing)
    print(f"Included {len(people)} photos")
    print(f"Missing {len(missing)} photo matches")
    print(OUT_PNG)
    print(OUT_PPTX)
    print(OUT_MANIFEST)


if __name__ == "__main__":
    main()
