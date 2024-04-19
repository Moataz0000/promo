// some scripts

// jquery ready start
$(document).ready(function() {
	// closing from click inside menuu
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });



   // check if the page is reload and if reload it showing the page but if not reload not showing the page
    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
        } else {
            $(this).closest('.js-check').removeClass('active');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} 




    
}); 
// jquery end

// just 4 secand display message
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 4000);




// "Owl Carousel" دي مكتبة في الجافا اسكريبت بنستخدمها علشان تعملنا انميشن اتوماتك لما نروح بالسهم علي المنتج 
// karsol