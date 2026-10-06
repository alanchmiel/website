/** Progressive enhancement: content and navigation work without JavaScript.
 * Only the phone menu changes state. Escape returns focus to its toggle.
 */
document.body.classList.add('js');
const button = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function setOpen(open) {
  navigation.classList.toggle('open', open);
  button.setAttribute('aria-expanded', String(open));
  button.textContent = open ? button.dataset.close : button.dataset.open;
}
button.addEventListener('click', () => setOpen(button.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') {
    setOpen(false); button.focus();
  }
});
