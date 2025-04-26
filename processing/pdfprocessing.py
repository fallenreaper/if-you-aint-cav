from typing import List
from pypdf import PdfReader
import re
from pprint import pprint


def extract(path) -> List[str]:
    reader = PdfReader(path)
    rslt = []
    for idx in range(reader.get_num_pages()):
        [rslt.append(x.strip()) for x in reader.get_page(idx).extract_text().split("\n") if "ATP 3-20.98" not in x]
    return rslt

def isUsefulText(s: str) -> bool:
    """if a given string does not meet the criteria to be used in content creation"""
    # if "ATP 3-20.98" in s: return False
    if s == s.upper(): return False
    return True


def extract_all_images_from_pdf(path, img_folder="./pdfimages"):
    reader = PdfReader(path)
    import os
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
    for i in range(reader.get_num_pages()):
        page = reader.get_page(i)
        for (count, imgdata) in enumerate(page.images):
            with open(f"{img_folder}/pg{i}_img{imgdata.name}", "wb") as fp:
                fp.write(imgdata.data)

def capture_paragraph_per_topic(data: List[str], topic) -> str:
    """Given a Topic, will return the first Paragraph"""
    try:
        idx = data.index(topic)
    except ValueError:
        return "<topic not found>"
    current = idx+1
    content = []
    compiled_re=re.compile(r"\d+-\d+")
    while True:
        c = data[current]
        if isUsefulText(c):
            content.append(c)
        next = current + 1
        _stringlist = data[next].split(".")
        if len(_stringlist) > 0 and compiled_re.match(_stringlist[0]):
            break
        current = next
    return "".join(content)


if __name__ == "__main__":
    path = "ATP_3-20.98.pdf"
    data = extract(path)

    print(data)

    content = {
        # Forms of X
        "formsofsecurity": capture_paragraph_per_topic(data, "SECTION II – FORMS OF SECURITY TASKS"),
        "formsofrecon": capture_paragraph_per_topic(data, "SECTION II – FORMS OF RECONNAISSANCE"),

        # Forms of Security - details
        "screen": capture_paragraph_per_topic(data, "SCREEN"),
        "guard": capture_paragraph_per_topic(data, "GUARD"),
        "cover": capture_paragraph_per_topic(data, "COVER"),
        "area": capture_paragraph_per_topic(data, "AREA SECURITY"),
        "local": capture_paragraph_per_topic(data, "LOCAL SECURITY"),

        # Forms of Recon - details
        "zone": capture_paragraph_per_topic(data, "ZONE RECONNAISSANCE"),
        "area": capture_paragraph_per_topic(data, "AREA RECONNAISSANCE"),
        "route": capture_paragraph_per_topic(data, "ROUTE RECONNAISSANCE"),
        "reconinforce": capture_paragraph_per_topic(data, "RECONNAISSANCE IN FORCE"),
        "specialrecon": capture_paragraph_per_topic(data, "SPECIAL RECONNAISSANCE"),

        # Recon Handover
        "rho": capture_paragraph_per_topic(data, "SECTION III – RECONNAISSANCE HANDOVER"),

        "passageoflines": capture_paragraph_per_topic(data, "PASSAGE OF LINES"),

        #DIDEA / Scout OODA Loop
        "didea": capture_paragraph_per_topic(data, "Figure 4-28. Direct fire engagement process")
    }

    pprint(content)

    extract_all_images_from_pdf(path)

    