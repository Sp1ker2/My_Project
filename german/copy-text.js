function copyToClipboard() {
const text = document.getElementById("copyText").textContent;
navigator.clipboard.writeText(text)
    .then(() => {
    alert("Текст скопирован в буфер обмена!");
    })
    .catch(err => {
    console.error("Ошибка при копировании текста: ", err);
    });
}
