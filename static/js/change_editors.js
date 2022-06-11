function delete_editor(route) {
    // TODO: add a function to request permission to delete editor in template
    let form = document.getElementById('change_editor_form');
    form.action = route
    form.submit();
}

function update_editor(route) {
    let form = document.getElementById('change_editor_form');
    form.action = route
    form.submit();
}

function invite_editor(route) {
    let form = document.getElementById('change_editor_form');
    form.action = route
    form.submit();
}

function ban_editor(route) {
    let form = document.getElementById('change_editor_form');
    form.action = route
    form.submit();
}