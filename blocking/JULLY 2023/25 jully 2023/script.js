function totalJumlah() {
    const total1 = parseFloat(document.getElementById('total1').value) || 0;
    const total2 = parseFloat(document.getElementById('total2').value) || 0;
    const total3 = parseFloat(document.getElementById('total3').value) || 0;
    const total4 = parseFloat(document.getElementById('total4').value) || 0;
    const total5 = parseFloat(document.getElementById('total5').value) || 0;

    const harga1 = parseFloat(document.getElementById('harga1').value) || 0;
    const harga2 = parseFloat(document.getElementById('harga2').value) || 0;
    const harga3 = parseFloat(document.getElementById('harga3').value) || 0;
    const harga4 = parseFloat(document.getElementById('harga4').value) || 0;
    const harga5 = parseFloat(document.getElementById('harga5').value) || 0;

    const jumlah1 = harga1 * total1;
    const jumlah2 = harga2 * total2;
    const jumlah3 = harga3 * total3;
    const jumlah4 = harga4 * total4;
    const jumlah5 = harga5 * total5;

    const jumlah6 = jumlah1 + jumlah2 + jumlah3 + jumlah4 + jumlah5;
    const jumlah7 = total1 + total2 + total3 + total4 + total5;

    // Menghitung diskon 
        if (jumlahPesanan > 0 && totalHarga > 50000) { 
            diskon = totalHarga * 0.05; 
        }
    const diskon = jumlah6 > 50000 ? jumlah6 * 0.05 : 0;
    const setelahDiskon = jumlah6 - diskon;
    const totalJumlahE = document.getElementById('jumlah');
    const totalDiskonE = document.getElementById('diskon')
    const totalHargaE = document.getElementById('pembayaran');
    totalJumlahE.textContent = jumlah7;
    totalDiskonE.textContent = diskon;
    totalHargaE.textContent = setelahDiskon;


}

document.getElementById('total1').addEventListener('input', totalJumlah);
document.getElementById('total2').addEventListener('input', totalJumlah);
document.getElementById('total3').addEventListener('input', totalJumlah);
document.getElementById('total4').addEventListener('input', totalJumlah);
document.getElementById('total5').addEventListener('input', totalJumlah);

document.getElementById('harga1').addEventListener('input', totalJumlah);
document.getElementById('harga2').addEventListener('input', totalJumlah);
document.getElementById('harga3').addEventListener('input', totalJumlah);
document.getElementById('harga4').addEventListener('input', totalJumlah);
document.getElementById('harga5').addEventListener('input', totalJumlah);