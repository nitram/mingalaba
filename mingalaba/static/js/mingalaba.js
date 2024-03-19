// const navigation = document.querySelector('[data-navigation]');
// const mobileNavigation = navigation.querySelector('[data-mobile-navigation]');
const body = document.querySelector('body');
// const mobileNavigationToggle = navigation.querySelector(
//   '[data-mobile-navigation-toggle]',
// );


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


// Function to check if an element is in the viewport
function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    
    return (
        rect.top >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
    );
}


// Function to handle scroll event
function handleScroll() {
    var title = document.querySelector('.animated-title');

    // Check if the welcome title is in the viewport
    if (isInViewport(title)) {
        // Wait for 1 second and then add class to trigger animation
        document.querySelectorAll('.animated-title .title-text').forEach((text) => {
            setTimeout(function() {
                text.classList.add('show-text');
            }, 300);
        });
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

    // mobileNavigationToggle.addEventListener('click', () => {
    //     toggleMobileNavigation();
    // });

    // Add scroll event listener
    window.addEventListener('scroll', handleScroll);
});