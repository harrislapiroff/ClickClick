(function($){
	
	var urlify = function(str){
		str = str.replace(/[^a-zA-Z0-9\s-_]/g,"");
		str = str.toLowerCase();
		str = str.replace(/\s/g,'-');
		return str
	}
	
	// Set events to prepopulate fields marked for prepopulation.
	$(function(){
		$('[data-prepopulate-slug]').each(function(){
			var prepopulate_to = $(this),
				prepopulate_from = $('#'+prepopulate_to.attr('data-prepopulate-slug')); // hopefully that attribute is an ID!
			
			// Only add the prepopulation events if the slug field is empty.
			if (prepopulate_to.val() === "") {
				// add the prepopulation event
				prepopulate_from.on("keydown.prepopulate keyup.prepopulate change.prepopulate", function(){
					var title = prepopulate_from.val(),
						slug = urlify(title);
					prepopulate_to.val(slug);
				});
				// remove the prepopulation event if they edit the slug field
				prepopulate_to.on("keydown.prepopulate", function(){
					prepopulate_from.off('.prepopulate');
					prepopulate_to.off('.prepopulate');
				});
			}
			
		})
	});
	
	// Set slugs that are meant to be part of URLs inside of their URLs.
	// TODO: Someday this should probably be handled on the server-side instead of in javascript.
	$(function(){
		$('[data-slug-url]').each(function(){
			var $this = $(this),
				template = $this.attr('data-slug-url').split('--INPUT_HERE--');
				$this.before(template[0]);
				$this.after(template[1]);
		});
	});
	
	// Set clicking on a .field element to focus on the input inside
	$(function(){
		$('.input').click(function(){
			var $this = $(this);
			$('input, textarea', $this).focus();
			$('.input').removeClass('focus');
			$this.addClass('focus');
		});
		$('.input input, .input textarea').blur(function(){
			var $this = $(this);
			$this.parent('.input').removeClass('focus')
		});
		$('.input input, .input textarea').focus(function(){
			var $this = $(this);
			$this.parent('.input').addClass('focus')
		});
	})

	// Set off tooltips
	$(function(){
		$('.tipped').tooltip();
	})
	
}).call(this, jQuery)