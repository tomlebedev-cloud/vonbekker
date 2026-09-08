#!/usr/bin/env python3
"""Builds index.html (standalone site) and artifact.html (Artifact-wrapped preview)
from body.part.html + assets/martynas-portrait.jpg."""
import base64, pathlib

root = pathlib.Path(__file__).parent
part = (root / "body.part.html").read_text(encoding="utf-8")
b64 = base64.b64encode((root / "assets/martynas-portrait.jpg").read_bytes()).decode()
part = part.replace("__PORTRAIT__", "data:image/jpeg;base64," + b64)

# Artifact version: no doctype/html/head/body — the host supplies those.
(root / "artifact.html").write_text(part, encoding="utf-8")

# Standalone version for hosting (GitHub Pages, any static host).
DESC = ("Martynas Švėgžda von Bekkeris — smuikininkas, Lietuvos muzikos ir teatro akademijos "
        "ir Hamburgo Johanneso Brahmso konservatorijos docentas.")
head = f"""<!doctype html>
<html lang="lt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#131110">
<meta property="og:type" content="profile">
<meta property="og:title" content="Martynas Švėgžda von Bekkeris">
<meta property="og:description" content="{DESC}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23131110'/><text y='23' x='16' text-anchor='middle' font-family='Georgia,serif' font-size='20' fill='%23C68A42'>M</text></svg>">
"""
# <title>/<link>/<style> belong in <head>; everything after </style> is the body.
split = part.index("</style>") + len("</style>")
(root / "index.html").write_text(
    head + part[:split] + "\n</head>\n<body>\n" + part[split:] + "\n</body>\n</html>\n",
    encoding="utf-8")
print("built index.html + artifact.html")
