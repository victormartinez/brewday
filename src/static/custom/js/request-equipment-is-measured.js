$(document).ready(function () {
    $('form').on('change', '.select-equipment', function () {
        var selectElement = $(this);
        var equipmentId = $(this).val();
        if (equipmentId === '') {
            return;
        }

        $.ajax({
            url: '/api/v1/equipments/' + equipmentId,
            dataType: 'json',
            success: function (data) {
                var siblings = selectElement.parent().siblings('.measured-by-volume');
                if (data.is_measured === false) {
                    console.log(siblings);
                    siblings.each(function () {
                        $(this).addClass('uk-hidden');
                    });
                }

                if (data.is_measured === true) {
                    console.log(siblings);
                    siblings.each(function () {
                        $(this).removeClass('uk-hidden');
                    });
                }
            },
            error: function (data) {
                alert("There was an error, please try later.");
            }
        });
    });
});