"""Oyun sitesi paketlerini üretir: dist/<site>/index.html ve dist/<site>.zip

Kullanım: python3 tools/build_platforms.py [GameDistribution oyun kimliği] [GoatCounter kodu]
Kaynak: depo kökündeki index.html (GitHub sayfası sürümü).
"""
import os, re, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gd_id = sys.argv[1] if len(sys.argv) > 1 else "GD_GAME_ID"
stats = sys.argv[2] if len(sys.argv) > 2 else ""

HEADS = {
    "crazygames": '<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>\n'
                  "<script>window.__PLATFORM='crazygames';window.__ADS=false</script>\n",  # Basic Launch: reklamsız. Full Launch'ta __ADS=false kaldırılır.
    "poki": '<script src="https://game-cdn.poki.com/scripts/v2/poki-sdk.js"></script>\n'
            "<script>window.__PLATFORM='poki'</script>\n",
    "gamedistribution": "<script>window.__PLATFORM='gamedistribution';"
        'window.GD_OPTIONS={gameId:"' + gd_id + '",onEvent:function(e){window.__gdEvent&&window.__gdEvent(e)}};'
        "(function(d,s,id){var js,f=d.getElementsByTagName(s)[0];if(d.getElementById(id))return;"
        "js=d.createElement(s);js.id=id;js.src='https://html5.api.gamedistribution.com/main.min.js';"
        "f.parentNode.insertBefore(js,f)}(document,'script','gamedistribution-jssdk'));</script>\n",
}
EXTRA_CSS = "<style>body{-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}</style>\n"

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
# Telefon uygulaması (PWA) etiketleri oyun sitelerinde gerekmez
src = re.sub(r"<!--pwa-->.*?<!--/pwa-->\n?", "", src, flags=re.S)
marker = '<meta name="viewport"'
i = src.index(marker)
i = src.index(">", i) + 1
for name, head in HEADS.items():
    st = "<script>window.__STATS='" + stats + "'</script>\n" if stats else ""
    out = src[:i] + "\n" + head + st + EXTRA_CSS + src[i:]
    d = os.path.join(ROOT, "dist", name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)
    with zipfile.ZipFile(os.path.join(ROOT, "dist", name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(d, "index.html"), "index.html")
    print("hazır:", name)
