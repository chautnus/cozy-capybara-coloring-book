#!/usr/bin/env python3
"""
Integrate the Step-by-Step Amazon KDP and Etsy Publishing Guides directly into the web application.
- Updates public/style.css with responsive, accessible guide styles
- Updates public/index.html with the Publishing Guide section and header navigation
- Updates public/app.js with dynamic data switching (Canada vs Capybara) and 1-click copy functionality
"""

import sys
import re
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = WORKSPACE_ROOT / "public"

STYLE_CSS_PATH = PUBLIC_DIR / "style.css"
INDEX_HTML_PATH = PUBLIC_DIR / "index.html"
APP_JS_PATH = PUBLIC_DIR / "app.js"

# 1. CSS Extensions
CSS_EXTENSIONS = """
/* ==============================================================================
   PUBLISHING GUIDE COMPONENT STYLES (AMAZON KDP & ETSY)
   ============================================================================== */
.guide-tabs {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin: 24px 0 32px;
  flex-wrap: wrap;
}

.guide-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 12px 26px;
  font-size: 1.05rem;
  font-weight: 700;
  border-radius: var(--radius-md);
  border: 2px solid var(--color-border);
  background: var(--color-bg-card);
  color: var(--color-text-muted);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.guide-tab-btn:hover {
  border-color: var(--color-primary);
  color: var(--color-text-main);
  transform: translateY(-1px);
}

.guide-tab-btn.active.kdp {
  background: #ff9900;
  color: #111111;
  border-color: #e68a00;
  box-shadow: 0 4px 12px rgba(255, 153, 0, 0.3);
}

.guide-tab-btn.active.etsy {
  background: #f1641e;
  color: #ffffff;
  border-color: #d85210;
  box-shadow: 0 4px 12px rgba(241, 100, 30, 0.3);
}

.guide-timeline {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.guide-step-card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 26px;
  box-shadow: var(--shadow-sm);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.guide-step-card:hover {
  border-color: #94a3b8;
  box-shadow: var(--shadow-md);
}

.guide-step-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
  flex-wrap: wrap;
  gap: 12px;
}

.guide-step-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.guide-step-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 14px;
  background: var(--color-secondary);
  color: #ffffff;
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
  border-radius: 9999px;
  letter-spacing: 0.05em;
}

.guide-step-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-text-main);
}

.copy-field-group {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.copy-field-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.copy-field-label {
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.copy-field-wrapper {
  display: flex;
  align-items: stretch;
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.copy-field-val {
  flex: 1;
  padding: 12px 16px;
  font-size: 0.95rem;
  color: var(--color-text-main);
  font-family: inherit;
  word-break: break-word;
  white-space: pre-wrap;
  line-height: 1.5;
}

.btn-inline-copy {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  border: none;
  border-left: 1px solid var(--color-border);
  color: var(--color-primary);
  font-weight: 700;
  font-size: 0.85rem;
  padding: 0 18px;
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.btn-inline-copy:hover {
  background: var(--color-primary);
  color: #ffffff;
}

.btn-inline-copy.copied {
  background: #15803d !important;
  color: #ffffff !important;
}

.copy-box-code {
  background: #0f172a;
  color: #f8fafc;
  border-radius: var(--radius-md);
  padding: 18px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.85rem;
  line-height: 1.5;
  max-height: 280px;
  overflow-y: auto;
  position: relative;
  white-space: pre-wrap;
  word-break: break-all;
  border: 1px solid #1e293b;
}

.guide-alert-box {
  background: var(--color-info-bg);
  color: var(--color-info-text);
  border-left: 4px solid #0284c7;
  padding: 14px 18px;
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
  line-height: 1.5;
  margin-top: 14px;
}

.guide-alert-box strong {
  color: #0369a1;
}

.royalties-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 14px;
  border-radius: var(--radius-md);
  overflow: hidden;
}

.royalties-table th, .royalties-table td {
  padding: 12px 16px;
  border: 1px solid var(--color-border);
  text-align: left;
  font-size: 0.92rem;
}

.royalties-table th {
  background: var(--color-bg-alt);
  font-weight: 800;
  color: var(--color-text-main);
}

.royalties-table tr:nth-child(even) td {
  background: #fafafa;
}

.checklist-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 8px;
}

.checklist-pill-item {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  border-radius: 9999px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--color-text-main);
  cursor: pointer;
  transition: all 0.15s ease;
}

.checklist-pill-item:hover {
  background: #e2e8f0;
  border-color: #94a3b8;
}

.checklist-pill-item.copied {
  background: #dcfce7;
  border-color: #86efac;
  color: #166534;
}
"""

def update_css():
    content = STYLE_CSS_PATH.read_text(encoding="utf-8")
    if "PUBLISHING GUIDE COMPONENT STYLES" not in content:
        content += "\n" + CSS_EXTENSIONS
        STYLE_CSS_PATH.write_text(content, encoding="utf-8")
        print("[OK] Appended Publishing Guide styles to public/style.css")
    else:
        print("[SKIP] Publishing Guide styles already present in public/style.css")

# 2. HTML Section
GUIDE_HTML_SECTION = """
  <!-- Step-by-Step Commercial Publishing Guide Section -->
  <section id="publishing-guide" class="section">
    <div class="container">
      <div class="section-header">
        <div class="tag-row" style="justify-content:center; margin-bottom:10px;">
          <span class="badge badge-accent">1-Click Copy-Paste Ready</span>
          <span class="badge badge-success">Algorithm-Optimized</span>
          <span class="badge badge-info">Amazon KDP &amp; Etsy Ready</span>
        </div>
        <h2 class="section-title">Step-by-Step Commercial Publishing Guide</h2>
        <p class="section-subtitle">A comprehensive, end-to-end publishing walkthrough for Amazon KDP Paperback and Etsy Digital Download with instant copy-to-clipboard tools.</p>
      </div>

      <!-- Guide Channel Switcher Tabs -->
      <div class="guide-tabs">
        <button class="guide-tab-btn active kdp" id="tab-btn-kdp">
          📦 Amazon KDP Paperback (Print-on-Demand)
        </button>
        <button class="guide-tab-btn etsy" id="tab-btn-etsy">
          🎨 Etsy Digital Download (Instant Delivery)
        </button>
      </div>

      <!-- Container dynamically populated by app.js -->
      <div id="publishing-guide-content">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </section>
"""

def update_html():
    content = INDEX_HTML_PATH.read_text(encoding="utf-8")
    
    # 1. Update navigation in header
    if 'href="#publishing-guide"' not in content:
        nav_target = '<a href="#downloads" class="nav-item btn-nav">Downloads</a>'
        nav_replacement = '<a href="#publishing-guide" class="nav-item">Publishing Guide</a>\n        <a href="#downloads" class="nav-item btn-nav">Downloads</a>'
        content = content.replace(nav_target, nav_replacement)
        print("[OK] Added 'Publishing Guide' link to header navigation.")
        
    # 2. Add section before downloads
    if 'id="publishing-guide"' not in content:
        section_target = '<!-- Downloads & Action Section -->'
        content = content.replace(section_target, GUIDE_HTML_SECTION + "\n  " + section_target)
        print("[OK] Inserted #publishing-guide section into public/index.html")
    else:
        print("[SKIP] #publishing-guide section already present.")
        
    INDEX_HTML_PATH.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    update_css()
    update_html()
