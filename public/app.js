// Barnaby's Peaceful Days - Dynamic 30-Page Gallery & Prompt Viewer

const PAGES_DATA = [
  { page: 1, chapter: 1, title: "Morning Sun & Herbal Tea", caption: "A quiet morning begins with a warm cup of herbal tea." },
  { page: 2, chapter: 1, title: "Watering Greenhouse Succulents", caption: "Growing happiness, one tiny leaf at a time." },
  { page: 3, chapter: 1, title: "The Village Artisan Bakery", caption: "The sweetest aroma in the whole village." },
  { page: 4, chapter: 1, title: "Market Stroll with Straw Basket", caption: "Simple treats from a sunny morning stroll." },
  { page: 5, chapter: 1, title: "Bicycle with a Flower Basket", caption: "Pedaling slowly down peaceful country roads." },
  { page: 6, chapter: 1, title: "Breakfast by the Garden Table", caption: "Sweet pancakes taste better under the open sky." },
  { page: 7, chapter: 1, title: "Greeting the Garden Snail", caption: "There is no rush to get anywhere today." },
  { page: 8, chapter: 1, title: "Reading in the Window Nook", caption: "Lost in cozy adventures between the pages." },
  { page: 9, chapter: 2, title: "The Cozy Antiquarian Bookstore", caption: "Keeper of stories and dusty forgotten wonders." },
  { page: 10, chapter: 2, title: "Afternoon Tea with Baby Ducklings", caption: "The finest company is always warm and gentle." },
  { page: 11, chapter: 2, title: "Pottery Studio Workshop", caption: "Shaping calm thoughts with loving hands." },
  { page: 12, chapter: 2, title: "Flower Arranging in Glass Jars", caption: "Bringing a splash of wild nature indoors." },
  { page: 13, chapter: 2, title: "Painting Watercolors in the Meadow", caption: "Painting colors that whisper tranquility." },
  { page: 14, chapter: 2, title: "Coffee Break with Hedgehog Friend", caption: "Warm conversations on a breezy afternoon." },
  { page: 15, chapter: 2, title: "Sewing a Patchwork Quilt", caption: "Stitching warmth into every corner." },
  { page: 16, chapter: 2, title: "Arranging the Spice Jars", caption: "Every scent tells a story of cozy comfort." },
  { page: 17, chapter: 3, title: "Floating Leaf Boat on Lily Pond", caption: "Floating gently wherever the calm waters lead." },
  { page: 18, chapter: 3, title: "The Relaxing Onsen Springs", caption: "Total peace is doing absolutely nothing at all." },
  { page: 19, chapter: 3, title: "Mushroom Foraging in Pine Forest", caption: "Treasures waiting beneath the soft forest moss." },
  { page: 20, chapter: 3, title: "Hammock Nap Between Apple Trees", caption: "Afternoon naps are sweet gifts to the soul." },
  { page: 21, chapter: 3, title: "Bird Watching with Binoculars", caption: "Listening closely to the songs of the breeze." },
  { page: 22, chapter: 3, title: "Rainy Day at Covered Porch", caption: "The soothing rhythm of gentle raindrops." },
  { page: 23, chapter: 3, title: "Fly-Fishing in Whispering Stream", caption: "Patience is the sweetest kind of quiet." },
  { page: 24, chapter: 3, title: "Picnic Under Great Willow Tree", caption: "Basking in the gentle shade of gratitude." },
  { page: 25, chapter: 4, title: "Baking Fresh Apple Cinnamon Pie", caption: "The kitchen is full of warmth, sugar, and spice." },
  { page: 26, chapter: 4, title: "Fireplace Warmth & Hot Cocoa", caption: "Cozy embers chase the evening chill away." },
  { page: 27, chapter: 4, title: "Stargazing with Brass Telescope", caption: "Wishing on a sky full of quiet dreams." },
  { page: 28, chapter: 4, title: "Playing Acoustic Lullabies", caption: "Soft melodies singing the day to rest." },
  { page: 29, chapter: 4, title: "Brushing Teeth in Vintage Bathroom", caption: "Ready for dreamland after a lovely day." },
  { page: 30, chapter: 4, title: "Sleepy Night in Cloud Bed", caption: "Rest peacefully, gentle friend. Tomorrow brings joy." }
];

let fluxPrompts = {};
let mjPrompts = {};

async function loadPrompts() {
  try {
    const [resFlux, resMj] = await Promise.all([
      fetch("prompts/flux_prompts.json"),
      fetch("prompts/midjourney_prompts.json")
    ]);
    if (resFlux.ok) {
      const arrFlux = await resFlux.json();
      arrFlux.forEach(item => { fluxPrompts[item.page] = item.prompt; });
    }
    if (resMj.ok) {
      const arrMj = await resMj.json();
      arrMj.forEach(item => { mjPrompts[item.page] = item.prompt; });
    }
  } catch (err) {
    console.warn("Using offline prompt fallback:", err);
  }
}

function renderPages(filterChapter = "all") {
  const container = document.getElementById("pages-grid");
  if (!container) return;

  const filtered = filterChapter === "all"
    ? PAGES_DATA
    : PAGES_DATA.filter(p => p.chapter.toString() === filterChapter);

  container.innerHTML = filtered.map(item => {
    const imgSrc = `assets/processed/page_${String(item.page).padStart(2, '0')}_clean.png`;
    return `
    <article class="page-card" data-page="${item.page}">
      <div class="page-card-header">
        <span class="page-num">Page ${String(item.page).padStart(2, '0')}</span>
        <span class="page-chapter">Chapter ${item.chapter}</span>
      </div>
      <div class="page-preview-frame">
        <img src="${imgSrc}" alt="${item.title}" class="page-preview-img" loading="lazy" onerror="this.parentElement.style.display='none'" />
      </div>
      <h3 class="page-title">${item.title}</h3>
      <p class="page-caption">"${item.caption}"</p>
      <div class="prompt-copy-btns">
        <button class="btn-copy" onclick="copyPrompt(${item.page}, 'flux')">Copy FLUX</button>
        <button class="btn-copy" onclick="copyPrompt(${item.page}, 'mj')">Copy Midjourney</button>
      </div>
    </article>
  `;
  }).join("");
}

function copyPrompt(pageNum, model) {
  const text = model === 'flux'
    ? (fluxPrompts[pageNum] || `FLUX prompt for page ${pageNum}`)
    : (mjPrompts[pageNum] || `Midjourney prompt for page ${pageNum}`);

  navigator.clipboard.writeText(text).then(() => {
    alert(`Copied ${model.toUpperCase()} prompt for Page ${pageNum} to clipboard!`);
  }).catch(() => {
    prompt("Copy this prompt:", text);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  await loadPrompts();
  renderPages("all");

  const tabButtons = document.querySelectorAll(".tab-btn");
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderPages(btn.dataset.chapter);
    });
  });
});
