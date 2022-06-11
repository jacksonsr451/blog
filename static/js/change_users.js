function delete_user(route) {
    // TODO: add a function to request permission to delete user in template
    let form = document.getElementById('change_user_form');
    form.action = route
    form.submit();
}

function update_user(route) {
    let form = document.getElementById('change_user_form');
    form.action = route
    form.submit();
}

function invite_user(route) {
    let form = document.getElementById('change_user_form');
    form.action = route
    form.submit();
}

function ban_user(route) {
    let form = document.getElementById('change_user_form');
    form.action = route
    form.submit();
}