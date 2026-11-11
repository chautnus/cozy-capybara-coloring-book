// Multi-Book Commercial Coloring Pipeline - Autumn in Canada & Barnaby's Peaceful Days

const CAPYBARA_PAGES = [
  { page: 1, filter: "1", title: "Morning Sun & Herbal Tea", caption: "A quiet morning begins with a warm cup of herbal tea.", src: "assets/processed/page_01_clean.png" },
  { page: 2, filter: "1", title: "Watering Greenhouse Succulents", caption: "Growing happiness, one tiny leaf at a time.", src: "assets/processed/page_02_clean.png" },
  { page: 3, filter: "1", title: "The Village Artisan Bakery", caption: "The sweetest aroma in the whole village.", src: "assets/processed/page_03_clean.png" },
  { page: 4, filter: "1", title: "Market Stroll with Straw Basket", caption: "Simple treats from a sunny morning stroll.", src: "assets/processed/page_04_clean.png" },
  { page: 5, filter: "1", title: "Bicycle with a Flower Basket", caption: "Pedaling slowly down peaceful country roads.", src: "assets/processed/page_05_clean.png" },
  { page: 6, filter: "1", title: "Breakfast by the Garden Table", caption: "Sweet pancakes taste better under the open sky.", src: "assets/processed/page_06_clean.png" },
  { page: 7, filter: "1", title: "Greeting the Garden Snail", caption: "There is no rush to get anywhere today.", src: "assets/processed/page_07_clean.png" },
  { page: 8, filter: "1", title: "Reading in the Window Nook", caption: "Lost in cozy adventures between the pages.", src: "assets/processed/page_08_clean.png" },
  { page: 9, filter: "2", title: "The Cozy Antiquarian Bookstore", caption: "Keeper of stories and dusty forgotten wonders.", src: "assets/processed/page_09_clean.png" },
  { page: 10, filter: "2", title: "Afternoon Tea with Baby Ducklings", caption: "The finest company is always warm and gentle.", src: "assets/processed/page_10_clean.png" },
  { page: 11, filter: "2", title: "Pottery Studio Workshop", caption: "Shaping calm thoughts with loving hands.", src: "assets/processed/page_11_clean.png" },
  { page: 12, filter: "2", title: "Flower Arranging in Glass Jars", caption: "Bringing a splash of wild nature indoors.", src: "assets/processed/page_12_clean.png" },
  { page: 13, filter: "2", title: "Painting Watercolors in the Meadow", caption: "Painting colors that whisper tranquility.", src: "assets/processed/page_13_clean.png" },
  { page: 14, filter: "2", title: "Coffee Break with Hedgehog Friend", caption: "Warm conversations on a breezy afternoon.", src: "assets/processed/page_14_clean.png" },
  { page: 15, filter: "2", title: "Sewing a Patchwork Quilt", caption: "Stitching warmth into every corner.", src: "assets/processed/page_15_clean.png" },
  { page: 16, filter: "2", title: "Arranging the Spice Jars", caption: "Every scent tells a story of cozy comfort.", src: "assets/processed/page_16_clean.png" },
  { page: 17, filter: "3", title: "Floating Leaf Boat on Lily Pond", caption: "Floating gently wherever the calm waters lead.", src: "assets/processed/page_17_clean.png" },
  { page: 18, filter: "3", title: "The Relaxing Onsen Springs", caption: "Total peace is doing absolutely nothing at all.", src: "assets/processed/page_18_clean.png" },
  { page: 19, filter: "3", title: "Mushroom Foraging in Pine Forest", caption: "Treasures waiting beneath the soft forest moss.", src: "assets/processed/page_19_clean.png" },
  { page: 20, filter: "3", title: "Hammock Nap Between Apple Trees", caption: "Afternoon naps are sweet gifts to the soul.", src: "assets/processed/page_20_clean.png" },
  { page: 21, filter: "3", title: "Bird Watching with Binoculars", caption: "Listening closely to the songs of the breeze.", src: "assets/processed/page_21_clean.png" },
  { page: 22, filter: "3", title: "Rainy Day at Covered Porch", caption: "The soothing rhythm of gentle raindrops.", src: "assets/processed/page_22_clean.png" },
  { page: 23, filter: "3", title: "Fly-Fishing in Whispering Stream", caption: "Patience is the sweetest kind of quiet.", src: "assets/processed/page_23_clean.png" },
  { page: 24, filter: "3", title: "Picnic Under Great Willow Tree", caption: "Basking in the gentle shade of gratitude.", src: "assets/processed/page_24_clean.png" },
  { page: 25, filter: "4", title: "Baking Fresh Apple Cinnamon Pie", caption: "The kitchen is full of warmth, sugar, and spice.", src: "assets/processed/page_25_clean.png" },
  { page: 26, filter: "4", title: "Fireplace Warmth & Hot Cocoa", caption: "Cozy embers chase the evening chill away.", src: "assets/processed/page_26_clean.png" },
  { page: 27, filter: "4", title: "Stargazing with Brass Telescope", caption: "Wishing on a sky full of quiet dreams.", src: "assets/processed/page_27_clean.png" },
  { page: 28, filter: "4", title: "Playing Acoustic Lullabies", caption: "Soft melodies singing the day to rest.", src: "assets/processed/page_28_clean.png" },
  { page: 29, filter: "4", title: "Brushing Teeth in Vintage Bathroom", caption: "Ready for dreamland after a lovely day.", src: "assets/processed/page_29_clean.png" },
  { page: 30, filter: "4", title: "Sleepy Night in Cloud Bed", caption: "Rest peacefully, gentle friend. Tomorrow brings joy.", src: "assets/processed/page_30_clean.png" }
];

const CANADA_PAGES = [
  {
    "page": 1,
    "filter": "central",
    "title": "Algonquin Provincial Park",
    "province": "Ontario",
    "caption": "Algonquin Provincial Park in autumn. In the foreground, an elegant traditional Canadian cedar canoe rests on the quiet l...",
    "src": "assets/canada/processed/page_01_clean.png",
    "density": "11.78%",
    "is_redesigned": true
  },
  {
    "page": 2,
    "filter": "central",
    "title": "Agawa Canyon Scenic Railway",
    "province": "Northern Ontario",
    "caption": "Agawa Canyon in Northern Ontario. A vintage passenger scenic train curves along railway tracks on the canyon floor besid...",
    "src": "assets/canada/processed/page_02_clean.png",
    "density": "15.40%",
    "is_redesigned": true
  },
  {
    "page": 3,
    "filter": "central",
    "title": "Niagara Horseshoe Falls",
    "province": "Ontario",
    "caption": "Grand panoramic view of Niagara Horseshoe Falls framed by autumn foliage. The roaring curved waterfall has powerful casc...",
    "src": "assets/canada/processed/page_03_clean.png",
    "density": "15.15%",
    "is_redesigned": true
  },
  {
    "page": 4,
    "filter": "central",
    "title": "Rideau Canal & Market",
    "province": "Ottawa, Ontario",
    "caption": "Scenic historic view along the Rideau Canal in Ottawa in autumn. A pleasure tour boat glides through calm water strata. ...",
    "src": "assets/canada/processed/page_04_clean.png",
    "density": "14.40%",
    "is_redesigned": true
  },
  {
    "page": 5,
    "filter": "central",
    "title": "Ch\u00e2teau Frontenac & Old Quebec",
    "province": "Quebec",
    "caption": "The iconic Ch\u00e2teau Frontenac castle rising majestically above Old Quebec in peak autumn. The historic castle features ch...",
    "src": "assets/canada/processed/page_05_clean.png",
    "density": "13.13%",
    "is_redesigned": true
  },
  {
    "page": 6,
    "filter": "central",
    "title": "Mont-Tremblant Alpine Village",
    "province": "Quebec",
    "caption": "Storybook pedestrian alpine resort village of Mont-Tremblant in autumn. A cobblestone village square with a vintage cloc...",
    "src": "assets/canada/processed/page_06_clean.png",
    "density": "13.97%",
    "is_redesigned": true
  },
  {
    "page": 7,
    "filter": "central",
    "title": "Montmorency Falls & Bridge",
    "province": "Quebec",
    "caption": "Dramatic plunge of Montmorency Falls in Quebec, higher than Niagara. A pedestrian suspension bridge spans the roaring wa...",
    "src": "assets/canada/processed/page_07_clean.png",
    "density": "12.26%",
    "is_redesigned": true
  },
  {
    "page": 8,
    "filter": "central",
    "title": "Jacques-Cartier Glacial Valley",
    "province": "Quebec",
    "caption": "Monumental U-shaped glacial valley of Jacques-Cartier National Park. A winding river snakes through the center with flow...",
    "src": "assets/canada/processed/page_08_clean.png",
    "density": "12.38%",
    "is_redesigned": true
  },
  {
    "page": 9,
    "filter": "west",
    "title": "Moraine Lake & Ten Peaks",
    "province": "Banff, Alberta",
    "caption": "Iconic view of Moraine Lake from the natural Rockpile in Banff National Park. Jagged snow-dusted summits of the Ten Peak...",
    "src": "assets/canada/processed/page_09_clean.png",
    "density": "13.97%",
    "is_redesigned": true
  },
  {
    "page": 10,
    "filter": "west",
    "title": "Icefields Parkway Wildlife",
    "province": "Alberta",
    "caption": "Scenic wildlife landscape along the Icefields Parkway in autumn. In the foreground, a magnificent bull elk with sweeping...",
    "src": "assets/canada/processed/page_10_clean.png",
    "density": "13.90%",
    "is_redesigned": true
  },
  {
    "page": 11,
    "filter": "west",
    "title": "Dinosaur Badlands Hoodoos",
    "province": "Alberta",
    "caption": "Bizarre mushroom-shaped sandstone Hoodoos in Dinosaur Provincial Park. The giant hoodoo rock pillars feature bold strati...",
    "src": "assets/canada/processed/page_11_clean.png",
    "density": "13.91%",
    "is_redesigned": true
  },
  {
    "page": 12,
    "filter": "west",
    "title": "Banff Upper Hot Springs",
    "province": "Banff, Alberta",
    "caption": "Steaming open-air mineral hot pool at Banff Upper Hot Springs. Stylized gentle steam ribbons drift into the cool autumn ...",
    "src": "assets/canada/processed/page_12_clean.png",
    "density": "13.89%",
    "is_redesigned": true
  },
  {
    "page": 13,
    "filter": "west",
    "title": "Okanagan Valley Vineyards",
    "province": "British Columbia",
    "caption": "Terraced hillside vineyards of the Okanagan Valley in autumn harvest. Contoured geometric rows of grapevines curve grace...",
    "src": "assets/canada/processed/page_13_clean.png",
    "density": "13.26%",
    "is_redesigned": true
  },
  {
    "page": 14,
    "filter": "west",
    "title": "Lynn Canyon Suspension Bridge",
    "province": "North Vancouver, BC",
    "caption": "Wooden pedestrian suspension footbridge swaying high above Lynn Canyon gorge in North Vancouver. Rushing canyon river wi...",
    "src": "assets/canada/processed/page_14_clean.png",
    "density": "32.92%",
    "is_redesigned": false
  },
  {
    "page": 15,
    "filter": "west",
    "title": "Tofino Pacific Coast",
    "province": "Vancouver Island, BC",
    "caption": "Wild coastal landscape of Tofino on Vancouver Island. In the foreground, massive smooth cedar driftwood logs rest on the...",
    "src": "assets/canada/processed/page_15_clean.png",
    "density": "31.51%",
    "is_redesigned": false
  },
  {
    "page": 16,
    "filter": "west",
    "title": "Natural Bridge & Emerald Lake",
    "province": "Yoho National Park, BC",
    "caption": "Ancient limestone natural rock bridge carved by raging glacier waters in Yoho National Park. The sculptural rock arch fe...",
    "src": "assets/canada/processed/page_16_clean.png",
    "density": "23.19%",
    "is_redesigned": false
  },
  {
    "page": 17,
    "filter": "atlantic",
    "title": "The Cabot Trail Ocean Bluffs",
    "province": "Cape Breton, Nova Scotia",
    "caption": "Spectacular sweeping coastal highway of the Cabot Trail winding along steep headland cliffs of Cape Breton Highlands. Be...",
    "src": "assets/canada/processed/page_17_clean.png",
    "density": "32.45%",
    "is_redesigned": false
  },
  {
    "page": 18,
    "filter": "atlantic",
    "title": "Peggy's Cove Lighthouse",
    "province": "Nova Scotia",
    "caption": "Classic Peggy's Cove octagonal wooden lighthouse standing proudly on giant smooth glacial granite boulders with rounded ...",
    "src": "assets/canada/processed/page_18_clean.png",
    "density": "28.19%",
    "is_redesigned": false
  },
  {
    "page": 19,
    "filter": "atlantic",
    "title": "Hopewell Rocks Flowerpots",
    "province": "Bay of Fundy, NB",
    "caption": "Monumental flowerpot sandstone sea stacks at Hopewell Rocks on the Bay of Fundy. At low tide, the massive curved rock pi...",
    "src": "assets/canada/processed/page_19_clean.png",
    "density": "24.36%",
    "is_redesigned": false
  },
  {
    "page": 20,
    "filter": "atlantic",
    "title": "Dickson Falls Forest Brook",
    "province": "Fundy National Park, NB",
    "caption": "Lush secluded forest cascade of Dickson Falls in Fundy National Park. A stepped brook tumbles down smooth mossy boulders...",
    "src": "assets/canada/processed/page_20_clean.png",
    "density": "14.53%",
    "is_redesigned": true
  },
  {
    "page": 21,
    "filter": "atlantic",
    "title": "Cavendish Red Sandstone Cliffs",
    "province": "Prince Edward Island",
    "caption": "Vivid coastal landscape of Cavendish Beach on Prince Edward Island. In the midground, dramatic red sandstone sea cliffs ...",
    "src": "assets/canada/processed/page_21_clean.png",
    "density": "14.02%",
    "is_redesigned": true
  },
  {
    "page": 22,
    "filter": "atlantic",
    "title": "Point Prim Historic Lighthouse",
    "province": "Prince Edward Island",
    "caption": "Historic Point Prim Lighthouse, the oldest lighthouse on Prince Edward Island built in 1845. A unique circular brick tow...",
    "src": "assets/canada/processed/page_22_clean.png",
    "density": "13.92%",
    "is_redesigned": true
  },
  {
    "page": 23,
    "filter": "atlantic",
    "title": "Western Brook Pond Fjord",
    "province": "Gros Morne, Newfoundland",
    "caption": "Towering vertical granite cliffs of Western Brook Pond glacier gorge in Gros Morne National Park. A scenic tour boat gli...",
    "src": "assets/canada/processed/page_23_clean.png",
    "density": "14.05%",
    "is_redesigned": true
  },
  {
    "page": 24,
    "filter": "atlantic",
    "title": "Quidi Vidi Fishing Village",
    "province": "St. John's, Newfoundland",
    "caption": "Picturesque historic fishing outport of Quidi Vidi near St. John's. Traditional wooden fishing stages and sheds on stilt...",
    "src": "assets/canada/processed/page_24_clean.png",
    "density": "13.93%",
    "is_redesigned": true
  },
  {
    "page": 25,
    "filter": "atlantic",
    "title": "Cape Spear Easternmost Point",
    "province": "Newfoundland",
    "caption": "Historic 1836 Cape Spear Lighthouse standing on a dramatic windswept promontory at the easternmost point of North Americ...",
    "src": "assets/canada/processed/page_25_clean.png",
    "density": "26.30%",
    "is_redesigned": false
  },
  {
    "page": 26,
    "filter": "prairie_north",
    "title": "Riding Mountain Ominik Marsh",
    "province": "Manitoba",
    "caption": "Floating wooden boardwalk trail winding gracefully in an S-curve through Ominik Marsh in Riding Mountain National Park. ...",
    "src": "assets/canada/processed/page_26_clean.png",
    "density": "14.08%",
    "is_redesigned": true
  },
  {
    "page": 27,
    "filter": "prairie_north",
    "title": "Churchill Polar Bears & Aurora",
    "province": "Northern Manitoba",
    "caption": "Wild autumn subarctic landscape in Churchill, Manitoba. A magnificent polar bear mother and her playful cub walk across ...",
    "src": "assets/canada/processed/page_27_clean.png",
    "density": "38.08%",
    "is_redesigned": false
  },
  {
    "page": 28,
    "filter": "prairie_north",
    "title": "Prairie Grain Elevators",
    "province": "Saskatchewan",
    "caption": "Classic rural Canadian prairie icon in Saskatchewan. A row of towering historic wooden grain elevators with chiseled geo...",
    "src": "assets/canada/processed/page_28_clean.png",
    "density": "33.27%",
    "is_redesigned": false
  },
  {
    "page": 29,
    "filter": "prairie_north",
    "title": "Tombstone Mountain & Tundra",
    "province": "Yukon Territory",
    "caption": "Dramatic subarctic wilderness of Tombstone Territorial Park along the Dempster Highway. In the foreground, low-lying cri...",
    "src": "assets/canada/processed/page_29_clean.png",
    "density": "38.53%",
    "is_redesigned": false
  },
  {
    "page": 30,
    "filter": "prairie_north",
    "title": "Alexandra Falls Gorge",
    "province": "Northwest Territories",
    "caption": "Powerful Alexandra Falls in the Northwest Territories. A wide, thunderous curtain of water drops in tiered cascading ban...",
    "src": "assets/canada/processed/page_30_clean.png",
    "density": "33.02%",
    "is_redesigned": false
  }
];

let activeBook = "canada"; // Default to newest release

const BOOK_CONFIGS = {
  canada: {
    brandBadge: "BOOK 2 • SCENIC LANDSCAPES & NATURE",
    brandTitle: "Autumn in Canada",
    badges: [
      '<span class="badge badge-accent">10 Provinces & 3 Territories</span>',
      '<span class="badge badge-success">8.5 &times; 8.5" Square Bleed</span>',
      '<span class="badge badge-info">100% Freedom of Panorama</span>'
    ],
    heading: "Autumn in Canada: A Scenic Journey Across Provinces & Territories",
    desc: "An architectural-grade coloring adventure capturing 30 iconic natural and historic landmarks across Canada. Masterfully formatted for <strong>Amazon KDP Paperback (64 pages)</strong> and <strong>Etsy Digital Download</strong> with single-sided print bleed shields.",
    stats: { scenes: "30", pages: "64", dpi: "300", price: "$7.99" },
    sectionSubtitle: "30 celebrated national landmarks across 6 geographic regions.",
    tabs: [
      { id: "all", label: "All 30 Scenes" },
      { id: "central", label: "Central (ON & QC)" },
      { id: "west", label: "Western & Pacific (AB & BC)" },
      { id: "atlantic", label: "Atlantic Canada (NS, NB, PEI, NL)" },
      { id: "prairie_north", label: "Prairies & North (MB, SK, YT, NWT)" }
    ],
    kdpTitle: "dist/canada_interior_8.5x8.5.pdf",
    kdpCover: "dist/canada_full_cover_spread.pdf",
    etsyZip: "dist/Autumn_in_Canada_Etsy_Digital_Bundle.zip",
    keywords: [
      "canada travel coloring book scenic landscapes fall foliage",
      "national parks adult relaxation stress relief nature lovers",
      "moraine lake niagara falls algonquin chateau frontenac",
      "canadian autumn road trip gifts seniors teens beginners",
      "large print clean lines architectural landmarks mindfulness",
      "single sided bleed shield coloring pages alcohol markers",
      "provinces territories rocky mountains atlantic ocean views"
    ],
    tags: [
      "canada coloring book", "scenic landscape pdf", "autumn foliage art",
      "printable adult book", "procreate travel art", "national park gift",
      "canada road trip", "mindful landscape", "fall leaves coloring",
      "large print nature", "moraine lake print", "niagara falls art",
      "stress relief coloring"
    ]
  },
  capybara: {
    brandBadge: "BOOK 1 • COZY CAPYBARA STORY",
    brandTitle: "Barnaby's Peaceful Days",
    badges: [
      '<span class="badge badge-accent">Trending BookTok Niche</span>',
      '<span class="badge badge-success">8.5 &times; 8.5" Square Trim</span>',
      '<span class="badge badge-info">Single-Sided Bleed Shield</span>'
    ],
    heading: "A Bold &amp; Easy Cozy Capybara Coloring Book",
    desc: "An end-to-end commercial coloring book production pipeline designed for stress relief, relaxation, and effortless publishing on <strong>Amazon KDP Paperback</strong> and <strong>Etsy Digital Download</strong>.",
    stats: { scenes: "30", pages: "64", dpi: "300", price: "$6.99" },
    sectionSubtitle: "24 peaceful hours in the life of Barnaby the Capybara across 4 distinct chapters.",
    tabs: [
      { id: "all", label: "All 30 Pages" },
      { id: "1", label: "Part 1: Morning Calm (1-8)" },
      { id: "2", label: "Part 2: Work & Friendship (9-16)" },
      { id: "3", label: "Part 3: Gentle Nature (17-24)" },
      { id: "4", label: "Part 4: Cozy Night (25-30)" }
    ],
    kdpTitle: "dist/kdp_interior_8.5x8.5.pdf",
    kdpCover: "dist/kdp_full_cover_spread.pdf",
    etsyZip: "dist/Barnaby_Cozy_Capybara_Etsy_Bundle.zip",
    keywords: [
      "cute simple relaxing aesthetic hygge cottagecore",
      "stress relief relaxation adults teens seniors beginners",
      "mindful mindfulness calming anxiety therapy gift",
      "quirky animals doing human things funny kawaii daily",
      "thick lines large print easy cozy spaces cafe rooms",
      "mindful coloring pages quick daily chill self care",
      "alcohol marker friendly single sided pages animal lover"
    ],
    tags: [
      "capybara coloring", "bold and easy book", "cozy coloring pages",
      "printable coloring", "procreate coloring", "stress relief art",
      "cute animal coloring", "mindful coloring pdf", "simple line art",
      "kawaii capybara gift", "digital coloring book", "ipad coloring pages",
      "relaxation gift idea"
    ]
  }
};

function switchBook(bookId) {
  if (!BOOK_CONFIGS[bookId]) return;
  activeBook = bookId;

  // Update switcher button states
  document.querySelectorAll(".book-tab-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.book === bookId);
  });

  const cfg = BOOK_CONFIGS[bookId];

  // Update Brand
  const brandTitle = document.querySelector(".brand-title");
  const brandBadge = document.querySelector(".brand-badge");
  if (brandTitle) brandTitle.textContent = cfg.brandTitle;
  if (brandBadge) brandBadge.textContent = cfg.brandBadge;

  // Update Hero
  const heroHeading = document.querySelector(".hero-heading");
  const heroDesc = document.querySelector(".hero-desc");
  const tagRow = document.querySelector(".tag-row");
  if (heroHeading) heroHeading.innerHTML = cfg.heading;
  if (heroDesc) heroDesc.innerHTML = cfg.desc;
  if (tagRow) tagRow.innerHTML = cfg.badges.join("");

  // Update Stats
  const statNums = document.querySelectorAll(".stat-number");
  if (statNums.length >= 4) {
    statNums[0].textContent = cfg.stats.scenes;
    statNums[1].textContent = cfg.stats.pages;
    statNums[2].textContent = cfg.stats.dpi;
    statNums[3].textContent = cfg.stats.price;
  }

  // Update Gallery Subtitle
  const sub = document.querySelector(".section-subtitle");
  if (sub) sub.textContent = cfg.sectionSubtitle;

  // Render Tabs
  const tabContainer = document.querySelector(".tab-controls");
  if (tabContainer) {
    tabContainer.innerHTML = cfg.tabs.map((t, idx) => `
      <button class="tab-btn ${idx === 0 ? 'active' : ''}" data-filter="${t.id}">${t.label}</button>
    `).join("");

    tabContainer.querySelectorAll(".tab-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        tabContainer.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        renderActiveBookPages(btn.dataset.filter);
      });
    });
  }

  // Update Downloads
  const kdpBtn = document.querySelector('a[href*="interior"]');
  const coverBtn = document.querySelector('a[href*="cover"]');
  const etsyBtn = document.querySelector('a[href*="Bundle"]');
  if (kdpBtn) kdpBtn.setAttribute("href", cfg.kdpTitle);
  if (coverBtn) coverBtn.setAttribute("href", cfg.kdpCover);
  if (etsyBtn) etsyBtn.setAttribute("href", cfg.etsyZip);

  // Update SEO Keywords
  const kwList = document.querySelector(".keyword-list");
  if (kwList) {
    kwList.innerHTML = cfg.keywords.map((kw, i) => `
      <li><strong>Box ${i + 1}:</strong> <code>${kw}</code></li>
    `).join("");
  }

  // Update Etsy Tags
  const tagCloud = document.querySelector(".tags-cloud");
  if (tagCloud) {
    tagCloud.innerHTML = cfg.tags.map(t => `<span class="pill">${t}</span>`).join("");
  }

  // Render Gallery
  renderActiveBookPages("all");
  renderPublishingGuide(currentGuideChannel);
}

function renderActiveBookPages(filterId = "all") {
  const container = document.getElementById("pages-grid");
  if (!container) return;

  const dataset = activeBook === "canada" ? CANADA_PAGES : CAPYBARA_PAGES;
  const filtered = filterId === "all"
    ? dataset
    : dataset.filter(item => item.filter === filterId);

  container.innerHTML = filtered.map(item => {
    const provinceBadge = item.province
      ? `<span class="badge-province">${item.province}</span>`
      : "";
    const statusBadge = item.is_redesigned !== undefined
      ? (item.is_redesigned
          ? `<span class="badge-status-ok" style="background:#2e7d32;color:#fff;padding:3px 8px;border-radius:12px;font-size:11px;font-weight:600;margin-left:auto;">ĐÃ REDESIGN • ${item.density} NÉT</span>`
          : `<span class="badge-status-wait" style="background:#e65100;color:#fff;padding:3px 8px;border-radius:12px;font-size:11px;font-weight:600;margin-left:auto;">CHỜ QUOTA (~40m)</span>`)
      : "";
    const imgSrc = `${item.src}?v=3`;
    return `
    <article class="page-card" data-page="${item.page}">
      <div class="page-card-header">
        <span class="page-num">Page ${String(item.page).padStart(2, '0')}</span>
        ${provinceBadge}
        ${statusBadge}
      </div>
      <div class="page-preview-frame">
        <img src="${imgSrc}" alt="${item.title}" class="page-preview-img" loading="lazy" />
      </div>
      <h3 class="page-title">${item.title}</h3>
      <p class="page-caption">"${item.caption}"</p>
      <div class="prompt-copy-btns">
        <a href="${item.src}" download="page_${String(item.page).padStart(2, '0')}.png" class="btn-copy" style="text-align:center;text-decoration:none;">Download PNG</a>
      </div>
    </article>
  `;
  }).join("");
}

document.addEventListener("DOMContentLoaded", () => {
  // Set up Book Switcher Bar clicks
  document.querySelectorAll(".book-tab-btn").forEach(btn => {
    btn.addEventListener("click", () => switchBook(btn.dataset.book));
  });

  // Initialize with Canada Book
  // Hook up publishing guide channel switcher buttons
  const kdpBtn = document.getElementById("tab-btn-kdp");
  const etsyBtn = document.getElementById("tab-btn-etsy");
  if (kdpBtn) kdpBtn.addEventListener("click", () => renderPublishingGuide("kdp"));
  if (etsyBtn) etsyBtn.addEventListener("click", () => renderPublishingGuide("etsy"));

  switchBook("canada");
});



// ==============================================================================
// PUBLISHING GUIDES DATA & RENDERING (AMAZON KDP & ETSY)
// ==============================================================================
const PUBLISHING_GUIDES = {
  canada: {
    kdp: {
      channelTitle: "Amazon KDP Paperback Publishing (Autumn in Canada)",
      badgeText: "KDP Print-on-Demand",
      steps: [
        {
          number: "Step 01",
          title: "Book Details & Author (Thông tin sách)",
          badge: "Metadata",
          fields: [
            { label: "Book Title (Tiêu đề chính)", value: "Autumn in Canada" },
            { label: "Subtitle (Phụ đề tối ưu SEO)", value: "A Scenic Coloring Journey Across Provinces & Territories: 30 Majestic Fall Foliage Landscapes for Adult Relaxation and Stress Relief" },
            { label: "Series Title", value: "Canadian Scenic Coloring Journeys (Book 2)" },
            { label: "Edition Number", value: "1" },
            { label: "Author / Primary Contributor", value: "Northland Heritage Press" }
          ]
        },
        {
          number: "Step 02",
          title: "HTML Book Description (Mô tả giàu định dạng KDP)",
          badge: "Rich HTML",
          isCode: true,
          label: "Mã HTML Description (Click nút Copy & dán thẳng vào ô Description trên KDP Dashboard)",
          value: `<h3>Experience the Majestic Splendor of Canadian Autumn from Coast to Coast!</h3>
<p>Immerse yourself in the breathtaking golden and crimson hues of Canada’s most celebrated landscapes. <b>Autumn in Canada: A Scenic Journey Across Provinces & Territories</b> takes colorists of all skill levels on an unforgettable 30-stop architectural and natural expedition across all 10 provinces and 3 northern territories.</p>

<p>Inspired by the rhythmic layering of traditional woodblock prints, each illustration features bold, decisive boundary linework paired with spacious contour tiers. Whether you are using alcohol markers (Ohuhu, Copic), colored pencils, or gel pens, these open, rhythmic spaces allow for effortless multi-layer blending, gentle color washing, and stunning gradients without the eye strain of cluttered micro-details.</p>

<h3>What Makes This Scenic Coloring Book Exceptional:</h3>
<ul>
  <li><b>30 Iconic Canadian Landmarks:</b> Explore Niagara Falls, Algonquin Park, Banff’s Moraine Lake, Château Frontenac, the rocky Atlantic bluffs of Peggy's Cove and Cabot Trail, the red cliffs of PEI, and the wild dancing Aurora of Churchill.</li>
  <li><b>Colorable Vintage Typography Badges:</b> Every illustration includes a classic National Park-style hollow title badge at the base, allowing you to color the landmark names.</li>
  <li><b>Single-Sided Printing with Bleed Shields:</b> Every artwork page is followed by a rich, dark protective backing page (#181818) to absorb marker ink bleed-through and protect subsequent designs.</li>
  <li><b>Color Swatches Test Palette Included:</b> Test your marker blending, color combinations, and shading tones directly on the included 28-block palette before touching your artwork.</li>
  <li><b>100% Freedom of Panorama & Trademark Safe:</b> Thoughtfully composed to honor authentic Canadian heritage under Section 32.2(1)(b) of the Canadian Copyright Act.</li>
  <li><b>Premium Square 8.5 x 8.5 Inch Format:</b> The ideal balance between generous artistic expanse and portable coloring comfort.</li>
</ul>

<p><b>Perfect gift for nature lovers, Canadian travelers, seniors, teens, and anyone seeking peaceful mindful stress relief.</b></p>
<p><i>Grab your favorite coloring tools and begin your autumn expedition today!</i></p>`
        },
        {
          number: "Step 03",
          title: "7 Search Keywords (Thuật toán tìm kiếm Amazon A9)",
          badge: "A9 Search",
          isKeywords: true,
          items: [
            "canada travel coloring book scenic landscapes fall foliage",
            "national parks adult relaxation stress relief nature lovers",
            "moraine lake niagara falls algonquin chateau frontenac",
            "canadian autumn road trip gifts seniors teens beginners",
            "large print clean lines architectural landmarks mindfulness",
            "single sided bleed shield coloring pages alcohol markers",
            "provinces territories rocky mountains atlantic ocean views"
          ]
        },
        {
          number: "Step 04",
          title: "Categories & Target Audience (Danh mục BISAC)",
          badge: "Classification",
          fields: [
            { label: "Primary Category (Chính)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Scenery & Landscapes" },
            { label: "Secondary Category (Phụ)", value: "Travel > Canada > General" },
            { label: "Tertiary Category (Bổ trợ)", value: "Self-Help > Stress Management" },
            { label: "Adult Content Confirmation", value: "No (Sách nội dung phù hợp cho mọi lứa tuổi)" }
          ]
        },
        {
          number: "Step 05",
          title: "Print Options & Interior Upload (Quy chuẩn in ấn)",
          badge: "Specs & Upload",
          fields: [
            { label: "Interior & Paper Type", value: "Black & white interior with white paper" },
            { label: "Trim Size", value: "8.5 x 8.5 in (21.59 x 21.59 cm)" },
            { label: "Bleed Settings", value: "Bleed (PDF already formatted with 0.125\" bleed: 8.625 x 8.750 in)" },
            { label: "Paperback Cover Finish", value: "Matte (Mịn không lóa — chuẩn tranh mộc bản nghệ thuật)" },
            { label: "Manuscript File (Ruột sách)", value: "dist/canada_interior_8.5x8.5.pdf (64 pages)" },
            { label: "Cover File (Bìa mở rộng)", value: "dist/canada_full_cover_spread.pdf (17.394 x 8.750 in)" }
          ],
          alert: "Lưu ý quan trọng: Khi tải file PDF ruột sách lên KDP, tại mục Bleed chọn <strong>Bleed (PDF only)</strong> để giữ đúng tỷ lệ 8.625 x 8.750 inch tràn lề không bị co kéo viền."
        },
        {
          number: "Step 06",
          title: "Pricing & Royalties (Định giá & Lợi nhuận)",
          badge: "Royalties",
          isRoyalties: true,
          table: [
            { marketplace: "Amazon.com (US)", price: "$7.99 USD", printCost: "$2.15", royalty: "$2.64 / book (~33%)" },
            { marketplace: "Amazon.ca (Canada)", price: "$10.99 CAD", printCost: "$3.12 CAD", royalty: "$3.47 CAD / book" },
            { marketplace: "Amazon.co.uk (UK)", price: "£6.99 GBP", printCost: "£1.85 GBP", royalty: "£2.34 GBP / book" },
            { marketplace: "Amazon.de/fr/es (EU)", price: "€7.99 EUR", printCost: "€2.24 EUR", royalty: "€2.55 EUR / book" }
          ]
        }
      ]
    },
    etsy: {
      channelTitle: "Etsy Digital Download Listing (Autumn in Canada)",
      badgeText: "Etsy Instant Download",
      steps: [
        {
          number: "Step 01",
          title: "Listing Title (Tiêu đề SEO 140 ký tự)",
          badge: "SEO Title",
          fields: [
            {
              label: "Listing Title (133 / 140 ký tự — Tối ưu hóa Etsy Search)",
              value: "Autumn in Canada Coloring Book PDF, 30 Scenic Landscapes Digital Download, Adult Relaxation, Procreate Transparent PNG, Fall Nature Art"
            }
          ]
        },
        {
          number: "Step 02",
          title: "13 Etsy Tags (Thẻ Tag chuẩn SEO <20 ký tự)",
          badge: "13 Tags",
          isTags: true,
          items: [
            "canada coloring book",
            "autumn landscapes",
            "fall foliage pdf",
            "scenic nature art",
            "procreate coloring",
            "ipad coloring pages",
            "printable adult book",
            "stress relief art",
            "national park gift",
            "canadian travel",
            "digital download",
            "alcohol marker art",
            "bold easy line art"
          ]
        },
        {
          number: "Step 03",
          title: "Listing Description (Mô tả sản phẩm Etsy)",
          badge: "Description",
          isCode: true,
          label: "Toàn văn Listing Description chuẩn Etsy (Click Copy)",
          value: `🍁 AUTUMN IN CANADA: A Scenic Journey Across Provinces & Territories 🍁
30 Handcrafted Landmark Coloring Pages | Instant Digital Download

Explore the breathtaking natural wonders and historic heritage of Canada with this complete 30-page coloring collection. Inspired by traditional woodblock prints, each artwork features bold, clean outlines with spacious rhythmic contour tiers—designed specifically for effortless color washing, smooth gradient blending, and stress-free coloring.

--------------------------------------------------
✨ WHAT YOU WILL RECEIVE IN THIS DIGITAL BUNDLE:
--------------------------------------------------
📦 01 x ZIP Archive (Autumn_in_Canada_Etsy_Digital_Bundle.zip - 19.8 MB) containing:

1. 📂 30 Transparent PNG Files (300 DPI)
   - Perfect for digital coloring on iPad / Tablet (Procreate, GoodNotes, Photoshop, Infinite Painter).
   - Crisp black lines with 100% transparent backgrounds—color directly on layers underneath without obscuring the line art!

2. 📄 01 Home-Printable PDF in US Letter Size (8.5 x 11 inches)
   - Formatted with elegant framing margins, ready for standard North American home printers.

3. 📄 01 Home-Printable PDF in International A4 Size (210 x 297 mm)
   - Formatted for European and international standard home printing.

4. 📖 Printing & Procreate Quick-Start User Guide (TXT)
   - Paper recommendations (Cardstock / Mixed Media) and Procreate layer setup tips.

--------------------------------------------------
🇨🇦 30 ICONIC SCENES INCLUDED:
--------------------------------------------------
• Ontario: Algonquin Canoe, Agawa Canyon Railway, Niagara Falls, Rideau Canal
• Quebec: Château Frontenac, Mont-Tremblant, Montmorency Falls, Jacques-Cartier Valley
• Alberta: Moraine Lake & Ten Peaks, Icefields Parkway Elk, Dinosaur Badlands, Banff Hot Springs
• British Columbia: Okanagan Vineyards, Lynn Canyon Bridge, Tofino Surf, Yoho Natural Bridge
• Atlantic: Cabot Trail, Peggy's Cove, Hopewell Rocks, Dickson Falls, Cavendish Cliffs, Point Prim, Western Brook Fjord, Quidi Vidi, Cape Spear
• Prairies & North: Riding Mountain Marsh, Churchill Polar Bears & Aurora, Prairie Grain Elevators, Tombstone Mountain, Alexandra Falls

--------------------------------------------------
💡 HOW TO DOWNLOAD & USE:
--------------------------------------------------
1. Complete your purchase.
2. Etsy will immediately provide a download link in your account under Purchases and Reviews.
3. Download the ZIP file to your computer or iPad.
4. Extract the ZIP file and start coloring right away!

*Note: This is an instant digital download. No physical book will be shipped.*`
        },
        {
          number: "Step 04",
          title: "Deliverable Files Upload (Tải lên file kỹ thuật số)",
          badge: "File Delivery",
          fields: [
            { label: "File phân phối chính", value: "dist/Autumn_in_Canada_Etsy_Digital_Bundle.zip (19.87 MB)" },
            { label: "Định dạng listing", value: "Digital item (Instant download ngay sau khi thanh toán)" },
            { label: "Giấy phép sử dụng", value: "Personal Use Only (Không chuyển nhượng hoặc bán lại file số thô)" }
          ]
        },
        {
          number: "Step 05",
          title: "Pricing & Renewal Settings (Định giá & Cài đặt)",
          badge: "Settings",
          fields: [
            { label: "Listing Price (Giá bán đề xuất)", value: "$4.99 — $5.99 USD" },
            { label: "Renewal Options", value: "Automatic ($0.20 USD phí gia hạn sau mỗi 4 tháng hoặc khi bán hết)" },
            { label: "Section Phân loại shop", value: "Coloring Books / Digital Downloads" }
          ]
        }
      ]
    }
  },
  capybara: {
    kdp: {
      channelTitle: "Amazon KDP Paperback Publishing (Barnaby's Peaceful Days)",
      badgeText: "KDP Print-on-Demand",
      steps: [
        {
          number: "Step 01",
          title: "Book Details & Author (Thông tin sách)",
          badge: "Metadata",
          fields: [
            { label: "Book Title (Tiêu đề chính)", value: "Barnaby's Peaceful Days" },
            { label: "Subtitle (Phụ đề tối ưu SEO)", value: "A Bold & Easy Cozy Capybara Coloring Book: 30 Relaxing and Cute Daily Life Scenes for Adults, Teens, and Beginners" },
            { label: "Series Title", value: "Cozy Animal Companions (Book 1)" },
            { label: "Edition Number", value: "1" },
            { label: "Author / Contributor Name", value: "Cozy Burrow Press" }
          ]
        },
        {
          number: "Step 02",
          title: "HTML Book Description (Mô tả giàu định dạng KDP)",
          badge: "Rich HTML",
          isCode: true,
          label: "Mã HTML Description (Click Copy & dán thẳng vào ô Description trên KDP)",
          value: `<h3>Slow Down, Breathe, and Unwind with Barnaby the Capybara!</h3>
<p>Step into a gentle world of everyday tranquility with <b>Barnaby's Peaceful Days</b>, a heartwarming collection of 30 bold, easy-to-color scenes celebrating the soothing beauty of quiet moments.</p>

<p>Designed specifically to eliminate coloring fatigue, every page features ultra-bold outlines and large open spaces that are effortlessly satisfying to fill with alcohol markers, gel pens, or colored pencils. No overwhelming micro-details, no stress—just pure calming flow.</p>

<h3>Why You Will Love This Cozy Coloring Book:</h3>
<ul>
  <li><b>30 Wholesome Daily Life Scenes:</b> Join Barnaby as he sips morning matcha, bakes artisan bread, visits local plant shops, and stargazes by a warm campfire.</li>
  <li><b>Bold, High-Contrast Outlines:</b> Thick 3–4pt contour lines make staying inside the lines effortless, perfect for relaxation and all skill levels.</li>
  <li><b>Single-Sided Pages with Dark Ink Shields:</b> Every artwork is backed by a dark bleed shield page to prevent marker bleed-through onto the next illustration.</li>
  <li><b>Color Swatches Test Page:</b> Conveniently test your shades, markers, and blending gradients before starting your page.</li>
  <li><b>Square 8.5 x 8.5 Inch Format:</b> The beloved square art book layout popular across TikTok, Instagram, and adult coloring communities.</li>
</ul>

<p><b>The ultimate gift for capybara lovers, cozy lifestyle fans, and anyone looking for a daily dose of mindfulness and peace.</b></p>`
        },
        {
          number: "Step 03",
          title: "7 Search Keywords (Thuật toán tìm kiếm Amazon A9)",
          badge: "A9 Search",
          isKeywords: true,
          items: [
            "cute simple relaxing aesthetic hygge cottagecore",
            "stress relief relaxation adults teens seniors beginners",
            "mindful mindfulness calming anxiety therapy gift",
            "quirky animals doing human things funny kawaii daily",
            "thick lines large print easy cozy spaces cafe rooms",
            "mindful coloring pages quick daily chill self care",
            "alcohol marker friendly single sided pages animal lover"
          ]
        },
        {
          number: "Step 04",
          title: "Categories & Target Audience (Danh mục BISAC)",
          badge: "Classification",
          fields: [
            { label: "Primary Category (Chính)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Animals" },
            { label: "Secondary Category (Phụ)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Humorous" },
            { label: "Tertiary Category (Bổ trợ)", value: "Self-Help > Stress Management" },
            { label: "Adult Content Confirmation", value: "No" }
          ]
        },
        {
          number: "Step 05",
          title: "Print Options & Interior Upload (Quy chuẩn in ấn)",
          badge: "Specs & Upload",
          fields: [
            { label: "Interior & Paper Type", value: "Black & white interior with white paper" },
            { label: "Trim Size", value: "8.5 x 8.5 in (21.59 x 21.59 cm)" },
            { label: "Bleed Settings", value: "Bleed (8.625 x 8.750 in)" },
            { label: "Paperback Cover Finish", value: "Matte or Glossy" },
            { label: "Manuscript File", value: "dist/kdp_interior_8.5x8.5.pdf (64 pages)" },
            { label: "Cover File", value: "dist/kdp_full_cover_spread.pdf (17.394 x 8.750 in)" }
          ]
        },
        {
          number: "Step 06",
          title: "Pricing & Royalties (Định giá & Lợi nhuận)",
          badge: "Royalties",
          isRoyalties: true,
          table: [
            { marketplace: "Amazon.com (US)", price: "$6.99 USD", printCost: "$2.15", royalty: "$2.04 / book (~29%)" },
            { marketplace: "Amazon.ca (Canada)", price: "$9.99 CAD", printCost: "$3.12 CAD", royalty: "$2.87 CAD / book" },
            { marketplace: "Amazon.co.uk (UK)", price: "£5.99 GBP", printCost: "£1.85 GBP", royalty: "£1.74 GBP / book" },
            { marketplace: "Amazon.de/fr/es (EU)", price: "€6.99 EUR", printCost: "€2.24 EUR", royalty: "€1.95 EUR / book" }
          ]
        }
      ]
    },
    etsy: {
      channelTitle: "Etsy Digital Download Listing (Barnaby's Peaceful Days)",
      badgeText: "Etsy Instant Download",
      steps: [
        {
          number: "Step 01",
          title: "Listing Title (Tiêu đề SEO 140 ký tự)",
          badge: "SEO Title",
          fields: [
            {
              label: "Listing Title (Chuẩn SEO Etsy Search)",
              value: "Cozy Capybara Coloring Book PDF, 30 Cute Daily Life Pages Digital Download, Bold and Easy Line Art, Procreate Transparent PNG, Stress Relief"
            }
          ]
        },
        {
          number: "Step 02",
          title: "13 Etsy Tags (Thẻ Tag chuẩn SEO <20 ký tự)",
          badge: "13 Tags",
          isTags: true,
          items: [
            "capybara coloring",
            "bold and easy book",
            "cozy coloring pages",
            "printable coloring",
            "procreate coloring",
            "stress relief art",
            "cute animal coloring",
            "mindful coloring pdf",
            "simple line art",
            "kawaii capybara gift",
            "digital coloring book",
            "ipad coloring pages",
            "relaxation gift idea"
          ]
        },
        {
          number: "Step 03",
          title: "Listing Description (Mô tả sản phẩm Etsy)",
          badge: "Description",
          isCode: true,
          label: "Toàn văn Listing Description chuẩn Etsy (Click Copy)",
          value: `☕ BARNABY'S PEACEFUL DAYS: A Cozy Capybara Coloring Book ☕
30 Cute & Relaxing Daily Life Pages | Instant Digital Download

Embrace the slow life with Barnaby the Capybara! This complete 30-page printable coloring collection features bold, easy-to-color outlines perfect for stress relief, relaxation, and mindfulness.

--------------------------------------------------
✨ WHAT IS INCLUDED IN YOUR DOWNLOAD:
--------------------------------------------------
📦 01 x ZIP Archive (Barnaby_Cozy_Capybara_Etsy_Bundle.zip) containing:
1. 📂 30 Transparent PNG Files (300 DPI) for iPad & Procreate
2. 📄 01 Home-Printable PDF in US Letter Size (8.5 x 11 in)
3. 📄 01 Home-Printable PDF in International A4 Size
4. 🎨 Bonus Color Palette Inspiration Guide
5. 📖 Home Printing & Procreate Quick-Start Guide

--------------------------------------------------
💡 HOW IT WORKS:
--------------------------------------------------
1. Purchase this listing.
2. Etsy instantly sends your download link.
3. Download, print at home, or import into Procreate and enjoy!`
        },
        {
          number: "Step 04",
          title: "Deliverable Files Upload (Tải lên file kỹ thuật số)",
          badge: "File Delivery",
          fields: [
            { label: "File phân phối chính", value: "dist/Barnaby_Cozy_Capybara_Etsy_Bundle.zip" },
            { label: "Định dạng listing", value: "Digital item (Instant download)" },
            { label: "Giấy phép sử dụng", value: "Personal Use Only" }
          ]
        },
        {
          number: "Step 05",
          title: "Pricing & Renewal Settings (Định giá & Cài đặt)",
          badge: "Settings",
          fields: [
            { label: "Listing Price (Giá bán đề xuất)", value: "$4.99 USD" },
            { label: "Renewal Options", value: "Automatic ($0.20 USD)" },
            { label: "Section Phân loại shop", value: "Coloring Books / Digital Downloads" }
          ]
        }
      ]
    }
  }
};

let currentGuideChannel = "kdp";

// Global copy helper with fallback and visual feedback
function copyToClipboard(text, btnElement, successLabel = "✓ Đã sao chép!") {
  const originalText = btnElement.innerText || btnElement.textContent;
  
  const performCopy = () => {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    } else {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.left = "-999999px";
      textarea.style.top = "-999999px";
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      try {
        document.execCommand("copy");
        textarea.remove();
        return Promise.resolve();
      } catch (err) {
        textarea.remove();
        return Promise.reject(err);
      }
    }
  };

  performCopy()
    .then(() => {
      btnElement.classList.add("copied");
      btnElement.innerText = successLabel;
      setTimeout(() => {
        btnElement.classList.remove("copied");
        btnElement.innerText = originalText;
      }, 1800);
    })
    .catch(err => {
      console.error("Copy failed: ", err);
      prompt("Sao chép thủ công:", text);
    });
}

function renderPublishingGuide(channel = currentGuideChannel) {
  currentGuideChannel = channel;
  const container = document.getElementById("publishing-guide-content");
  if (!container) return;

  const bookData = PUBLISHING_GUIDES[activeBook] || PUBLISHING_GUIDES.canada;
  const guideData = bookData[channel];
  if (!guideData) return;

  // Update tabs active state
  const kdpTabBtn = document.getElementById("tab-btn-kdp");
  const etsyTabBtn = document.getElementById("tab-btn-etsy");
  if (kdpTabBtn && etsyTabBtn) {
    kdpTabBtn.classList.toggle("active", channel === "kdp");
    etsyTabBtn.classList.toggle("active", channel === "etsy");
  }

  let html = `
    <div style="margin-bottom: 24px; text-align: center;">
      <span class="badge ${channel === 'kdp' ? 'badge-accent' : 'badge-success'}" style="font-size:0.95rem; padding:6px 18px;">
        ${guideData.badgeText}
      </span>
      <h3 style="font-size: 1.4rem; font-weight: 800; margin-top: 10px; color: var(--color-text-main);">
        ${guideData.channelTitle}
      </h3>
    </div>
    <div class="guide-timeline">
  `;

  guideData.steps.forEach((step, sIdx) => {
    html += `
      <div class="guide-step-card">
        <div class="guide-step-header">
          <div class="guide-step-title-wrap">
            <span class="guide-step-badge">${step.number}</span>
            <h4 class="guide-step-title">${step.title}</h4>
          </div>
          <span class="badge badge-info">${step.badge}</span>
        </div>
    `;

    // Render Fields
    if (step.fields && step.fields.length > 0) {
      html += `<div class="copy-field-group">`;
      step.fields.forEach((f, fIdx) => {
        const fieldId = `field_${channel}_${sIdx}_${fIdx}`;
        html += `
          <div class="copy-field-item">
            <label class="copy-field-label">${f.label}</label>
            <div class="copy-field-wrapper">
              <div class="copy-field-val" id="${fieldId}">${escapeHtml(f.value)}</div>
              <button class="btn-inline-copy" onclick="copyField('${fieldId}', this)">
                📋 Sao chép
              </button>
            </div>
          </div>
        `;
      });
      html += `</div>`;
    }

    // Render Code / Rich HTML / Description
    if (step.isCode) {
      const codeId = `code_${channel}_${sIdx}`;
      html += `
        <div class="copy-field-item" style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <label class="copy-field-label">${step.label || 'Mã nguồn'}</label>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyCode('${codeId}', this)">
              📋 Sao chép toàn bộ HTML/Text
            </button>
          </div>
          <pre class="copy-box-code" id="${codeId}">${escapeHtml(step.value)}</pre>
        </div>
      `;
    }

    // Render Keywords Group
    if (step.isKeywords) {
      const allKwText = step.items.join("\n");
      html += `
        <div style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <span style="font-size:0.9rem; color:var(--color-text-muted);">
              7 hộp từ khóa độc lập trên KDP Dashboard (Click từng ô để sao chép):
            </span>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyRawText(\`${escapeAttr(allKwText)}\`, this, '✓ Đã chép 7 box!')">
              📋 Sao chép cả 7 Box
            </button>
          </div>
          <div class="copy-field-group">
      `;
      step.items.forEach((kw, kIdx) => {
        const kwId = `kw_${channel}_${kIdx}`;
        html += `
          <div class="copy-field-item">
            <label class="copy-field-label">Từ khóa Box 0${kIdx + 1} (${kw.length}/50 ký tự)</label>
            <div class="copy-field-wrapper">
              <div class="copy-field-val" id="${kwId}">${escapeHtml(kw)}</div>
              <button class="btn-inline-copy" onclick="copyField('${kwId}', this)">
                📋 Copy Box ${kIdx + 1}
              </button>
            </div>
          </div>
        `;
      });
      html += `</div></div>`;
    }

    // Render Tags Pills Group
    if (step.isTags) {
      const allTagsComma = step.items.join(", ");
      html += `
        <div style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <span style="font-size:0.9rem; color:var(--color-text-muted);">
              13 Thẻ Tags Etsy (<20 ký tự/tag). Click vào thẻ bất kỳ để chép:
            </span>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyRawText(\`${escapeAttr(allTagsComma)}\`, this, '✓ Đã chép 13 tags!')">
              📋 Sao chép toàn bộ 13 Tags (, )
            </button>
          </div>
          <div class="checklist-pills">
      `;
      step.items.forEach((tag, tIdx) => {
        html += `
          <span class="checklist-pill-item" onclick="copyTagPill(this, \`${escapeAttr(tag)}\`)">
            <span>🏷️</span>
            <strong>${escapeHtml(tag)}</strong>
            <small style="opacity:0.75;">(${tag.length}/20)</small>
          </span>
        `;
      });
      html += `</div></div>`;
    }

    // Render Royalties Table
    if (step.isRoyalties && step.table) {
      html += `
        <div style="overflow-x: auto;">
          <table class="royalties-table">
            <thead>
              <tr>
                <th>Thị trường (Marketplace)</th>
                <th>Giá niêm yết (List Price)</th>
                <th>Chi phí in KDP</th>
                <th>Lợi nhuận ước tính (Est. Royalty)</th>
              </tr>
            </thead>
            <tbody>
      `;
      step.table.forEach(row => {
        html += `
          <tr>
            <td><strong>${escapeHtml(row.marketplace)}</strong></td>
            <td><span class="badge badge-accent">${escapeHtml(row.price)}</span></td>
            <td>${escapeHtml(row.printCost)}</td>
            <td><strong style="color:#15803d;">${escapeHtml(row.royalty)}</strong></td>
          </tr>
        `;
      });
      html += `</tbody></table></div>`;
    }

    // Render Alert Box
    if (step.alert) {
      html += `
        <div class="guide-alert-box">
          ⚠️ ${step.alert}
        </div>
      `;
    }

    html += `</div>`; // End guide-step-card
  });

  html += `</div>`; // End guide-timeline
  container.innerHTML = html;
}

// Helpers for inline onclick events
function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeAttr(str) {
  if (!str) return "";
  return String(str).replace(/\`/g, "\\`").replace(/\${/g, "\\${");
}

window.copyField = function(elementId, btnElement) {
  const el = document.getElementById(elementId);
  if (el) {
    copyToClipboard(el.innerText || el.textContent, btnElement);
  }
};

window.copyCode = function(elementId, btnElement) {
  const el = document.getElementById(elementId);
  if (el) {
    copyToClipboard(el.textContent, btnElement);
  }
};

window.copyRawText = function(text, btnElement, successMsg = "✓ Đã sao chép!") {
  copyToClipboard(text, btnElement, successMsg);
};

window.copyTagPill = function(pillElement, text) {
  copyToClipboard(text, pillElement, "✓ Chép tag!");
};
