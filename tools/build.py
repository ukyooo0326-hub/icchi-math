#!/usr/bin/env python3
"""原稿（chu/*.md, kou/*.md）を 1 枚の HTML（dist/index.html）にビルドする。

使い方:
  python3 tools/build.py          # ビルド
  python3 tools/build.py --check  # 記法チェックのみ（警告を表示）
"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = [
    ("chu", "中学生版", "中1 → 中3"),
    ("kou", "高校生版", "数I → 数A → 数II → 数B → 数C / 数III"),
]
NAMES = {
    "イッチ": ("イッチ", "◆Icchi/Math", "icchi"),
    "古参ニキ": ("古参ニキ", "◆Kosan.Niki", "niki"),
    "名無し": ("名無しさん@数学スレ", "", "nanashi"),
}
STEPS = {"①": "全体を見る", "②": "知識の利用", "③": "部分を見る", "④": "工夫する"}
BLOCKS = {"point", "warn", "exercise", "answer", "check"}
WEEK = "月火水木金土日"

warnings = []


def warn(src, lineno, msg):
    warnings.append(f"{src}:{lineno}: {msg}")


# ---------- inline ----------

MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$")


def inline(text, src="", lineno=0, chap=""):
    maths = []

    def stash(m):
        if "[[" in m.group(0) or "]]" in m.group(0):
            warn(src, lineno, "数式 $...$ の中に [[ ]] があります（[[$...$]] の順に書く）")
        if m.group(1) is not None:
            maths.append("\\[" + m.group(1) + "\\]")
        else:
            maths.append("\\(" + m.group(2) + "\\)")
        return f"\x00{len(maths) - 1}\x00"

    t = MATH_RE.sub(stash, text)
    if "$" in t:
        warn(src, lineno, "閉じていない $ があります")
    if t.count("[[") != t.count("]]"):
        warn(src, lineno, "[[ ]] の対応がとれていません")
    t = html.escape(t, quote=False)
    t = re.sub(r"\[\[(.+?)\]\]", r'<span class="red" tabindex="0">\1</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)

    def badge(m):
        num, label = m.group(1), m.group(2)
        base = label.split("（")[0]
        if STEPS[num] != base:
            warn(src, lineno, f"ステップ表記が規約と違います: 【{num}{label}】")
        return f'<span class="step s{"①②③④".index(num) + 1}"><b>{num}</b>{label}</span>'

    t = re.sub(r"【([①②③④])([^】]*)】", badge, t)
    t = re.sub(
        r"&gt;&gt;(\d+)",
        lambda m: f'<a class="anc" href="#{chap}-{m.group(1)}" data-to="{chap}-{m.group(1)}">&gt;&gt;{m.group(1)}</a>',
        t,
    )
    t = re.sub(r"\x00(\d+)\x00", lambda m: html.escape(maths[int(m.group(1))], quote=False), t)
    return t


def is_display(line):
    s = line.strip()
    return s.startswith("$$") and s.endswith("$$") and len(s) > 4


def render_post_body(lines, src, start, chap):
    out, buf = [], []
    for i, line in lines:
        if is_display(line):
            if buf:
                out.append("<p>" + "<br>".join(buf) + "</p>")
                buf = []
            out.append('<div class="dm">' + inline(line.strip(), src, i, chap) + "</div>")
        elif line.strip() == "":
            if buf:
                out.append("<p>" + "<br>".join(buf) + "</p>")
                buf = []
        else:
            buf.append(inline(line, src, i, chap))
    if buf:
        out.append("<p>" + "<br>".join(buf) + "</p>")
    return "".join(out)


def render_block_body(lines, src, chap):
    out, para, lst, ltype, table = [], [], [], None, []

    def flush():
        nonlocal para, lst, ltype, table
        if para:
            out.append("<p>" + "<br>".join(para) + "</p>")
            para = []
        if lst:
            out.append(f"<{ltype}>" + "".join(f"<li>{x}</li>" for x in lst) + f"</{ltype}>")
            lst, ltype = [], None
        if table:
            rows = [r for r in table if not re.fullmatch(r"\|?[\s:\-|]+\|?", r[1])]
            h = []
            for k, (i, r) in enumerate(rows):
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                tag = "th" if k == 0 else "td"
                h.append("<tr>" + "".join(f"<{tag}>{inline(c, src, i, chap)}</{tag}>" for c in cells) + "</tr>")
            out.append('<div class="tw"><table>' + "".join(h) + "</table></div>")
            table = []

    for i, line in lines:
        s = line.strip()
        m_ul = re.match(r"^\s*[-・]\s+(.*)", line)
        m_ol = re.match(r"^\s*\d+[.)]\s+(.*)", line)
        if s == "":
            flush()
        elif is_display(line):
            flush()
            out.append('<div class="dm">' + inline(s, src, i, chap) + "</div>")
        elif s.startswith("|"):
            if para or lst:
                flush()
            table.append((i, s))
        elif m_ul or m_ol:
            t = "ul" if m_ul else "ol"
            if para or table or (ltype and ltype != t):
                flush()
            ltype = t
            lst.append(inline((m_ul or m_ol).group(1), src, i, chap))
        else:
            if lst or table:
                flush()
            para.append(inline(line, src, i, chap))
    flush()
    return "".join(out)


# ---------- chapter ----------

def stable(seed, n=8):
    return hashlib.sha1(seed.encode()).hexdigest()[:n]


def parse_chapter(path, book):
    src = f"{book}/{path.name}"
    text = path.read_text(encoding="utf-8")
    meta = {}
    lines = text.split("\n")
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            if ":" in lines[i]:
                k, v = lines[i].split(":", 1)
                meta[k.strip()] = v.strip()
            i += 1
        i += 1
    else:
        warn(src, 1, "フロントマターがありません")
    for k in ("title", "unit", "goal"):
        if k not in meta:
            warn(src, 1, f"フロントマターに {k} がありません")

    chap = book + "-" + path.stem.split("_")[0]
    items = []  # ("post", n, name, [(lineno, line)]) / ("block", type, title, [...]) / ("h2", text)
    cur = None
    while i < len(lines):
        line = lines[i]
        ln = i + 1
        m_post = re.match(r"^@(\d+)\s+(\S+)\s*$", line)
        m_blk = re.match(r"^:::(\w+)\s*(.*)$", line)
        if cur and cur[0] == "block":
            if line.strip() == ":::":
                items.append(cur)
                cur = None
            else:
                cur[3].append((ln, line))
        elif m_post:
            if cur:
                items.append(cur)
            cur = ["post", int(m_post.group(1)), m_post.group(2), [], ln]
        elif m_blk:
            if cur:
                items.append(cur)
            btype = m_blk.group(1)
            if btype not in BLOCKS:
                warn(src, ln, f"未知のブロック :::{btype}")
            cur = ["block", btype, m_blk.group(2).strip(), [], ln]
        elif line.startswith("## "):
            if cur:
                items.append(cur)
                cur = None
            items.append(["h2", line[3:].strip()])
        else:
            if cur:
                cur[3].append((ln, line))
            elif line.strip():
                warn(src, ln, "レス・ブロックの外に本文があります")
        i += 1
    if cur:
        if cur[0] == "block":
            warn(src, cur[4], f":::{cur[1]} が閉じていません")
        items.append(cur)

    # checks
    nums = [it[1] for it in items if it[0] == "post"]
    for k, n in enumerate(nums):
        if n != k + 1:
            warn(src, 0, f"レス番号が連番ではありません（{k + 1} 番目が {n}）")
            break
    numset = set(nums)
    prev = None
    for it in items:
        if it[0] == "post":
            if it[2] not in NAMES:
                warn(src, it[4], f"未知の名前: {it[2]}")
            body = [l for _, l in it[3] if l.strip()]
            if len(body) > 7:
                warn(src, it[4], f">>{it[1]} が {len(body)} 行あります（6 行目安）")
            for ln, l in it[3]:
                for a in re.findall(r">>(\d+)", l):
                    if int(a) not in numset:
                        warn(src, ln, f"存在しないレスへのアンカー >>{a}")
                    elif int(a) >= it[1]:
                        warn(src, ln, f"未来のレスへのアンカー >>{a}")
                if "【" in l and "名無し" == it[2] and re.search(r"【[①②③④]", l):
                    warn(src, ln, "名無しがステップバッジを使っています")
        if it[0] == "block" and it[1] == "answer" and not (prev and prev[0] == "block" and prev[1] == "exercise"):
            warn(src, it[4], ":::answer の直前が :::exercise ではありません")
        prev = it
    return meta, chap, items, src


def render_chapter(meta, chap, items, src, index):
    h = []
    title = meta.get("title", "")
    h.append(f'<article class="chap" id="{chap}" data-chap="{chap}" hidden>')
    h.append('<header class="thread-head">')
    h.append(f'<p class="unit">{html.escape(meta.get("unit", ""))}</p>')
    h.append(f'<h1 class="ttl">{inline(title, src, 1, chap)}</h1>')
    rows = [("ゴール", meta.get("goal")), ("前提", meta.get("prereq")), ("このスレの核", meta.get("core"))]
    h.append('<dl class="meta">' + "".join(
        f"<div><dt>{k}</dt><dd>{inline(v, src, 1, chap)}</dd></div>" for k, v in rows if v) + "</dl>")
    h.append("</header>")
    h.append('<div class="thread">')
    sec = 0
    day = 1 + index % 27
    for it in items:
        if it[0] == "post":
            n, name = it[1], it[2]
            disp, trip, cls = NAMES.get(name, (name, "", "nanashi"))
            sec += 37 + (int(stable(chap + str(n), 2), 16) % 90)
            hh, mm, ss = 21 + sec // 3600, (sec // 60) % 60, sec % 60
            date = f"2026/04/{day:02d}({WEEK[(day + 1) % 7]}) {hh:02d}:{mm:02d}:{ss:02d}.{int(stable(str(n) + chap, 2), 16) % 100:02d}"
            pid = "Icchi" + stable(chap, 4) if cls == "icchi" else stable(chap + name + (str(n) if cls == "nanashi" else ""), 8)
            body = render_post_body(it[3], src, it[4], chap)
            h.append(
                f'<section class="post {cls}" id="{chap}-{n}">'
                f'<div class="ph"><a class="no" href="#{chap}-{n}">{n}</a>'
                f'<span class="nm">{html.escape(disp)}</span>'
                + (f'<span class="trip">{trip}</span>' if trip else "")
                + f'<span class="dt">{date}</span><span class="id">ID:{pid}</span></div>'
                f'<div class="pb">{body}</div></section>'
            )
        elif it[0] == "block":
            btype, btitle = it[1], it[2]
            body = render_block_body(it[3], src, chap)
            label = {"point": "まとめ", "warn": "注意", "exercise": "練習問題", "answer": "解答", "check": "チェック"}.get(btype, btype)
            if btype == "answer":
                h.append(f'<details class="blk answer"><summary>解答をひらく</summary><div class="bb">{body}</div></details>')
            else:
                t = inline(btitle, src, it[4], chap) if btitle else ""
                lvl = f' data-level="{html.escape(btitle)}"' if btype == "exercise" else ""
                h.append(
                    f'<div class="blk {btype}"{lvl}><div class="bh"><span class="bl">{label}</span>'
                    + (f'<span class="bt">{t}</span>' if t else "")
                    + f'</div><div class="bb">{body}</div></div>'
                )
        elif it[0] == "h2":
            h.append(f'<h2 class="sec">{inline(it[1], src, 0, chap)}</h2>')
    h.append("</div></article>")
    return "".join(h)


def ordered_files(book):
    """docs/curriculum.md の表に書かれた順（＝履修順）で並べる。表にないファイルは末尾に。"""
    cur = (ROOT / "docs" / "curriculum.md").read_text(encoding="utf-8")
    files = {f.name: f for f in (ROOT / book).glob("*.md")}
    out = []
    section = cur.split(f"（`{book}/`）")[1].split("\n## ")[0] if f"（`{book}/`）" in cur else ""
    for name in re.findall(r"^\| `([^`]+\.md)`", section, re.M):
        if name in files:
            out.append(files.pop(name))
        else:
            warn(f"{book}/{name}", 0, "目次にあるがファイルがありません")
    for name in sorted(files):
        warn(f"{book}/{name}", 0, "目次（docs/curriculum.md）に載っていません")
        out.append(files[name])
    return out


def main():
    check_only = "--check" in sys.argv
    toc, arts = [], []
    idx = 0
    for book, bname, order in BOOKS:
        files = ordered_files(book)
        entries = []
        for f in files:
            meta, chap, items, src = parse_chapter(f, book)
            arts.append(render_chapter(meta, chap, items, src, idx))
            idx += 1
            unit = meta.get("unit", f.stem)
            grade, _, uname = unit.partition("・")
            grade = grade.replace("数学", "数")
            if f.stem.startswith("0-00"):
                grade, uname = "はじめに", "高校数学と4ステップ" if uname in ("", "はじめに") else uname
            entries.append({"id": chap, "grade": grade, "unit": uname or unit,
                            "posts": sum(1 for it in items if it[0] == "post")})
        toc.append({"book": book, "name": bname, "order": order, "chapters": entries})

    for w in warnings:
        print("WARN", w)
    print(f"{len(warnings)} warnings, {idx} chapters")
    if check_only:
        sys.exit(1 if warnings else 0)

    tpl = (ROOT / "tools" / "template.html").read_text(encoding="utf-8")
    out = tpl.replace("/*__TOC__*/", json.dumps(toc, ensure_ascii=False)).replace("<!--__CHAPTERS__-->", "\n".join(arts))
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "index.html").write_text(out, encoding="utf-8")
    print("wrote dist/index.html", f"{len(out) // 1024} KB")


if __name__ == "__main__":
    main()
