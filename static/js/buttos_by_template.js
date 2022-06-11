function button_delete(form_id, route) {
    // TODO: add a function to request permission to delete editor in template
    let form = document.getElementById(form_id);
    form.action = route
    form.submit();
}

function button_update(form_id, route) {
    let form = document.getElementById(form_id);
    form.action = route
    form.submit();
}

function button_invite(form_id, route) {
    let form = document.getElementById(form_id);
    form.action = route
    form.submit();
}

function button_ban(form_id, route) {
    let form = document.getElementById(form_id);
    form.action = route
    form.submit();
}