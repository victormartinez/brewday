$(document).ready(function () {
    function updateEmptyFormIDs(element, totalForms) {
        var thisInput = element;
        var currentName = element.attr('name');
        var newName = currentName.replace(/__prefix__/g, totalForms);

        thisInput.attr('name', newName);
        thisInput.attr('id', 'id_' + newName);

        var newFormRow = element.closest('.form-row');
        var newRowId = 'row_id_' + newName;
        newFormRow.attr('id', newRowId);

        newFormRow.addClass('new-parent-row');

        var parentDiv = element.parent();
        parentDiv.attr('id', 'parent_id_' + newName);

        var inputLabel = parentDiv.find('label');
        inputLabel.attr('for', 'id_' + newName);

        return newFormRow;
    };

    $('.plus-new-user-ingredient-form').on('click', function () {
        var formId = '#id_form-TOTAL_FORMS';
        var emptyRow = $('#empty-row').clone();
        emptyRow.attr('id', null);
        emptyRow.removeAttr('hidden');

        var totalForms = parseInt($(formId).val());

        var newFormRow;
        emptyRow.find('input, select').each(function () {
            newFormRow = updateEmptyFormIDs($(this), totalForms);
        });

        $('.form-row:last').after(newFormRow);
        $(formId).val(totalForms + 1);
    });

    $('.uk-grid').on('click', '.minus-new-user-ingredient-form', function () {
        $(this).parent().parent().remove();

        var formId = '#id_form-TOTAL_FORMS';

        var totalForms = parseInt($(formId).val());
        $(formId).val(totalForms - 1);
    });
});