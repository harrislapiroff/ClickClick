/* 
 * Keycut -- bind keyboard shortcuts to links and buttons
 *
 * Usage:
 *    <a href="next" data-keycut="123">Next</a>
 *
 */

(function ($) {

	var KEYCODES = {
		BACKSPACE: 8,
		COMMA: 188,
		DELETE: 46,
		DOWN: 40,
		END: 35,
		ENTER: 13,
		ESCAPE: 27,
		HOME: 36,
		LEFT: 37,
		PAGE_DOWN: 34,
		PAGE_UP: 33,
		PERIOD: 190,
		RIGHT: 39,
		SPACE: 32,
		TAB: 9,
		UP: 38
	}

	$(function(){
		$(document).on('keyup', function (e) {
			var key = e.which;
			$('[data-keycut]').each(function (i) {
				var $this = $(this);
				if (KEYCODES[$this.data('keycut')] === e.which) {
					window.location = $this.attr('href');
					return false; // break the loop
				} // endif
			}); // end [data-keycut] each
		}); // end document on keyup
	}) // end $

}).call(this, jQuery);

