<script src="script.js"></script>
<script>
  document.getElementById('acceptCookies').addEventListener('click', function() {
    document.getElementById('cookiePopup').style.display = 'none';
    localStorage.setItem('cookiesAccepted', 'true');
  });

  window.onload = function() {
    if (!localStorage.getItem('cookiesAccepted')) {
      document.getElementById('cookiePopup').style.display = 'block';
    }
  };
</script>
