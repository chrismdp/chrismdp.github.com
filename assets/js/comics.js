(() => {
  'use strict';
  const buttons = document.querySelectorAll('[data-random-comic]');
  if (!buttons.length) return;
  const script = document.currentScript;
  const catalogueUrl = new URL('../../comics/index.json', script.src);
  fetch(catalogueUrl)
    .then(response => {
      if (!response.ok) throw new Error('Comic catalogue unavailable');
      return response.json();
    })
    .then(urls => {
      const choices = urls.filter(url => new URL(url, location.origin).pathname !== location.pathname);
      if (!choices.length) return;
      buttons.forEach(button => {
        button.hidden = false;
        button.addEventListener('click', () => {
          location.assign(choices[Math.floor(Math.random() * choices.length)]);
        });
      });
    })
    .catch(() => {}); // Previous, next and the archive remain available without JavaScript.
})();
