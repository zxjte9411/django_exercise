(($) => {
    $('.btn-delete').click(function () {
        let button = this;
        $.ajax({
            'url': $(button).data('href'),
            'type': 'DELETE'
        }).done(function () {
            $(button).parent('.store').remove();
        }).fail(function (e) {
            console.log(e);
        });
    });
})(jQuery);