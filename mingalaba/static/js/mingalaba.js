const navigation = document.querySelector('[data-navigation]');
const mobileNavigation = navigation.querySelector('[data-mobile-navigation]');
const body = document.querySelector('body');
const mobileNavigationToggle = navigation.querySelector(
  '[data-mobile-navigation-toggle]',
);


// Mobile Navigation
function toggleMobileNavigation() {
  if (mobileNavigation.hidden) {
    body.classList.add('no-scroll');
    mobileNavigation.hidden = false;
    mobileNavigationToggle.setAttribute('aria-expanded', 'true');
  } else {
    body.classList.remove('no-scroll');
    mobileNavigation.hidden = true;
    mobileNavigationToggle.setAttribute('aria-expanded', 'false');
  }
}


// Load Image
async function load_image(image, container) {
    if (image !== null && image !== "") {
      let response = await fetch(`/api/gtimg/${image}`);
      let data = await response.json();
      
      let img = new Image();
      let url = `${media_prefix}${data.file}`;
  
      img.onload = function() {
        container.style.backgroundImage = `url(${url})`;
        container.style.opacity = 1;
      }
  
      img.src = url;
  
      if (img.complete) img.onload();
    }
    else {
      return;
    }
  }


// Main: Funciton calls
document.addEventListener('DOMContentLoaded', () => {

    mobileNavigationToggle.addEventListener('click', () => {
        toggleMobileNavigation();
    });
});