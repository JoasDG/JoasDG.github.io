$('section').on('click', function(e){
  e.preventDefault();
  window.location.href=$(this).data('link');
})
