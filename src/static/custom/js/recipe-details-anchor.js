$(document).ready(function () {
    $('.recipe-card').on('click', function () {
        var recipeUrl = $(this).find('.recipe-detail-anchor').attr('href');
        window.location = recipeUrl;
    });
});