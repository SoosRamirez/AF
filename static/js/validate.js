jQuery.validator.addMethod("alphanumeric", function(value, element) {
    return this.optional(element) || /^\w+$/i.test(value);
}, "Letters, numbers, and underscores only please");
jQuery(document).ready(function($) {
    $('#commentForm').validate({
        rules: {
            comment: {
                required: true,
                minlength: 5,
                alphanumeric: true
            }
        },
        messages: {
            comment: {
                required: "Поле имя обязательно для заполнения",
                minlength: jQuery.validator.format("Длина имени должна быть больше 5-ти символов"),
                alphanumeric: "Letters, numbers, and underscores only please"
            }
        },
        submitHandler: function () {
            form.submit();
        }
    });
});