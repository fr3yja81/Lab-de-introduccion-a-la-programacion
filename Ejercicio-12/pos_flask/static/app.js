let cart = [];
let scannerInterval = null;
const video = document.getElementById('video-scanner');
const canvas = document.getElementById('canvas-scanner');
const log = document.getElementById('log-scanner');

// --- ESCÁNER (Lógica Pyzbar + Flask) ---
function toggleScanner() {
    const container = document.getElementById('reader-container');
    if (container.classList.contains('hidden')) {
        container.classList.remove('hidden');
        startCamera();
    } else {
        container.classList.add('hidden');
        stopCamera();
    }
}

function startCamera() {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
        .then(stream => {
            video.srcObject = stream;
            scannerInterval = setInterval(sendFrame, 600);
        })
        .catch(err => log.innerText = "Error de cámara");
}

function stopCamera() {
    if (video.srcObject) video.srcObject.getTracks().forEach(t => t.stop());
    clearInterval(scannerInterval);
}

function sendFrame() {
    if (video.videoWidth === 0) return;
    const ctx = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    
    const dataUrl = canvas.toDataURL('image/jpeg', 0.6);

    fetch('/scanner', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: dataUrl })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "ok") {
            log.innerText = `Leído: ${data.value}`;
            if (data.producto) {
                if (navigator.vibrate) navigator.vibrate(200);
                addToCart(data.producto.id, data.producto.nombre, data.producto.precio);
                toggleScanner();
            } else {
                log.innerText = "No registrado";
            }
        }
    });
}

// --- CARRITO Y UI ---
function addToCart(id, nombre, precio) {
    const item = cart.find(i => i.id === id);
    if (item) item.qty++; else cart.push({ id, nombre, precio, qty: 1 });
    render();
}

function render() {
    const list = document.getElementById('cart-items');
    list.innerHTML = '';
    let sub = 0;
    cart.forEach(i => {
        sub += i.precio * i.qty;
        list.innerHTML += `<div class="flex justify-between text-xs bg-[#2a2a2a] p-2 rounded">
            <span>${i.nombre} (x${i.qty})</span><span>$${(i.precio * i.qty).toFixed(2)}</span>
        </div>`;
    });
    const total = sub * 1.16;
    document.getElementById('sub-val').innerText = `$${sub.toFixed(2)}`;
    document.getElementById('iva-val').innerText = `$${(sub * 0.16).toFixed(2)}`;
    document.getElementById('total-val').innerText = `$${total.toFixed(2)}`;
    document.getElementById('item-count').innerText = `${cart.length} items`;
}

function processPayment() {
    if (cart.length === 0) return;
    const recList = document.getElementById('receipt-products');
    recList.innerHTML = '';
    let total = 0;
    cart.forEach(i => {
        total += i.precio * i.qty;
        recList.innerHTML += `<div class="flex justify-between"><span>${i.qty}x ${i.nombre}</span><span>$${(i.precio * i.qty).toFixed(2)}</span></div>`;
    });
    document.getElementById('rec-total').innerText = `$${(total * 1.16).toFixed(2)}`;
    document.getElementById('receipt-date').innerText = new Date().toLocaleString();
    document.getElementById('receipt-folio').innerText = "FOLIO: " + Math.floor(Math.random() * 999999);
    document.getElementById('receipt-modal').classList.remove('hidden');
}

function closeReceipt() {
    cart = []; render();
    document.getElementById('receipt-modal').classList.add('hidden');
}

function filterProducts() {
    const val = document.getElementById('main-search').value.toLowerCase();
    document.querySelectorAll('.product-item').forEach(p => {
        const match = p.dataset.name.includes(val) || p.dataset.id.toLowerCase().includes(val);
        p.style.display = match ? 'flex' : 'none';
    });
}

function filterByCategory(cat) {
    document.querySelectorAll('.product-item').forEach(p => {
        p.style.display = (cat === 'Todos' || p.dataset.category === cat) ? 'flex' : 'none';
    });
}