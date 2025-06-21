document.addEventListener("DOMContentLoaded", function () {
    const deleteTriggers = document.querySelectorAll('[data-bs-target="#confirmDeleteModal"]');
    const confirmBtn = document.getElementById("confirmDeleteButton");
    let targetForm = null;

    deleteTriggers.forEach(button => {
        button.addEventListener("click", function () {
            const formId = this.getAttribute("data-form-id");
            targetForm = document.getElementById(formId);
        });
    });

    confirmBtn.addEventListener("click", function () {
        if (targetForm) {
            targetForm.submit();
        }
    });
});