import json
from pathlib import Path

# Load prompts
with open("prompts/canada_prompts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cards = []
for p in data["pages"]:
    num = p["page_number"]
    title = p.get("display_title", p.get("title", f"Page {num}"))
    prov = p.get("display_province", p.get("province", "Canada"))
    src = f"assets/canada/processed/page_{num:02d}_clean.png"
    caption = f"{title} ({prov}) — Traditional Dong Ho Multi-Layer Woodblock."
    
    card = f"""        <article class="page-card" data-page="{num}">
          <div class="page-card-header">
            <span class="page-num">Page {num:02d}</span>
            <span class="badge-province">{prov}</span>
          </div>
          <div class="page-preview-frame">
            <img src="{src}" alt="{title}" class="page-preview-img" loading="lazy" />
          </div>
          <h3 class="page-title">{title}</h3>
          <p class="page-caption">"{caption}"</p>
          <div class="prompt-copy-btns">
            <a href="{src}" download="page_{num:02d}.png" class="btn-copy" style="text-align:center;text-decoration:none;">Download PNG</a>
          </div>
        </article>"""
    cards.append(card)

cards_html = "\n".join(cards)

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace section-subtitle
content = content.replace(
    '<p class="section-subtitle">24 peaceful hours in the life of Barnaby the Capybara across 4 distinct chapters.</p>',
    '<p class="section-subtitle">30 celebrated national landmarks across 6 geographic regions in Dong Ho Layered Woodblock style.</p>'
)

# Replace tab-controls
old_tabs = """      <div class="tab-controls">
        <button class="tab-btn active" data-chapter="all">All 30 Pages</button>
        <button class="tab-btn" data-chapter="1">Part 1: Morning Calm (1-8)</button>
        <button class="tab-btn" data-chapter="2">Part 2: Work &amp; Friendship (9-16)</button>
        <button class="tab-btn" data-chapter="3">Part 3: Gentle Nature (17-24)</button>
        <button class="tab-btn" data-chapter="4">Part 4: Cozy Night (25-30)</button>
      </div>"""

new_tabs = """      <div class="tab-controls">
        <button class="tab-btn active" data-filter="all">All 30 Scenes</button>
        <button class="tab-btn" data-filter="central">Central (ON &amp; QC)</button>
        <button class="tab-btn" data-filter="west">Western &amp; Pacific (AB &amp; BC)</button>
        <button class="tab-btn" data-filter="atlantic">Atlantic Canada (NS, NB, PEI, NL)</button>
        <button class="tab-btn" data-filter="prairie_north">Prairies &amp; North (MB, SK, YT, NWT)</button>
      </div>"""

content = content.replace(old_tabs, new_tabs)

# Replace empty pages-grid
old_grid = """      <div id="pages-grid" class="pages-grid">
        <!-- Rendered dynamically by app.js -->
      </div>"""

new_grid = f"""      <div id="pages-grid" class="pages-grid">
{cards_html}
      </div>"""

content = content.replace(old_grid, new_grid)

# Replace KDP keywords
old_keywords = """              <li><strong>Box 1:</strong> <code>cute simple relaxing aesthetic hygge cottagecore</code></li>
              <li><strong>Box 2:</strong> <code>stress relief relaxation adults teens seniors beginners</code></li>
              <li><strong>Box 3:</strong> <code>mindful mindfulness calming anxiety therapy gift</code></li>
              <li><strong>Box 4:</strong> <code>quirky animals doing human things funny kawaii daily</code></li>
              <li><strong>Box 5:</strong> <code>thick lines large print easy cozy spaces cafe rooms</code></li>
              <li><strong>Box 6:</strong> <code>mindful coloring pages quick daily chill self care</code></li>
              <li><strong>Box 7:</strong> <code>alcohol marker friendly single sided pages animal lover</code></li>"""

new_keywords = """              <li><strong>Box 1:</strong> <code>canada travel coloring book scenic landscapes fall foliage</code></li>
              <li><strong>Box 2:</strong> <code>national parks adult relaxation stress relief nature lovers</code></li>
              <li><strong>Box 3:</strong> <code>moraine lake niagara falls algonquin chateau frontenac</code></li>
              <li><strong>Box 4:</strong> <code>canadian autumn road trip gifts seniors teens beginners</code></li>
              <li><strong>Box 5:</strong> <code>large print clean lines architectural landmarks mindfulness</code></li>
              <li><strong>Box 6:</strong> <code>single sided bleed shield coloring pages alcohol markers</code></li>
              <li><strong>Box 7:</strong> <code>provinces territories rocky mountains atlantic ocean views</code></li>"""

content = content.replace(old_keywords, new_keywords)

# Replace Etsy tags
old_tags = """            <div class="tags-cloud">
              <span class="pill">capybara coloring</span>
              <span class="pill">bold and easy book</span>
              <span class="pill">cozy coloring pages</span>
              <span class="pill">printable coloring</span>
              <span class="pill">procreate coloring</span>
              <span class="pill">stress relief art</span>
              <span class="pill">cute animal coloring</span>
              <span class="pill">mindful coloring pdf</span>
              <span class="pill">simple line art</span>
              <span class="pill">kawaii capybara gift</span>
              <span class="pill">digital coloring book</span>
              <span class="pill">ipad coloring pages</span>
              <span class="pill">calming activities</span>
            </div>"""

new_tags = """            <div class="tags-cloud">
              <span class="pill">canada coloring book</span>
              <span class="pill">scenic landscape pdf</span>
              <span class="pill">autumn foliage art</span>
              <span class="pill">printable adult book</span>
              <span class="pill">procreate travel art</span>
              <span class="pill">national park gift</span>
              <span class="pill">canada road trip</span>
              <span class="pill">mindful landscape</span>
              <span class="pill">fall leaves coloring</span>
              <span class="pill">large print nature</span>
              <span class="pill">moraine lake print</span>
              <span class="pill">niagara falls art</span>
              <span class="pill">stress relief coloring</span>
            </div>"""

content = content.replace(old_tags, new_tags)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] index.html updated with static SSR Canada content and 30 cards!")
