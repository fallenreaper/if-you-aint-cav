"""Needs to make sure python3 runtime has:  pypdf and pypdf[image]"""
#!/bin/python3

# python3 -m venv ./venv
# source ./venv/bin/activate

from typing import List
from pypdf import PdfReader
import re
import json
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
    if s.startswith("Chapter"): return False
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
    return " ".join(content)


if __name__ == "__main__":
    path = "ATP_3-20.98.pdf"
    data = extract(path)

    print(data)

    content = {
        # Forms of X
        "formsofsecurity": { "title": "Forms of Security", "text": capture_paragraph_per_topic(data, "SECTION II – FORMS OF SECURITY TASKS")},
        "formsofrecon": { "title": "Forms of Reconnaissance", "text": capture_paragraph_per_topic(data, "SECTION II – FORMS OF RECONNAISSANCE")},

        # Forms of Security - details
        "screen": { "title": "Screen", "text": capture_paragraph_per_topic(data, "SCREEN")},
        "guard": { "title": "Guard", "text": capture_paragraph_per_topic(data, "GUARD")},
        "cover":  { "title": "Cover", "text": capture_paragraph_per_topic(data, "COVER")},
        "area": { "title": "Area Security", "text": capture_paragraph_per_topic(data, "AREA SECURITY")},
        "local": { "title": "Local Security", "text": capture_paragraph_per_topic(data, "LOCAL SECURITY")},

        # Forms of Recon - details
        "zone": { "title": "Zone Recon", "text": capture_paragraph_per_topic(data, "ZONE RECONNAISSANCE")},
        "area": { "title": "Area Recon", "text": capture_paragraph_per_topic(data, "AREA RECONNAISSANCE")},
        "route": { "title": "Route Recon", "text": capture_paragraph_per_topic(data, "ROUTE RECONNAISSANCE")},
        "reconinforce": { "title": "Recon in Force", "text": capture_paragraph_per_topic(data, "RECONNAISSANCE IN FORCE")},
        "specialrecon": { "title": "Special Recon", "text": capture_paragraph_per_topic(data, "SPECIAL RECONNAISSANCE")},

        # Recon Handover
        "rho": { "title": "Recon Handover", "text": capture_paragraph_per_topic(data,"SECTION III – RECONNAISSANCE HANDOVER")},

        "passageoflines": { "title": "Passage of Lines", "text": capture_paragraph_per_topic(data, "PASSAGE OF LINES")},

        #DIDEA / Scout OODA Loop
        "didea": { "title": "DIDEA", "text": capture_paragraph_per_topic(data, "Figure 4-28. Direct fire engagement process")},

        "dangerareas": { "title": "Danger Areas", "text": capture_paragraph_per_topic(data, "DANGER AREAS")},
    }

    pprint(content)

    with open("extraction.json", "w+") as fp:
        # json.dump(fp, content)
        fp.write(json.dumps(content))

    # No need to extract images at this time.
    # extract_all_images_from_pdf(path)

    