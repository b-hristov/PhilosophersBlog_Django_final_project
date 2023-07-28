
const banner = document.querySelector('.greeting-banner');

function showGreetingBanner(username) {
  banner.querySelector('p').textContent = `Welcome, ${username}! Enjoy our webspace and create your own content!`;
  banner.style.display = 'block';
  setTimeout(hideGreetingBanner, 5000);
}

function showGreetingBannerNoUser() {
  banner.querySelector('p').textContent = `Welcome, dear friend! Please login to your account to see the posts!`;
  banner.style.display = 'block';
  setTimeout(hideGreetingBanner, 5000);
}

function hideGreetingBanner() {
  banner.style.display = 'none';
}

const username = banner.dataset.username;

// Show the banner when the user is authenticated
const isAuthenticated = true;
if (isAuthenticated) {
  showGreetingBanner(username);
  console.log(true)
} else {
  showGreetingBannerNoUser()
  console.log(false)
}

