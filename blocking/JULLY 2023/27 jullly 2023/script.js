const items = [];

        function addItem() {
            const name = document.getElementById('name').value;
            const date = document.getElementById('date').value;
            const itemSelect = document.getElementById('item');
            const selectedItem = itemSelect.options[itemSelect.selectedIndex].text;
            const price = parseInt(document.getElementById('price').value);
            const quantity = parseInt(document.getElementById('quantity').value);
            const total = price * quantity;

            if (selectedItem && price && quantity) {
                items.push({
                    item: selectedItem,
                    price,
                    quantity,
                    total,
                });

                updateReceipt(name, date);
            }
            
        }

        function updateReceipt(name, date) {
            const receiptList = document.getElementById('receipt-list');
            receiptList.innerHTML = '';
            document.getElementById('receipt-name').textContent = name;
            document.getElementById('receipt-date').textContent = date;

            let total = 0;
            for (const item of items) {
                total += item.total;
                const listItem = document.createElement('li');
                listItem.textContent = `${item.item} x ${item.quantity} = ${item.total}`;
                receiptList.appendChild(listItem);
            }

            document.getElementById('total').textContent = total;
        }

        function printReceipt() {
            let receiptText = '==== Receipt ====\n';
            const name = document.getElementById('name').value;
            const date = document.getElementById('date').value;

            receiptText += `Name: ${name}\n`;
            receiptText += `Date: ${date}\n`;

            for (const item of items) {
                receiptText += `${item.item} x ${item.quantity} = ${item.total}\n`;
            }

            receiptText += `Total: ${document.getElementById('total').textContent}`;

            alert(receiptText);
        }

        function printReceipt() {
    let receiptText = '==== Receipt ====\n';
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;

    receiptText += `Name: ${name}\n`;
    receiptText += `Date: ${date}\n`;

    for (const item of items) {
        receiptText += `${item.item} x ${item.quantity} = ${item.total}\n`;
    }

    const total = parseFloat(document.getElementById('total').textContent);
    const amountGiven = parseFloat(document.getElementById('amount-given').value);
    const change = amountGiven - total;

    receiptText += `Total: ${total}\n`;
    receiptText += `Amount Given: ${amountGiven}\n`;
    receiptText += `Change: ${change.toFixed(2)}`;

    alert(receiptText);
}
function resetForm() {
    items.length = 0;
    const formInputs = document.querySelectorAll('input, select');
    formInputs.forEach(input => (input.value = ''));
    updateReceipt('', '');
}
function updateReceipt(name, date) {
    const receiptList = document.getElementById('receipt-list');
    receiptList.innerHTML = '';
    document.getElementById('receipt-name').textContent = name;
    document.getElementById('receipt-date').textContent = date;

    let total = 0;
    for (const item of items) {
        total += item.total;
        const listItem = document.createElement('li');
        listItem.textContent = `${item.item} x ${item.quantity} = ${item.total}`;
        receiptList.appendChild(listItem);
    }

    // Check if the total is above 50000 and apply the discount if needed
    const discountAmount = total > 50000 ? total * 0.05 : 0;
    total -= discountAmount;

    document.getElementById('total').textContent = total.toFixed(2);
}