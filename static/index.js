window.onload = () => {
    var copy_button = document.getElementById('copy_button');
    var result_output = document.getElementById('result_output');

    copy_button.onclick = () => {
        if (execCopy(result_output)) {
            alert('Copy Completed.');
        } else {
            alert('Copy Failed. You cannot copy in this browser.');
        }
    }

    execCopy = (element) => {
        element.select();
        document.execCommand("copy");
        return true;
    }
}