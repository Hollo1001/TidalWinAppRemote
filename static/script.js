function sendCommand(command) {
    document.getElementById('hiddenCommand').value = command;
    document.getElementById('commandForm').submit();
}

function sendSearchCommand(action) {
    let query = document.getElementById('searchQuery').value.trim();
    if (query) {
        sendCommand(`${action} ${query}`);
    } else {
        alert('Please enter a query.');
    }
}
