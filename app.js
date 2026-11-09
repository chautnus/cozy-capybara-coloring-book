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
  { page: 1, filter: "central", title: "Algonquin Provincial Park", province: "Ontario", caption: "Cedar canoe resting on the quiet lake shore under maple canopy.", src: "assets/canada/processed/page_01_clean.png" },
  { page: 2, filter: "central", title: "Agawa Canyon Scenic Railway", province: "Northern Ontario", caption: "Vintage passenger tour train winding along the granite canyon floor.", src: "assets/canada/processed/page_02_clean.png" },
  { page: 3, filter: "central", title: "Niagara Horseshoe Falls", province: "Ontario", caption: "Thunderous curved waterfall panorama framed by stone promenade.", src: "assets/canada/processed/page_03_clean.png" },
  { page: 4, filter: "central", title: "Rideau Canal & ByWard", province: "Ottawa, Ontario", caption: "Pleasure boat cruising peaceful canal waters under autumn foliage.", src: "assets/canada/processed/page_04_clean.png" },
  { page: 5, filter: "central", title: "Château Frontenac & Old Quebec", province: "Quebec", caption: "Historic castle hotel and horse carriage on cobblestone lane.", src: "assets/canada/processed/page_05_clean.png" },
  { page: 6, filter: "central", title: "Mont-Tremblant Alpine Village", province: "Quebec", caption: "Pedestrian village clock tower and gondola ascending autumn peak.", src: "assets/canada/processed/page_06_clean.png" },
  { page: 7, filter: "central", title: "Montmorency Falls & Bridge", province: "Quebec", caption: "Suspension footbridge spanning roaring 83-meter waterfall crest.", src: "assets/canada/processed/page_07_clean.png" },
  { page: 8, filter: "central", title: "Jacques-Cartier Glacial Valley", province: "Quebec", caption: "Serpentine river curving between towering glacial gorge walls.", src: "assets/canada/processed/page_08_clean.png" },
  { page: 9, filter: "west", title: "Moraine Lake & Ten Peaks", province: "Banff, Alberta", caption: "Jagged snow-dusted summits towering over glassy turquoise water.", src: "assets/canada/processed/page_09_clean.png" },
  { page: 10, filter: "west", title: "Icefields Parkway Bull Elk", province: "Alberta", caption: "Majestic bull elk grazing in a golden mountain meadow vista.", src: "assets/canada/processed/page_10_clean.png" },
  { page: 11, filter: "west", title: "Dinosaur Badlands Hoodoos", province: "Alberta", caption: "Mushroom-shaped sandstone pillars sculpted by ancient rivers.", src: "assets/canada/processed/page_11_clean.png" },
  { page: 12, filter: "west", title: "Banff Upper Hot Springs", province: "Banff, Alberta", caption: "Steaming open-air mineral pool surrounded by snow-dusted pines.", src: "assets/canada/processed/page_12_clean.png" },
  { page: 13, filter: "west", title: "Okanagan Valley Vineyards", province: "British Columbia", caption: "Terraced grapevines overlooking sunlit blue lake and winery.", src: "assets/canada/processed/page_13_clean.png" },
  { page: 14, filter: "west", title: "Lynn Canyon Suspension Bridge", province: "North Vancouver, BC", caption: "Wooden footbridge swaying above rushing canyon stream and cedars.", src: "assets/canada/processed/page_14_clean.png" },
  { page: 15, filter: "west", title: "Tofino Pacific Coast & Driftwood", province: "Vancouver Island, BC", caption: "Wild ocean beach with giant driftwood logs and misty sea stacks.", src: "assets/canada/processed/page_15_clean.png" },
  { page: 16, filter: "west", title: "Natural Bridge & Emerald Lake", province: "Yoho National Park, BC", caption: "Ancient limestone natural stone bridge carved by glacier torrents.", src: "assets/canada/processed/page_16_clean.png" },
  { page: 17, filter: "atlantic", title: "The Cabot Trail Ocean Bluffs", province: "Cape Breton, Nova Scotia", caption: "Sweeping highway perched above ocean swells and fiery hills.", src: "assets/canada/processed/page_17_clean.png" },
  { page: 18, filter: "atlantic", title: "Peggy's Cove Lighthouse", province: "Nova Scotia", caption: "Classic beacon on smooth glacial granite boulders and ocean surf.", src: "assets/canada/processed/page_18_clean.png" },
  { page: 19, filter: "atlantic", title: "Hopewell Rocks Flowerpots", province: "Bay of Fundy, NB", caption: "Towering sandstone sea stacks standing on dry ocean floor at low tide.", src: "assets/canada/processed/page_19_clean.png" },
  { page: 20, filter: "atlantic", title: "Dickson Falls Forest Brook", province: "Fundy National Park, NB", caption: "Cascading forest brook tumbling down mossy boulders and footbridge.", src: "assets/canada/processed/page_20_clean.png" },
  { page: 21, filter: "atlantic", title: "Cavendish Red Sandstone Cliffs", province: "Prince Edward Island", caption: "Vivid red coastal bluffs contrasting with golden dunes and waves.", src: "assets/canada/processed/page_21_clean.png" },
  { page: 22, filter: "atlantic", title: "Point Prim Historic Lighthouse", province: "Prince Edward Island", caption: "Oldest circular brick lighthouse (1845) on a breezy ocean point.", src: "assets/canada/processed/page_22_clean.png" },
  { page: 23, filter: "atlantic", title: "Western Brook Pond Fjord", province: "Gros Morne, Newfoundland", caption: "Tour boat navigating two-thousand-foot vertical glacier cliffs.", src: "assets/canada/processed/page_23_clean.png" },
  { page: 24, filter: "atlantic", title: "Quidi Vidi Fishing Village", province: "St. John's, Newfoundland", caption: "Traditional wooden fishing stages on stilts in sheltered cove.", src: "assets/canada/processed/page_24_clean.png" },
  { page: 25, filter: "atlantic", title: "Cape Spear Easternmost Point", province: "Newfoundland", caption: "Historic 1836 lighthouse at the easternmost tip of North America.", src: "assets/canada/processed/page_25_clean.png" },
  { page: 26, filter: "prairie_north", title: "Riding Mountain Ominik Marsh", province: "Manitoba", caption: "Floating boardwalk S-curve winding through cattails and golden birches.", src: "assets/canada/processed/page_26_clean.png" },
  { page: 27, filter: "prairie_north", title: "Churchill Polar Bears & Aurora", province: "Northern Manitoba", caption: "Polar bear family traversing autumn tundra under flowing aurora arches.", src: "assets/canada/processed/page_27_clean.png" },
  { page: 28, filter: "prairie_north", title: "Prairie Grain Elevators", province: "Saskatchewan", caption: "Iconic wooden grain towers rising above endless ripe wheat fields.", src: "assets/canada/processed/page_28_clean.png" },
  { page: 29, filter: "prairie_north", title: "Tombstone Mountain & Tundra", province: "Yukon Territory", caption: "Crimson subarctic tundra plain facing the razor-sharp granite spire.", src: "assets/canada/processed/page_29_clean.png" },
  { page: 30, filter: "prairie_north", title: "Alexandra Falls Gorge", province: "Northwest Territories", caption: "Thirty-two-meter limestone waterfall curtain framed by amber birches.", src: "assets/canada/processed/page_30_clean.png" }
];

let activeBook = "canada"; // Default to newest release

const BOOK_CONFIGS = {
  canada: {
    brandBadge: "NEW RELEASE • KDP & ETSY",
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
    brandBadge: "BOOKTOK BESTSELLER PIPELINE",
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
    return `
    <article class="page-card" data-page="${item.page}">
      <div class="page-card-header">
        <span class="page-num">Page ${String(item.page).padStart(2, '0')}</span>
        ${provinceBadge}
      </div>
      <div class="page-preview-frame">
        <img src="${item.src}" alt="${item.title}" class="page-preview-img" loading="lazy" onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22300%22 height=%22300%22><rect width=%22300%22 height=%22300%22 fill=%22%23eee%22/><text x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 fill=%22%23999%22>Page ${item.page}</text></svg>'" />
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
  switchBook("canada");
});
