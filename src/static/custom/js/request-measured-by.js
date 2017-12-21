$(document).ready(function () {
    $('form').on('change', '.select-ingredient-type', function () {
        var selectElement = $(this);
        var ingredientType = $(this).val();
        if (ingredientType === '') {
            return;
        }

        $.ajax({
            url: '/api/v1/ingredient-types/' + ingredientType,
            dataType: 'json',
            success: function (data) {
                if (data.measured_by === null) {
                    selectElement.parent().siblings(".measured-by").each(function() {
                        $(this).removeClass('uk-hidden');
                    });
                    return;
                }


                var measuredBySelector = '.' + data.measured_by;
                var measuredByAndSelector = ".measured-by" + measuredBySelector;

                var divsWithMeasuredByAnd = selectElement.parent().siblings(measuredByAndSelector);
                divsWithMeasuredByAnd.each(function () {
                    if ($(this).hasClass('uk-hidden') === true) {
                        $(this).removeClass('uk-hidden');
                    }

                    $(this).children('input[type=number]').val("");
                });

                var measuredByAndNotSelector = ".measured-by:not(" + measuredBySelector + ")";
                var divsWithMeasuredByAndNot = selectElement.parent().siblings(measuredByAndNotSelector);
                divsWithMeasuredByAndNot.each(function () {
                    if ($(this).hasClass('uk-hidden') === false) {
                        $(this).addClass('uk-hidden');
                    }

                    $(this).children('input[type=number]').val("");
                });
            },
            error: function (data) {
                alert("There was an error, please try later.");
            }
        });
    });
});