
import streamlit as st
import random
import html
from datetime import datetime

st.set_page_config(
    page_title="MOON TEA ✨ Pink Bling",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# 💗 PINK BLING THEME — KHÔNG CẦN THƯ VIỆN QR
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700&display=swap');

:root {
    --pink: #ff70b8;
    --hotpink: #ff3e9d;
    --lightpink: #ffe3f1;
    --purple: #c8a2ff;
    --ink: #57334e;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #ffe0f0 0%, transparent 38%),
        radial-gradient(ellipse at 90% 15%, #eadcff 0%, transparent 35%),
        radial-gradient(ellipse at 50% 90%, #fff0f8 0%, transparent 40%),
        #fff9fd;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.stApp::before {
    content: "✦  ✧  ✨  ⋆  ✦  ˚  ✧  ✨  ⋆  ✦  ✧  ˚  ✨";
    position: fixed;
    top: 4%;
    left: 0;
    width: 100%;
    color: #ff72b7;
    font-size: 21px;
    letter-spacing: 30px;
    opacity: .28;
    pointer-events: none;
    z-index: 0;
    animation: sparkle 4s ease-in-out infinite alternate;
}

@keyframes sparkle {
    0% { opacity: .12; transform: translateY(0); }
    100% { opacity: .48; transform: translateY(12px); }
}

@keyframes glitter {
    0%, 100% { filter: drop-shadow(0 0 2px #ffb6dc); }
    50% { filter: drop-shadow(0 0 12px #ff62b0); }
}

h1, h2, h3 {
    color: #a13d79;
}

.hero {
    padding: 30px;
    border-radius: 28px;
    background: linear-gradient(120deg,
        rgba(255,255,255,.96),
        rgba(255,218,238,.95),
        rgba(225,211,255,.96));
    border: 1px solid white;
    box-shadow: 0 12px 40px rgba(218, 92, 165, .18);
    position: relative;
    overflow: hidden;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 5vw, 60px);
    font-weight: 700;
    letter-spacing: 3px;
    background: linear-gradient(90deg, #ff399d, #bb75e8, #ff78b9);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    animation: glitter 3s infinite;
}

.hero-subtitle {
    color: #956486;
    font-size: 16px;
}

.pink-card {
    background: rgba(255,255,255,.88);
    border: 1px solid #ffd4e9;
    padding: 17px;
    border-radius: 22px;
    box-shadow: 0 8px 26px rgba(205, 94, 157, .10);
    margin-bottom: 15px;
}

.price {
    font-size: 22px;
    font-weight: 800;
    color: #ec429a;
}

.pink-pill {
    display: inline-block;
    background: linear-gradient(90deg, #ffd4e9, #e8dcff);
    border-radius: 20px;
    padding: 5px 12px;
    color: #9d4e85;
    font-size: 12px;
    font-weight: 800;
}

div.stButton > button,
div.stFormSubmitButton > button {
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 15px;
    color: white;
    background: linear-gradient(100deg, #ff5ba8, #d58be9);
    font-weight: 800;
    box-shadow: 0 5px 15px rgba(255, 91, 168, .18);
    transition: .2s;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(255, 91, 168, .32);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff0f7, #f0e8ff);
    border-right: 1px solid #f9d4e8;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,.82);
    padding: 12px;
    border: 1px solid #f8d5e8;
    border-radius: 18px;
}

div[data-testid="stImage"] img {
    border-radius: 17px;
}

.receipt {
    background: white;
    border: 2px dashed #ff9acb;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 8px 25px #ffc5e333;
}

.glam-banner {
    background: linear-gradient(120deg, #ffdaed, #f0e1ff, #fff1c9);
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    color: #a13d79;
    border: 1px solid white;
    box-shadow: 0 8px 25px #e5b0d522;
}

div[data-testid="stAlert"] {
    border-radius: 16px;
}

hr {
    border-color: #f6cfe4;
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# MENU ĐỒ UỐNG
# =====================================================

MENU = {
    "Trà sữa": [
        {
            "name": "Trà sữa trân châu đường đen",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=800&q=80",
            "desc": "Béo thơm, trân châu dẻo, đường đen đậm vị.",
            "tag": "BEST SELLER 💗",
        },
        {
            "name": "Trà sữa ô long kem cheese",
            "price": 49000,
            "image": "https://images.unsplash.com/photo-1525385133512-2f3bdd039054?auto=format&fit=crop&w=800&q=80",
            "desc": "Ô long thơm dịu, kem cheese béo mặn.",
            "tag": "SIGNATURE ✨",
        },
        {
            "name": "Trà sữa khoai môn",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=800&q=80",
            "desc": "Khoai môn dịu ngọt, vibe tím pastel.",
            "tag": "PURPLE MOOD 💜",
        },
        {
            "name": "Trà sữa dâu",
            "price": 47000,
            "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=800&q=80",
            "desc": "Dâu thơm ngọt, sữa mịn màng.",
            "tag": "PINK VIBES 🎀",
        },
        {
            "name": "Hồng trà sữa",
            "price": 39000,
            "image": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=800&q=80",
            "desc": "Trà đậm vị, hậu ngọt thanh.",
            "tag": "CLASSIC",
        },
    ],
    "Matcha": [
        {
            "name": "Matcha latte",
            "price": 49000,
            "image": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha xanh thơm, sữa tươi béo nhẹ.",
            "tag": "MATCHA GIRL 🍵",
        },
        {
            "name": "Matcha dâu latte",
            "price": 55000,
            "image": "https://images.unsplash.com/photo-1546173159-315724a31696?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha thanh mát, dâu ngọt dịu.",
            "tag": "PRETTY LAYERS 💗",
        },
        {
            "name": "Matcha kem cheese",
            "price": 55000,
            "image": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha đậm vị, kem cheese béo mặn.",
            "tag": "CREAMY ✨",
        },
    ],
    "Trà trái cây": [
        {
            "name": "Trà đào cam sả",
            "price": 42000,
            "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=800&q=80",
            "desc": "Đào giòn, cam tươi và sả thơm.",
            "tag": "REFRESHING 🍑",
        },
        {
            "name": "Trà vải",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1513558161293-c5b0b182a0e4?auto=format&fit=crop&w=800&q=80",
            "desc": "Vải thơm dịu, ngọt nhẹ nhàng.",
            "tag": "FLORAL 🌸",
        },
    ],
}

TOPPINGS = {
    "Không topping": 0,
    "Trân châu đen": 7000,
    "Trân châu trắng": 7000,
    "Thạch củ năng": 8000,
    "Pudding trứng": 8000,
    "Kem cheese": 12000,
    "Thạch dừa": 7000,
}

VOUCHERS = {
    "MOON10": {"min": 100000, "type": "percent", "value": 10},
    "MATCHA15": {"min": 150000, "type": "percent", "value": 15},
    "FREESHIP": {"min": 80000, "type": "fixed", "value": 15000},
}

PRIZES = [
    {"name": "Giảm 10% đơn hàng", "code": "MOON10",
     "desc": "Áp dụng cho đơn từ 100.000đ."},
    {"name": "Tặng topping trân châu", "code": None,
     "desc": "Báo nhân viên để nhận quà ở lần ghé quán tiếp theo."},
    {"name": "Giảm 15.000đ", "code": "FREESHIP",
     "desc": "Áp dụng cho đơn từ 80.000đ."},
    {"name": "Matcha giảm 15%", "code": "MATCHA15",
     "desc": "Áp dụng cho đơn từ 150.000đ."},
    {"name": "May mắn lần sau 🌷", "code": None,
     "desc": "Cảm ơn bạn đã chơi cùng MOON TEA!"},
]


# =====================================================
# KHỞI TẠO SESSION
# =====================================================

DEFAULTS = {
    "cart": [],
    "page": "Trang chủ",
    "voucher_input": "",
    "voucher": "",
    "discount": 0,
    "paid": False,
    "order_id": "",
    "payment_method": "Tiền mặt",
    "total_paid": 0,
    "customer": "",
    "phone": "",
    "reviews": [],
    "review_done": False,
    "spun": False,
    "prize": None,
    "checkout_ready": False,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# HÀM HỖ TRỢ
# =====================================================

def money(number):
    return f"{int(number):,}".replace(",", ".") + "đ"


def cart_subtotal():
    return sum(
        item["unit_price"] * item["qty"]
        for item in st.session_state.cart
    )


def calculate_discount(amount, code):
    voucher = VOUCHERS.get(code.upper().strip())
    if not voucher or amount < voucher["min"]:
        return 0
    if voucher["type"] == "percent":
        return round(amount * voucher["value"] / 100)
    return min(amount, voucher["value"])


def reset_order():
    st.session_state.cart = []
    st.session_state.voucher_input = ""
    st.session_state.voucher = ""
    st.session_state.discount = 0
    st.session_state.paid = False
    st.session_state.order_id = ""
    st.session_state.payment_method = "Tiền mặt"
    st.session_state.total_paid = 0
    st.session_state.customer = ""
    st.session_state.phone = ""
    st.session_state.review_done = False
    st.session_state.checkout_ready = False


# =====================================================
# SIDEBAR — ĐIỀU HƯỚNG
# =====================================================

with st.sidebar:
    st.markdown(
        "<div style='text-align:center;font-size:52px'>🎀</div>"
        "<h1 style='text-align:center'>MOON TEA</h1>"
        "<p style='text-align:center;color:#ba6a9b'>"
        "✨ PINK BLING CLUB ✨</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    pages = [
        "Trang chủ",
        "Đặt món",
        "Giỏ hàng & Thanh toán",
        "Vòng quay may mắn",
        "Giới thiệu quán",
        "Đánh giá & Phản hồi",
    ]

    st.session_state.page = st.radio(
        "MENU",
        pages,
        index=pages.index(st.session_state.page),
    )

    st.divider()
    st.markdown("### 🛍️ YOUR BAG")
    st.write(
        f"Số lượng: {sum(i['qty'] for i in st.session_state.cart)} món"
    )
    st.markdown(
        f"<div class='price'>{money(cart_subtotal())}</div>",
        unsafe_allow_html=True,
    )

    if st.button("💗 Xem giỏ hàng", use_container_width=True):
        st.session_state.page = "Giỏ hàng & Thanh toán"
        st.rerun()

    st.caption("Made for pretty girls with pretty drinks ✨")


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero">
    <div class="brand">✦ MOON TEA ✦</div>
    <div class="hero-subtitle">
        PINK BLING EDITION · Sip pretty, shine brighter 💗
    </div>
    <br>
    <span class="pink-pill">GLITTER ✨</span>
    <span class="pink-pill">PASTEL 🎀</span>
    <span class="pink-pill">SLAY ALL DAY 💅</span>
</div>
""", unsafe_allow_html=True)

st.write("")


# =====================================================
# TRANG CHỦ
# =====================================================

if st.session_state.page == "Trang chủ":

    left, right = st.columns([1.15, 1])

    with left:
        st.markdown("# Hey bestie! 💗")
        st.markdown("## Hôm nay mình uống gì cho thật slay?")
        st.write(
            "Chào mừng đến MOON TEA — thiên đường trà sữa pastel, "
            "matcha xanh mướt và topping xinh xắn."
        )
        st.write(
            "Mix đồ uống theo gu của bạn, săn voucher và thử vận may "
            "để nhận những món quà siêu cưng."
        )

        if st.button("💅 LET'S ORDER!", type="primary"):
            st.session_state.page = "Đặt món"
            st.rerun()

        st.markdown("#### ✨ Your mood, your drink, your rules.")

    with right:
        st.image(
            "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True,
        )

    st.markdown("## 💖 THE IT-GIRL PICKS")

    featured = [
        MENU["Trà sữa"][0],
        MENU["Matcha"][0],
        MENU["Trà trái cây"][0],
    ]

    cols = st.columns(3)

    for col, item in zip(cols, featured):
        with col:
            st.image(item["image"], use_container_width=True)
            st.markdown(f"**{item['name']}**")
            st.markdown(
                f"<div class='price'>{money(item['price'])}</div>",
                unsafe_allow_html=True,
            )

            if st.button("＋ Add to bag", key="home_" + item["name"]):
                st.session_state.cart.append({
                    "name": item["name"],
                    "qty": 1,
                    "base_price": item["price"],
                    "topping": "Không topping",
                    "topping_price": 0,
                    "sweetness": "50%",
                    "ice": "Có đá",
                    "unit_price": item["price"],
                })
                st.toast("Added to your bag! 💗")
                st.rerun()

    st.markdown("""
    <div class="glam-banner">
        <h2>✨ A LITTLE GLITTER, A LOT OF LOVE ✨</h2>
        Mỗi ly nước là một lý do để bạn tỏa sáng.
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# ĐẶT MÓN
# =====================================================

elif st.session_state.page == "Đặt món":

    st.title("🧋 THE DRINK MENU")
    st.write("Chọn món, mix topping và customize theo gu của bạn!")

    category = st.selectbox("Chọn nhóm đồ uống", list(MENU.keys()))
    products = MENU[category]

    for start in range(0, len(products), 2):
        cols = st.columns(2)

        for col, item in zip(cols, products[start:start + 2]):
            with col:
                st.markdown(
                    "<div class='pink-card'>",
                    unsafe_allow_html=True,
                )

                st.image(item["image"], use_container_width=True)
                st.markdown(f"### {item['name']}")
                st.markdown(
                    f"<span class='pink-pill'>{item['tag']}</span>",
                    unsafe_allow_html=True,
                )
                st.caption(item["desc"])
                st.markdown(
                    f"<div class='price'>{money(item['price'])}</div>",
                    unsafe_allow_html=True,
                )

                with st.form("form_" + item["name"]):
                    qty = st.number_input(
                        "Số lượng ly",
                        min_value=1,
                        max_value=30,
                        value=1,
                        step=1,
                    )

                    topping = st.selectbox(
                        "Topping",
                        list(TOPPINGS.keys()),
                    )

                    sweetness = st.select_slider(
                        "Độ ngọt",
                        options=["0%", "30%", "50%", "70%", "100%"],
                        value="50%",
                    )

                    ice = st.radio(
                        "Lượng đá",
                        ["Có đá", "Ít đá", "Không đá"],
                        horizontal=True,
                    )

                    add = st.form_submit_button(
                        "💗 ADD TO BAG",
                        use_container_width=True,
                    )

                    if add:
                        topping_price = TOPPINGS[topping]

                        st.session_state.cart.append({
                            "name": item["name"],
                            "qty": int(qty),
                            "base_price": item["price"],
                            "topping": topping,
                            "topping_price": topping_price,
                            "sweetness": sweetness,
                            "ice": ice,
                            "unit_price": item["price"] + topping_price,
                        })

                        st.success("Món đã vào giỏ! Slayyy 💅")
                        st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)


# =====================================================
# GIỎ HÀNG & THANH TOÁN
# =====================================================

elif st.session_state.page == "Giỏ hàng & Thanh toán":

    st.title("🛍️ YOUR BAG & CHECKOUT")

    if not st.session_state.cart:
        st.info("Giỏ hàng trống rồi bestie ơi! Chọn món nha 💗")

        if st.button("Đi đến menu"):
            st.session_state.page = "Đặt món"
            st.rerun()

    else:
        for idx, item in enumerate(st.session_state.cart):
            with st.container(border=True):
                c1, c2, c3 = st.columns([4, 1, 1])

                with c1:
                    st.markdown(f"**{item['name']}**")
                    st.caption(
                        f"Topping: {item['topping']} · "
                        f"Độ ngọt: {item['sweetness']} · {item['ice']}"
                    )
                    st.caption(
                        f"{money(item['base_price'])} + "
                        f"{money(item['topping_price'])}/ly topping"
                    )

                with c2:
                    st.write(f"× {item['qty']}")

                with c3:
                    st.markdown(
                        f"**{money(item['unit_price'] * item['qty'])}**"
                    )

                    if st.button("🗑️ Xóa", key=f"delete_{idx}"):
                        st.session_state.cart.pop(idx)
                        st.rerun()

        subtotal = cart_subtotal()

        st.divider()
        st.markdown("## 🎟️ VOUCHER BABE")

        with st.form("voucher_form"):
            code = st.text_input(
                "Nhập mã giảm giá",
                value=st.session_state.voucher_input,
                placeholder="MOON10 / MATCHA15 / FREESHIP",
            ).strip().upper()

            apply = st.form_submit_button("✨ APPLY VOUCHER")

            if apply:
                discount = calculate_discount(subtotal, code)

                if code in VOUCHERS and subtotal >= VOUCHERS[code]["min"]:
                    st.session_state.voucher = code
                    st.session_state.voucher_input = code
                    st.session_state.discount = discount
                    st.success(f"Yasss! Bạn tiết kiệm {money(discount)} 💗")
                else:
                    st.session_state.voucher = ""
                    st.session_state.voucher_input = code
                    st.session_state.discount = 0
                    st.error(
                        "Mã không hợp lệ hoặc đơn hàng chưa đủ giá trị tối thiểu."
                    )

        # Voucher có thể được chọn từ vòng quay
        if st.session_state.voucher in VOUCHERS:
            discount = calculate_discount(
                subtotal,
                st.session_state.voucher,
            )
            if subtotal >= VOUCHERS[st.session_state.voucher]["min"]:
                st.session_state.discount = discount
            else:
                st.session_state.discount = 0

        discount = st.session_state.discount
        total = max(0, subtotal - discount)

        c1, c2, c3 = st.columns(3)
        c1.metric("Tạm tính", money(subtotal))
        c2.metric("Giảm giá", "-" + money(discount))
        c3.metric("TOTAL 💗", money(total))

        st.divider()
        st.markdown("## 💳 CHECKOUT")

        with st.form("checkout_form"):
            customer = st.text_input(
                "Tên khách hàng",
                value=st.session_state.customer,
            )

            phone = st.text_input(
                "Số điện thoại (không bắt buộc)",
                value=st.session_state.phone,
            )

            payment = st.radio(
                "Phương thức thanh toán",
                ["Tiền mặt", "Chuyển khoản / QR"],
                horizontal=True,
            )

            checkout = st.form_submit_button(
                "CONTINUE TO PAYMENT ✨",
                type="primary",
                use_container_width=True,
            )

            if checkout:
                if not customer.strip():
                    st.error("Nhập tên khách hàng trước nha bestie!")
                else:
                    st.session_state.customer = customer.strip()
                    st.session_state.phone = phone.strip()
                    st.session_state.payment_method = payment
                    st.session_state.total_paid = total
                    st.session_state.order_id = (
                        "MT" + datetime.now().strftime("%y%m%d%H%M%S")
                    )
                    st.session_state.checkout_ready = True
                    st.session_state.paid = False
                    st.rerun()

        if (
            st.session_state.checkout_ready
            and not st.session_state.paid
        ):
            st.markdown("### ✨ CONFIRM YOUR ORDER")

            st.write(f"**Mã đơn:** {st.session_state.order_id}")
            st.write(f"**Khách hàng:** {st.session_state.customer}")
            st.write(f"**Tổng tiền:** {money(st.session_state.total_paid)}")

            if st.session_state.payment_method == "Chuyển khoản / QR":
                st.markdown("""
                <div class="glam-banner">
                    <div style="font-size:48px">💳 ✨ 💗</div>
                    <h2>SCAN & SLAY</h2>
                    <p>Phương thức chuyển khoản đã được chọn.</p>
                    <p>Vui lòng sử dụng QR ngân hàng thật của quán
                    hoặc nhập thông tin tài khoản đã được quán cấu hình.</p>
                    <p><b>Chưa có QR ngân hàng trong bản demo này.</b></p>
                </div>
                """, unsafe_allow_html=True)

                st.info(
                    "Không dùng hình minh họa để chuyển tiền. "
                    "Nút xác nhận bên dưới chỉ mô phỏng thanh toán."
                )
            else:
                st.info("Bạn sẽ thanh toán tiền mặt tại quầy.")

            if st.button(
                "💗 XÁC NHẬN THANH TOÁN THÀNH CÔNG",
                type="primary",
                use_container_width=True,
            ):
                st.session_state.paid = True
                st.session_state.review_done = False
                st.session_state.page = "Đánh giá & Phản hồi"
                st.rerun()

        if st.session_state.paid:
            st.divider()

            st.markdown(
                "<div class='receipt'>"
                "<h2 style='text-align:center'>🌙 MOON TEA</h2>"
                "<p style='text-align:center'>YOUR PINK BLING RECEIPT ✨</p>"
                "</div>",
                unsafe_allow_html=True,
            )

            st.write(f"**Mã đơn:** {st.session_state.order_id}")
            st.write(f"**Khách hàng:** {st.session_state.customer}")
            st.write(
                f"**Thanh toán:** {st.session_state.payment_method}"
            )
            st.caption(datetime.now().strftime("%d/%m/%Y %H:%M"))

            for item in st.session_state.cart:
                amount = item["unit_price"] * item["qty"]
                st.write(
                    f"**{item['name']}** × {item['qty']} — {money(amount)}"
                )
                st.caption(
                    f"{item['topping']} · {item['sweetness']} · {item['ice']}"
                )

            st.divider()
            st.write(f"Tạm tính: {money(subtotal)}")
            st.write(f"Giảm giá: -{money(discount)}")
            st.markdown(f"## TOTAL: {money(total)} 💗")

        if st.button("← Tiếp tục chọn món"):
            st.session_state.page = "Đặt món"
            st.rerun()


# =====================================================
# VÒNG QUAY MAY MẮN
# =====================================================

elif st.session_state.page == "Vòng quay may mắn":

    st.title("🎡 THE PINK BLING LUCKY WHEEL")
    st.write("Quay một lần để nhận voucher hoặc quà nhỏ nha bestie!")

    st.markdown("""
    <div class="glam-banner">
        <div style="font-size:60px">💗 ✨ 🎀 ✨ 💗</div>
        <h2>SPIN THE GLAM!</h2>
        <p>May mắn đang chờ bạn phía bên kia ánh kim tuyến.</p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.spun:
        if st.button(
            "✨ SPIN NOW, BABE! ✨",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.prize = random.choice(PRIZES)
            st.session_state.spun = True
            st.rerun()

    else:
        prize = st.session_state.prize

        st.balloons()
        st.success(f"🎉 Bạn nhận được: {prize['name']}")
        st.write(prize["desc"])

        if prize["code"]:
            st.code(prize["code"])

            if st.button("💗 Dùng voucher này"):
                st.session_state.voucher = prize["code"]
                st.session_state.voucher_input = prize["code"]
                st.session_state.discount = 0
                st.session_state.page = "Giỏ hàng & Thanh toán"
                st.rerun()

        if st.button("Quay lại từ đầu"):
            st.session_state.spun = False
            st.session_state.prize = None
            st.rerun()

    st.caption(
        "Vòng quay là tính năng demo. Quà thực tế do quán xác nhận."
    )


# =====================================================
# GIỚI THIỆU QUÁN
# =====================================================

elif st.session_state.page == "Giới thiệu quán":

    st.title("💗 MEET MOON TEA")

    left, right = st.columns(2)

    with left:
        st.image(
            "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True,
        )

    with right:
        st.markdown("## Một chút ánh trăng trong mỗi chiếc ly 🌙")

        st.write("""
        MOON TEA là góc nhỏ dành cho những tâm hồn yêu đồ uống,
        màu pastel và những khoảnh khắc thật xinh.

        Từ trà sữa cổ điển đến matcha thơm dịu, mỗi ly đều được
        thiết kế để bạn tận hưởng hương vị theo cách riêng.
        """)

        st.markdown("### 🎀 OUR PROMISE")
        st.write("✨ Tùy chỉnh độ ngọt và lượng đá.")
        st.write("✨ Nhiều loại topping cho bạn mix.")
        st.write("✨ Không gian và trải nghiệm nhẹ nhàng.")

        st.markdown("### 📍 THÔNG TIN QUÁN")
        st.write("Địa chỉ: 123 Đường Ánh Trăng, TP. Hồ Chí Minh")
        st.write("Giờ mở cửa: 09:00 – 22:00")
        st.write("Hotline: 0900 123 456")

        st.caption(
            "Địa chỉ và số điện thoại là thông tin mẫu. "
            "Hãy thay bằng thông tin thật trước khi sử dụng."
        )

    st.markdown("""
    <div class="glam-banner">
        <h2>THANK YOU FOR LETTING US BE PART OF YOUR DAY 💗</h2>
        Sip slowly. Shine softly. Slay always.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🧋 Đặt món ngay"):
        st.session_state.page = "Đặt món"
        st.rerun()


# =====================================================
# ĐÁNH GIÁ & PHẢN HỒI
# =====================================================

elif st.session_state.page == "Đánh giá & Phản hồi":

    st.title("💌 RATE YOUR EXPERIENCE")
    st.markdown("### Your opinion is the real sparkle! ✨")

    if not st.session_state.paid:
        st.info(
            "Form đánh giá sẽ mở sau khi bạn xác nhận thanh toán."
        )

        if st.button("Đến giỏ hàng"):
            st.session_state.page = "Giỏ hàng & Thanh toán"
            st.rerun()

    else:
        st.success(
            f"Cảm ơn {st.session_state.customer} đã ghé MOON TEA! 💗"
        )

        if not st.session_state.review_done:

            with st.form("review_form"):
                stars = st.select_slider(
                    "Bạn chấm MOON TEA bao nhiêu sao?",
                    options=[1, 2, 3, 4, 5],
                    value=5,
                    format_func=lambda n: "⭐" * n,
                )

                comment = st.text_area(
                    "Lời nhắn cho quán",
                    placeholder=(
                        "Món bạn yêu thích, trải nghiệm của bạn "
                        "hoặc điều chúng mình có thể cải thiện..."
                    ),
                )

                display_name = st.text_input(
                    "Tên hiển thị",
                    value=st.session_state.customer,
                )

                send = st.form_submit_button(
                    "SEND LOVE 💗",
                    type="primary",
                    use_container_width=True,
                )

                if send:
                    st.session_state.reviews.append({
                        "name": display_name.strip() or "Khách MOON TEA",
                        "stars": stars,
                        "comment": comment.strip(),
                        "order": st.session_state.order_id,
                        "time": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    })

                    st.session_state.review_done = True
                    st.rerun()

        else:
            st.success("Đã nhận feedback. Thank you, queen! 👑")

            if st.button("✨ Tạo đơn hàng mới"):
                reset_order()
                st.session_state.page = "Đặt món"
                st.rerun()

    if st.session_state.reviews:
        st.divider()
        st.markdown("## 💬 LOVE NOTES")

        for review in reversed(st.session_state.reviews[-10:]):
            with st.container(border=True):
                st.write(
                    f"**{review['name']}** · {'⭐' * review['stars']}"
                )

                if review["comment"]:
                    st.write(review["comment"])

                st.caption(
                    f"{review['time']} · Đơn {review['order']}"
                )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div style="
    text-align:center;
    color:#bc76a2;
    padding:18px;
    font-weight:700;">
    ✨ MADE WITH LOVE & GLITTER ✨<br>
    MOON TEA · SIP PRETTY, SHINE BRIGHTER 💗
</div>
""", unsafe_allow_html=True)
