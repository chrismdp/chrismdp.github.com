const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const script = fs.readFileSync('assets/js/comics.js', 'utf8');
async function run(urls, ok = true) {
  const buttons = Array.from({length: 2}, () => ({hidden: true, addEventListener(_, fn) { this.click = fn; }}));
  let destination;
  vm.runInNewContext(script, {
    document: {querySelectorAll: () => buttons, currentScript: {src: 'https://example.com/assets/js/comics.js'}},
    location: {origin: 'https://example.com', pathname: '/comics/current/', assign: url => {destination = url;}},
    URL, Math,
    fetch: async url => {
      assert.equal(url.href, 'https://example.com/comics/index.json');
      return {ok, json: async () => urls};
    }
  });
  await new Promise(resolve => setImmediate(resolve));
  return {buttons, destination: () => destination};
}
(async () => {
  const normal = await run(['/comics/current/', '/comics/other/']);
  for (const button of normal.buttons) {
    assert.equal(button.hidden, false);
    button.click();
    assert.equal(normal.destination(), '/comics/other/');
  }
  for (const result of [await run(['/comics/current/']), await run([], false)]) {
    assert.ok(result.buttons.every(button => button.hidden));
  }
  console.log('PASS: both random buttons exclude current comic; empty/failing catalogues remain usable');
})();
