import urllib.request

url = "https://cozy-capybara-coloring-book.vercel.app"
try:
    with urllib.request.urlopen(url) as res:
        content = res.read().decode("utf-8")
        print(f"URL: {url}")
        print(f"HTTP Status: {res.status}")
        print(f"Contains '#publishing-guide': {'id=\"publishing-guide\"' in content}")
        print(f"Contains nav link '#publishing-guide': {'href=\"#publishing-guide\"' in content}")
        print(f"Contains tab-btn-kdp: {'id=\"tab-btn-kdp\"' in content}")
        print(f"Contains tab-btn-etsy: {'id=\"tab-btn-etsy\"' in content}")
except Exception as e:
    print(f"Error checking {url}: {e}")

js_url = "https://cozy-capybara-coloring-book.vercel.app/app.js"
try:
    with urllib.request.urlopen(js_url) as res:
        js_content = res.read().decode("utf-8")
        print(f"JS URL: {js_url}")
        print(f"JS HTTP Status: {res.status}")
        print(f"JS Contains 'PUBLISHING_GUIDES': {'const PUBLISHING_GUIDES' in js_content}")
        print(f"JS Contains 'renderPublishingGuide': {'function renderPublishingGuide' in js_content}")
        print(f"JS Length: {len(js_content)} chars")
except Exception as e:
    print(f"Error checking {js_url}: {e}")
