const fs = require('fs');
const vm = require('vm');

let outputHtml = '';
const mockElement = () => ({
  classList: { add: () => {}, remove: () => {}, toggle: () => {} },
  querySelectorAll: () => [],
  addEventListener: () => {},
  setAttribute: () => {},
  set innerHTML(val) { outputHtml = val; },
  get innerHTML() { return outputHtml; },
  textContent: '',
  innerText: ''
});

const sandbox = {
  document: {
    querySelectorAll: () => [],
    querySelector: () => mockElement(),
    getElementById: (id) => mockElement(),
    addEventListener: () => {}
  },
  window: {},
  navigator: { clipboard: { writeText: () => Promise.resolve() } },
  console: console,
  getHtml: () => outputHtml
};

const code = fs.readFileSync('public/app.js', 'utf-8');
vm.createContext(sandbox);
vm.runInContext(code + `
  console.log("Calling renderPublishingGuide('kdp')...");
  renderPublishingGuide('kdp');
  console.log("KDP Render output length:", getHtml().length);
  console.log("KDP Has Amazon:", getHtml().includes("Amazon"));

  console.log("Calling renderPublishingGuide('etsy')...");
  renderPublishingGuide('etsy');
  console.log("Etsy Render output length:", getHtml().length);
  console.log("Etsy Has Etsy:", getHtml().includes("Etsy"));
`, sandbox);
