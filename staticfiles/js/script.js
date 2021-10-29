console.log('working')

let theme = localStorage.getItem('theme')

if (theme == null) {
    setTheme('light')
} else {
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot');

for (var i = 0; themeDots.length > i; i++) {
    themeDots[i].addEventListener('click', function() {
        let mode = this.dataset.mode
        console.log('option clicked', mode)
        setTheme(mode)
    })
}

function setTheme(mode) {
    if (mode == 'light') {
        document.getElementById('theme-style').href =
            static + '/default.css'
    }
    if (mode == 'blue') {
        document.getElementById('theme-style').href =
            static + '/blue.css'
    }
    if (mode == 'green') {
        document.getElementById('theme-style').href =
            static + '/green.css'
    }
    if (mode == 'purple') {
        document.getElementById('theme-style').href =
            static + '/purple.css'
    }
    localStorage.setItem('theme', mode)
}

$(function() {
    console.log('jquery')
        //----- OPEN
    $('[data-popup-open]').on('click', function(e) {
        var targeted_popup_class = jQuery(this).attr('data-popup-open');
        $('[data-popup="' + targeted_popup_class + '"]').fadeIn(350);

        e.preventDefault();
    });

    //----- CLOSE
    $('[data-popup-close]').on('click', function(e) {
        var targeted_popup_class = jQuery(this).attr('data-popup-close');
        $('[data-popup="' + targeted_popup_class + '"]').fadeOut(350);

        e.preventDefault();
    });
});