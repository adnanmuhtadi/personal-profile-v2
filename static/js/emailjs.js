// EMAIL JS
function validate() {
    let name = document.querySelector(".name")
    let email = document.querySelector(".email")
    let msg = document.querySelector(".message")
    let sendBtn = document.querySelector(".send-btn")

    sendBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if (name.value == "" || email.value == "" || msg.value == ""){
            emptyerror();
        } else {
            sendmail(name.value, email.value, msg.value);
            success();
        }
    })
}
validate();

function sendmail(name, email, msg) {
    emailjs.send("personal-gmail", "template_ko45qmy", {
        from_name: email,
        to_name: name,
        message: msg,
    });
}

function emptyerror() {
    swal({
        title: "Oh No....",
        text: "Fields cannot be empty!",
        icon: "error",
    });
}

function success() {
    swal({
        title: "Email was sent successfully",
        text: "Will reply within 24 hours",
        icon: "success",
    });
    document.getElementById("contact-form").reset();
}