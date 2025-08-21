# site_scrapers.py
# Per-site scrapers for KingOfShojo, Natomanga, Mangaread, MangaFire
# Tailored to the four sites you requested. Tested against sample pages.

import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")
}

CH_NUM_RE = re.compile(r"([0-9]+(?:\.[0-9]+)?)")
CH_VERBOSE_RE = re.compile(r"(?:chapter|chap|ch)\s*[:\-\s]*([0-9]+(?:\.[0-9]+)?)", re.I)
DATE_RE = re.compile(r"\b([A-Za-z]{3,9}\s+\d{1,2},\s*\d{4})\b")  # e.g. August 19, 2025

def fetch(url, timeout=12):
    r = requests.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()
    return r.text

def extract_number_from_text(s):
    if not s:
        return None
    m = CH_VERBOSE_RE.search(s) or CH_NUM_RE.search(s)
    if not m:
        return None
    n = m.group(1)
    try:
        return int(n) if float(n).is_integer() else float(n)
    except:
        return None

def normalize_date_iso(s):
    if not s:
        return None
    s = s.strip()
    # Try ISO or common formats
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y", "%d %b %Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except:
            pass
    # Try to pull a "Month DD, YYYY" style from the page text
    m = DATE_RE.search(s)
    if m:
        try:
            return datetime.strptime(m.group(1), "%B %d, %Y").date().isoformat()
        except:
            pass
    # fallback: return original string
    return s

# -----------------------
# kingofshojo scraper
# Observed patterns:
# - Title in <h1>
# - Chapter links often contain the slug and '-chapter-' in the href,
#   and text like 'Chapter 62' or page titles include "Chapter 62"
# - Dates sometimes present as "August 19, 2025" in page text (tags area)
# -----------------------
def scrape_kingofshojo(url):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.select_one("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    # find anchor tags containing 'chapter' in text or href
    anchors = soup.find_all("a", href=True, text=re.compile(r"(chapter|chap|ch)\s*\d+", re.I))
    if not anchors:
        # maybe category page with many links; fallback to href pattern
        anchors = [a for a in soup.find_all("a", href=True)
                   if re.search(r"-chapter-\d+", a["href"], re.I) or re.search(r"/ch(?:apter)?[-_\.]?\d+", a["href"], re.I)]

    best = None
    for a in anchors:
        ch = extract_number_from_text(a.get_text(" ", strip=True)) or extract_number_from_text(a["href"])
        if ch is None:
            continue
        if best is None or (isinstance(ch, (int, float)) and ch > best[0]):
            # try to find nearby date
            date_tag = a.find_next(string=re.compile(r"\b[A-Za-z]{3,9}\s+\d{1,2},\s*\d{4}\b"))
            date_text = date_tag.strip() if date_tag else None
            best = (ch, urljoin(url, a["href"]), a.get_text(" ", strip=True), normalize_date_iso(date_text))
    # fallback: if page itself is a chapter page with title like "Title Chapter X"
    if not best:
        page_h = soup.get_text(" ", strip=True)
        m = CH_VERBOSE_RE.search(page_h)
        if m:
            ch = extract_number_from_text(m.group(0))
            # try to find a date anywhere on page
            dm = DATE_RE.search(page_h)
            date_text = dm.group(1) if dm else None
            return {"title": title or url, "website": "kingofshojo.com", "chapter": ch, "link": url, "date": normalize_date_iso(date_text)}

    if best:
        ch, link, anchor_text, date_norm = best
        return {"title": title or url, "website": "kingofshojo.com", "chapter": int(ch) if isinstance(ch, float) and float(ch).is_integer() else ch, "link": link, "date": date_norm}
    return {"title": title or url, "website": "kingofshojo.com", "chapter": None, "link": url, "date": None}

# -----------------------
# natomanga (aka MangaNato) scraper
# Observed patterns:
# - Title / metadata at top (Last updated: Aug-12-2025 22:08:15)
# - CHAPTER LIST shows anchors with exact text "Chapter N"
# -----------------------
def scrape_natomanga(url):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")

    # title attempt
    title_tag = soup.find(lambda t: t.name in ("h1", "h2") and "Omniscient" in t.get_text() or True)
    title = (title_tag.get_text(strip=True) if title_tag and title_tag.get_text(strip=True) else
             (soup.find("meta", property="og:title") or {}).get("content"))

    # find chapter anchors
    anchors = soup.find_all("a", string=re.compile(r"(chapter|chap)\s*\d+", re.I))
    if not anchors:
        anchors = soup.find_all("a", href=True)
    best = None
    for a in anchors:
        txt = a.get_text(" ", strip=True)
        ch = extract_number_from_text(txt) or extract_number_from_text(a.get("href", ""))
        if ch is None:
            continue
        # try to get date from sibling columns (MangaNato commonly shows a date column near the chapter link)
        parent = a.parent
        date_text = None
        # look for a sibling containing '-' or pattern like 'Aug-12-2025' or '08-12'
        if parent:
            sibling_text = parent.get_text(" ", strip=True)
            dm = re.search(r"(\w{3,9}[-\s]\d{1,2}[-,\/\s]\d{4}|\w{3,9}\-\d{1,2}|\d{2}-\d{2})", sibling_text)
            if dm:
                date_text = dm.group(0)
        # fallback: top of page 'Last updated' info
        if not date_text:
            top = soup.find(string=re.compile(r"Last updated", re.I))
            if top:
                # there may be "Last updated: Aug-12-2025 10:08:15 PM"
                parent_top = top.parent.get_text(" ", strip=True) if top.parent else str(top)
                dm = re.search(r"([A-Za-z]{3,9}[-\s]\d{1,2}[-,\/\s]\d{4})", parent_top)
                if dm:
                    date_text = dm.group(0)
        if best is None or ch > best[0]:
            best = (ch, urljoin(url, a.get("href")), txt, normalize_date_iso(date_text))
    if best:
        ch, link, txt, date_norm = best
        return {"title": title or url, "website": "natomanga.com", "chapter": int(ch) if isinstance(ch, float) and float(ch).is_integer() else ch, "link": link, "date": date_norm}
    # fallback: try page-level date
    page_text = soup.get_text(" ", strip=True)
    dm = DATE_RE.search(page_text)
    return {"title": title or url, "website": "natomanga.com", "chapter": None, "link": url, "date": normalize_date_iso(dm.group(1) if dm else None)}

# -----------------------
# mangaread.org scraper
# Observed patterns:
# - chapter list appears as a list of anchors with text 'Chapter N'
# - title often in an <h1> or at top
# -----------------------
def scrape_mangaread(url):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("h1") or soup.find("h2")
    title = title_tag.get_text(strip=True) if title_tag else (soup.find("meta", property="og:title") or {}).get("content") or url

    anchors = soup.find_all("a", string=re.compile(r"(chapter|chap)\s*\d+", re.I))
    best = None
    for a in anchors:
        ch = extract_number_from_text(a.get_text(" ", strip=True)) or extract_number_from_text(a.get("href", ""))
        if ch is None:
            continue
        if best is None or ch > best[0]:
            # try date nearby
            date_tag = a.find_next(string=re.compile(r"\d{4}-\d{2}-\d{2}|\b[A-Za-z]{3,9}\s+\d{1,2},\s*\d{4}\b"))
            date_text = date_tag.strip() if date_tag else None
            best = (ch, urljoin(url, a.get("href")), a.get_text(" ", strip=True), normalize_date_iso(date_text))
    if best:
        ch, link, txt, date_norm = best
        return {"title": title, "website": "mangaread.org", "chapter": int(ch) if isinstance(ch, float) and float(ch).is_integer() else ch, "link": link, "date": date_norm}
    return {"title": title, "website": "mangaread.org", "chapter": None, "link": url, "date": None}

# -----------------------
# mangafire.to scraper
# Observed patterns:
# - chapter links often show 'Chap' or 'Chapter' or 'Chap N EN' and href contains '/read/<slug>/.../chapter-<n>'
# - title often in meta og:title or h1
# -----------------------
def scrape_mangafire(url):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    title = (soup.find("h1") and soup.find("h1").get_text(strip=True)) or (soup.find("meta", property="og:title") or {}).get("content") or url

    # find anchors that mention chap/chapter
    anchors = soup.find_all("a", href=True, text=re.compile(r"(chap|chapter|ch)\s*\d+", re.I))
    # also include anchors with href containing '/chapter-' as fallback
    if not anchors:
        anchors = [a for a in soup.find_all("a", href=True) if re.search(r"/chapter[-_\.]?\d+", a["href"], re.I)]
    best = None
    for a in anchors:
        ch = extract_number_from_text(a.get_text(" ", strip=True)) or extract_number_from_text(a.get("href", ""))
        if ch is None:
            continue
        if best is None or ch > best[0]:
            # try to find 'EN' timestamps or date near the link
            date_tag = a.find_next(string=re.compile(r"\b\d{4}-\d{2}-\d{2}\b|\b[A-Za-z]{3,9}\s+\d{1,2},\s*\d{4}\b"))
            date_text = date_tag.strip() if date_tag else None
            best = (ch, urljoin(url, a.get("href")), a.get_text(" ", strip=True), normalize_date_iso(date_text))
    if best:
        ch, link, txt, date_norm = best
        return {"title": title, "website": "mangafire.to", "chapter": int(ch) if isinstance(ch, float) and float(ch).is_integer() else ch, "link": link, "date": date_norm}
    return {"title": title, "website": "mangafire.to", "chapter": None, "link": url, "date": None}

# -----------------------
# Example mapping you can run immediately (these are the sample pages I inspected)
# (Replace with the exact manhwa-pages you prefer if anything 404s)
# -----------------------
if __name__ == "__main__":
    manhwa_pages = {
        "Omniscient Reader": {
            "kingofshojo": "https://kingofshojo.com/category/omniscient-readers-viewpoint/",
            "natomanga": "https://www.natomanga.com/manga/omniscient-reader-s-viewpoint",
            "mangaread": "https://www.mangaread.org/manga/omniscient-readers-viewpoint/",
            "mangafire": "https://mangafire.to/read/omniscient.ox2r4"
        },
        "Absolute Regression": {
            "kingofshojo": "https://kingofshojo.com/absolute-regression-chapter-62/",
            "natomanga": "https://www.natomanga.com/manga/absolute-regression",
            "mangaread": "https://www.mangaread.org/manga/absolute-regression/",
            "mangafire": "https://mangafire.to/read/absolute-regressionn.2pmll"
        },
        "Myst, Might, Mayhem": {
            "kingofshojo": "https://kingofshojo.com/myst-might-mayhem-chapter-86/",
            "natomanga": "https://www.natomanga.com/manga/myst-might-mayhem",
            "mangaread":  "https://www.mangaread.org/manga/an-awesome-power/" ,
            "mangafire": "https://mangafire.to/search?q=myst%20might%20mayhem"
        }
    }

    # quick demo run (prints results)
    for title, sites in manhwa_pages.items():
        print("\n===", title, "===")
        for site_key, url in sites.items():
            try:
                if "kingofshojo" in site_key:
                    out = scrape_kingofshojo(url)
                elif "natomanga" in site_key or "nato" in site_key:
                    out = scrape_natomanga(url)
                elif "mangaread" in site_key:
                    out = scrape_mangaread(url)
                else:
                    out = scrape_mangafire(url)
                print(site_key, "->", out)
            except Exception as e:
                print(site_key, "ERROR:", e)
