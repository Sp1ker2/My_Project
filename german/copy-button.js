function copyToClipboard() {
    // Находим элемент с текстом
    const copyText = document.getElementById("copyText").innerText;
    
    // Создаем временное текстовое поле для копирования
    const tempInput = document.createElement("input");
    document.body.appendChild(tempInput);
    tempInput.value = copyText;
    tempInput.select();
    tempInput.setSelectionRange(0, 99999); // Для мобильных устройств
    document.execCommand("copy");
    
    // Удаляем временное поле
    document.body.removeChild(tempInput);

    // Опционально: Уведомление об успешном копировании
    alert("Текст скопирован: " + copyText);
}