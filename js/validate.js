$('#commentForm').validate({
        rules: {
            comment: {
                required: true,
                minlength: 5
            }
        },
        messages: {
            comment: {
                required: "Поле имя обязательно для заполнения",
                minlength: jQuery.validator.format("Длина имени должна быть больше 5-ти символов")
            }
        },
        submitHandler: function () {
            form.submit();
        }
    });