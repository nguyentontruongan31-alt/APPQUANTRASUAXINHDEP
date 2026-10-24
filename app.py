
import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Kiều Nữ Quán",
    page_icon="🎀",
    layout="wide"
)

# ===================== GIAO DIỆN PINK OLD MONEY =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffe0ef 0%, transparent 30%),
        radial-gradient(circle at 90% 20%, #f3ddfa 0%, transparent 30%),
        linear-gradient(135deg,#fff8fc,#ffeaf4,#fff9fc);
    color: #79445e;
}
h1,h2,h3 {
    color: #a74777 !important;
    font-family: 'Playfair Display', serif !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#ffe6f1,#f5e8fa);
}
div.stButton > button, div.stFormSubmitButton > button {
    background: linear-gradient(100deg,#ed79ad,#c59bdf);
    color: white;
    border: 1px solid white;
    border-radius: 14px;
    font-weight: bold;
}
div.stButton > button:hover {
    border-color: #d85897;
    color: white;
    box-shadow: 0 0 18px #f6a9d0;
}
.pink-card {
    background: rgba(255,255,255,.82);
    padding: 22px;
    border-radius: 22px;
    border: 1px solid #f5c9df;
    box-shadow: 0 7px 22px #e8b8d333;
    margin-bottom: 15px;
}
.brand {
    font-family: 'Playfair Display',serif;
    font-size: clamp(32px,5vw,58px);
    font-weight: bold;
    letter-spacing: 3px;
    color: #c64f8c;
    text-shadow: 0 0 18px #ffc2e0;
}
.price {
    color: #d14c91;
    font-size: 23px;
    font-weight: bold;
}
.sparkle {
    text-align:center;
    color:#d78caf;
    letter-spacing:10px;
    animation: shine 2s infinite alternate;
}
@keyframes shine {
    from {opacity:.45;text-shadow:0 0 2px #fff}
    to {opacity:1;text-shadow:0 0 15px #ed83bb}
}
</style>
""", unsafe_allow_html=True)

# ===================== MENU =====================
MENU = {
    "Trà sữa": [
        ("Trà Sữa Bá Tước Earl Grey", 29000, "Trà thơm thanh, sữa dịu béo", "🫖"),
        ("Trà Sữa Hoàng Gia Trân Châu", 32000, "Trân châu dẻo, trà đậm vị", "🧋"),
        ("Trà Sữa Tử Tước Khoai Môn", 29000, "Khoai môn tím béo mịn", "💜"),
        ("Hồng Trà Phu Nhân Dâu Tây", 32000, "Dâu ngọt dịu, màu hồng xinh", "🍓"),
        ("Trà Sữa Caramel Điện Hạ", 29000, "Caramel ngọt thơm", "🍮"),
        ("Trà Sữa Chocolate Dạ Hội", 32000, "Chocolate đậm vị", "🍫"),
        ("Ô Long Hoàng Tộc Kem Cheese", 35000, "Ô long thơm và kem cheese", "🧋"),
    ],
    "Matcha": [
        ("Matcha Tiểu Thư Kyoto", 35000, "Matcha thanh khiết", "🍵"),
        ("Matcha Hầu Tước Kem Sữa", 39000, "Matcha và kem sữa", "🍃"),
        ("Matcha Dâu Phu Nhân", 39000, "Matcha kết hợp dâu", "🍓"),
        ("Matcha Đậu Đỏ Ngự Uyển", 35000, "Đậu đỏ bùi thơm", "🍵"),
    ],
    "Trà trái cây": [
        ("Trà Đào Dạ Tiệc Versailles", 29000, "Trà đào thanh mát", "🍑"),
        ("Trà Vải Nữ Hoàng Ngọc Trai", 32000, "Vải thơm dịu", "🍈"),
        ("Trà Dâu Hồng Ngọc", 29000, "Dâu chua ngọt", "🍓"),
        ("Trà Chanh Bá Tước", 22000, "Chanh thanh mát", "🍋"),
    ],
    "Chocolate & Cacao": [
        ("Cacao Báu Vật Hoàng Gia", 29000, "Cacao thơm đậm", "🍫"),
        ("Chocolate Sữa Công Nương", 32000, "Chocolate sữa mềm mượt", "🥛"),
    ],
    "Ăn vặt": [
        ("Khoai Tây Chiên Kim Sắc", 19000, "Khoai tây vàng giòn", "🍟"),
        ("Gà Viên Bá Tước", 25000, "Gà viên chiên giòn", "🍗"),
        ("Phô Mai Que Hoàng Kim", 25000, "Phô mai béo thơm", "🧀"),
        ("Bánh Gạo Công Nương", 29000, "Bánh gạo sốt cay ngọt", "🍢"),
        ("Cá Viên Tiệc Trà", 19000, "Cá viên chiên nóng", "🍡"),
        ("Xúc Xích Quý Tộc", 22000, "Xúc xích vàng thơm", "🌭"),
        ("Há Cảo Ngự Thiện", 29000, "Há cảo mềm thơm", "🥟"),
        ("Waffle Tiểu Thư", 29000, "Bánh waffle thơm bơ", "🧇"),
        ("Brownie Dạ Hội", 25000, "Bánh chocolate mềm ẩm", "🍰"),
        ("Sừng Bò Hoàng Gia", 25000, "Bánh croissant thơm bơ", "🥐"),
    ],
}

TOPPINGS = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Pudding trứng": 7000,
    "Thạch củ năng": 6000,
    "Kem cheese": 9000,
}

VOUCHERS = {
    "KIEUNU10": (80000, 0.10),
    "OLDMONEY": (120000, 0.15),
    "TIENNU": (60000, 10000),
}

# ===================== SESSION =====================
if "cart" not in st.session_state:
    st.session_state.cart = []
if "page" not in st.session_state:
    st.session_state.page = "Trang chủ"
if "spun" not in st.session_state:
    st.session_state.spun = False
if "prize" not in st.session_state:
    st.session_state.prize = None
if "paid" not in st.session_state:
    st.session_state.paid = False
if "reviews" not in st.session_state:
    st.session_state.reviews = []
if "review_done" not in st.session_state:
    st.session_state.review_done = False

def money(n):
    return f"{int(n):,}".replace(",", ".") + "đ"

def total_cart():
    return sum(x["unit"] * x["qty"] for x in st.session_state.cart)

# ===================== THANH ĐIỀU HƯỚNG =====================
with st.sidebar:
    st.markdown("<div style='text-align:center;font-size:48px'>👑</div>",
                unsafe_allow_html=True)
    st.markdown("## KIỀU NỮ QUÁN")
    st.caption("PINK OLD MONEY CAFÉ")
    page = st.radio("DANH MỤC", [
        "Trang chủ",
        "Thực đơn & Đặt món",
        "Giỏ hàng & Thanh toán",
        "Vòng quay may mắn",
        "Về Kiều Nữ Quán",
        "Đánh giá & Phản hồi",
    ])
    st.markdown("---")
    st.write("🛍️ Số món:", sum(x["qty"] for x in st.session_state.cart))
    st.markdown(f"### {money(total_cart())}")

st.markdown("""
<div class="pink-card" style="text-align:center">
    <div class="sparkle">✧ ✦ ♡ ✦ ✧</div>
    <div class="brand">KIỀU NỮ QUÁN</div>
    <div style="letter-spacing:3px">THE AFFORDABLE OLD MONEY CAFÉ</div>
    <p>👑 Thanh lịch quý tộc · Giá bình dân · Ngập tràn sắc hồng 🎀</p>
</div>
""", unsafe_allow_html=True)

# ===================== TRANG CHỦ =====================
if page == "Trang chủ":
    st.title("Kính chào tiểu thư! 🎀")
    st.write(
        "Chào mừng đến Kiều Nữ Quán — nơi phong cách old money "
        "gặp sắc hồng lãng mạn. Thưởng thức món ngon với mức giá "
        "dễ thương từ 19.000đ."
    )
    c1, c2, c3 = st.columns(3)
    for col, category, item in zip(
        [c1, c2, c3],
        ["Trà sữa", "Matcha", "Ăn vặt"],
        [MENU["Trà sữa"][0], MENU["Matcha"][0], MENU["Ăn vặt"][0]]
    ):
        with col:
            name, price, desc, emoji = item
            st.markdown("<div class='pink-card'>", unsafe_allow_html=True)
            st.markdown(f"## {emoji}")
            st.subheader(name)
            st.caption(desc)
            st.markdown(f"<div class='price'>{money(price)}</div>",
                        unsafe_allow_html=True)
            if st.button("＋ Thêm vào giỏ", key="home_" + name):
                st.session_state.cart.append({
                    "name": name, "qty": 1, "unit": price,
                    "topping": "Không topping", "sweet": "50%", "ice": "Có đá"
                })
                st.toast("Đã thêm món vào giỏ 🎀")
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# ===================== THỰC ĐƠN =====================
elif page == "Thực đơn & Đặt món":
    st.title("Thực đơn hoàng gia ✦")
    category = st.selectbox("Chọn danh mục", list(MENU.keys()))
    products = MENU[category]

    for start in range(0, len(products), 2):
        cols = st.columns(2)
        for col, item in zip(cols, products[start:start + 2]):
            name, price, desc, emoji = item
            with col:
                st.markdown("<div class='pink-card'>", unsafe_allow_html=True)
                st.markdown(f"## {emoji} {name}")
                st.write(desc)
                st.markdown(f"<div class='price'>{money(price)}</div>",
                            unsafe_allow_html=True)
                with st.form("form_" + name):
                    qty = st.number_input("Số lượng", 1, 20, 1, key="q_" + name)
                    if category == "Ăn vặt":
                        topping = "Không topping"
                        sweet = "Không áp dụng"
                        ice = "Không áp dụng"
                    else:
                        topping = st.selectbox(
                            "Topping", list(TOPPINGS.keys()), key="t_" + name
                        )
                        sweet = st.select_slider(
                            "Độ ngọt",
                            options=["0%", "30%", "50%", "70%", "100%"],
                            value="50%", key="s_" + name
                        )
                        ice = st.radio(
                            "Đá", ["Có đá", "Ít đá", "Không đá"],
                            horizontal=True, key="i_" + name
                        )
                    submitted = st.form_submit_button("🎀 Thêm vào giỏ")
                    if submitted:
                        unit = price + TOPPINGS[topping]
                        st.session_state.cart.append({
                            "name": name, "qty": int(qty), "unit": unit,
                            "topping": topping, "sweet": sweet, "ice": ice
                        })
                        st.success("Đã thêm món vào giỏ!")
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

# ===================== GIỎ HÀNG / THANH TOÁN =====================
elif page == "Giỏ hàng & Thanh toán":
    st.title("Giỏ hàng & Thanh toán 🛍️")
    if not st.session_state.cart:
        st.info("Giỏ hàng đang trống. Hãy chọn món trong thực đơn.")
    else:
        for i, item in enumerate(st.session_state.cart):
            a, b, c = st.columns([5, 1, 1])
            with a:
                st.write("**" + item["name"] + "**")
                st.caption(
                    f"Topping: {item['topping']} · Độ ngọt: "
                    f"{item['sweet']} · {item['ice']}"
                )
            with b:
                st.write(f"× {item['qty']}")
            with c:
                st.write(money(item["unit"] * item["qty"]))
                if st.button("Xóa", key=f"del_{i}"):
                    st.session_state.cart.pop(i)
                    st.rerun()

        subtotal = total_cart()
        st.markdown("---")
        st.subheader("🎟️ Voucher")
        voucher = st.text_input(
            "Nhập mã voucher",
            placeholder="KIEUNU10 / OLDMONEY / TIENNU"
        ).strip().upper()

        discount = 0
        if voucher in VOUCHERS:
            minimum, value = VOUCHERS[voucher]
            if subtotal >= minimum:
                if value < 1:
                    discount = int(subtotal * value)
                else:
                    discount = int(value)
                st.success(f"Đã áp dụng voucher: giảm {money(discount)}")
            else:
                st.warning(f"Đơn cần đạt {money(minimum)} để dùng mã này.")

        final_total = max(0, subtotal - discount)
        a, b, c = st.columns(3)
        a.metric("Tạm tính", money(subtotal))
        b.metric("Giảm giá", "-" + money(discount))
        c.metric("Tổng cộng", money(final_total))

        st.subheader("Thông tin thanh toán")
        customer = st.text_input("Tên khách hàng")
        payment = st.radio(
            "Phương thức thanh toán",
            ["Tiền mặt tại quầy", "Chuyển khoản / QR"],
            horizontal=True
        )

        if payment == "Chuyển khoản / QR":
            st.info(
                "Đính kèm hoặc hiển thị mã QR ngân hàng thật của quán tại đây. "
                "Ứng dụng mẫu chưa xác minh giao dịch ngân hàng."
            )

        if st.button("Xác nhận đơn hàng 🎀", type="primary"):
            if not customer.strip():
                st.error("Chị vui lòng nhập tên khách hàng.")
            else:
                st.session_state.customer = customer.strip()
                st.session_state.order_id = "KN" + datetime.now().strftime("%y%m%d%H%M%S")
                st.session_state.order_total = final_total
                st.session_state.order_discount = discount
                st.session_state.order_subtotal = subtotal
                st.session_state.order_payment = payment
                st.session_state.paid = True
                st.session_state.review_done = False
                st.session_state.order_voucher = voucher
                st.success("Đơn hàng đã được xác nhận! 🎉")

        if st.session_state.paid:
            st.markdown("---")
            st.markdown("<div class='pink-card'>", unsafe_allow_html=True)
            st.markdown("## 👑 KIỀU NỮ QUÁN")
            st.markdown("### HÓA ĐƠN THANH TOÁN")
            st.write("Mã đơn:", st.session_state.order_id)
            st.write("Khách hàng:", st.session_state.customer)
            st.write("Thời gian:", datetime.now().strftime("%d/%m/%Y %H:%M"))
            for item in st.session_state.cart:
                st.write(
                    f"{item['name']} × {item['qty']}: "
                    f"{money(item['unit'] * item['qty'])}"
                )
            st.write("Tạm tính:", money(st.session_state.order_subtotal))
            st.write("Giảm giá:", "-" + money(st.session_state.order_discount))
            st.markdown(f"## Tổng cộng: {money(st.session_state.order_total)}")
            st.write("Phương thức:", st.session_state.order_payment)
            st.markdown("</div>", unsafe_allow_html=True)
            st.caption("Lưu ý: xác nhận đơn trong bản mẫu chưa phải xác minh tiền đã vào ngân hàng.")

# ===================== VÒNG QUAY MAY MẮN =====================
elif page == "Vòng quay may mắn":
    st.title("🎡 Vòng quay may mắn")
    st.markdown(
        "<div class='pink-card' style='text-align:center'>"
        "<div style='font-size:55px'>🎀 ✧ 👑 ✧ 🎀</div>"
        "<h2>THE ROYAL LUCKY SPIN</h2>"
        "Thử vận may để nhận quà dành riêng cho tiểu thư!"
        "</div>", unsafe_allow_html=True
    )
    if st.button("QUAY NGAY ✨", type="primary"):
        st.session_state.prize = random.choice([
            ("Giảm 10% đơn hàng", "KIEUNU10"),
            ("Giảm 15% đơn hàng", "OLDMONEY"),
            ("Giảm ngay 10.000đ", "TIENNU"),
            ("Tặng một topping", "TOPPING"),
            ("Chúc may mắn lần sau", "LUCKY")
        ])
        st.session_state.spun = True

    if st.session_state.spun and st.session_state.prize:
        title, code = st.session_state.prize
        st.balloons()
        st.success("🎉 Phần thưởng: " + title)
        if code not in ["TOPPING", "LUCKY"]:
            st.code(code)
            if st.button("Dùng voucher trong giỏ"):
                st.session_state.page = "Giỏ hàng & Thanh toán"
                st.rerun()
        elif code == "TOPPING":
            st.write("Hãy cho nhân viên xem kết quả để nhận topping theo điều kiện quán.")
        else:
            st.write("Cảm ơn tiểu thư đã tham gia! 💗")

# ===================== GIỚI THIỆU =====================
elif page == "Về Kiều Nữ Quán":
    st.title("Về Kiều Nữ Quán ♡")
    st.markdown("<div class='pink-card'>", unsafe_allow_html=True)
    st.markdown("## Thanh lịch không nhất thiết phải đắt đỏ.")
    st.write(
        "Kiều Nữ Quán lấy cảm hứng từ phong cách old money: "
        "cổ điển, tinh tế và nhẹ nhàng. Chúng mình tin rằng ai cũng "
        "xứng đáng tận hưởng một chút xa hoa trong đời thường."
    )
    st.markdown("### ✦ Tôn chỉ của quán")
    st.write("🎀 Thức uống dễ chọn, dễ yêu.")
    st.write("✦ Giá bình dân, niêm yết rõ ràng.")
    st.write("♡ Có đồ ăn vặt để thưởng thức cùng bạn bè.")
    st.write("👑 Sắc hồng thanh lịch và trải nghiệm thân thiện.")
    st.markdown("### Thông tin")
    st.write("Địa chỉ: cập nhật địa chỉ thật của quán.")
    st.write("Giờ mở cửa: cập nhật giờ hoạt động.")
    st.write("Hotline: cập nhật số điện thoại.")
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== ĐÁNH GIÁ =====================
elif page == "Đánh giá & Phản hồi":
    st.title("Đánh giá & Phản hồi 💌")
    if not st.session_state.get("paid", False):
        st.info("Sau khi xác nhận đơn hàng, bạn có thể đánh giá trải nghiệm.")
    elif st.session_state.get("review_done", False):
        st.success("Cảm ơn tiểu thư đã gửi đánh giá! 💗")
        if st.button("Tạo đơn hàng mới"):
            st.session_state.cart = []
            st.session_state.paid = False
            st.session_state.review_done = False
            st.session_state.spun = False
            st.session_state.page = "Thực đơn & Đặt món"
            st.rerun()
    else:
        st.write(f"Cảm ơn {st.session_state.get('customer', 'tiểu thư')} đã ghé quán!")
        with st.form("review_form"):
            stars = st.select_slider(
                "Bạn chấm quán bao nhiêu sao?",
                options=[1, 2, 3, 4, 5],
                value=5,
                format_func=lambda x: "⭐" * x
            )
            message = st.text_area(
                "Lời nhắn cho quán",
                placeholder="Món yêu thích hoặc góp ý của bạn..."
            )
            name = st.text_input(
                "Tên hiển thị",
                value=st.session_state.get("customer", "")
            )
            submit = st.form_submit_button("Gửi đánh giá 💗")
            if submit:
                st.session_state.reviews.append({
                    "name": name or "Khách hàng",
                    "stars": stars,
                    "message": message,
                    "time": datetime.now().strftime("%d/%m/%Y %H:%M")
                })
                st.session_state.review_done = True
                st.rerun()

    if st.session_state.reviews:
        st.markdown("---")
        st.subheader("Lời nhắn từ khách hàng")
        for review in reversed(st.session_state.reviews[-10:]):
            st.markdown("<div class='pink-card'>", unsafe_allow_html=True)
            st.write(f"**{review['name']}** · {'⭐' * review['stars']}")
            st.write(review["message"] or "Không có lời nhắn.")
            st.caption(review["time"])
            st.markdown("</div>", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("---")
st.markdown(
    "<div class='sparkle'>✧ ♡ 👑 ♡ ✧</div>"
    "<p style='text-align:center;color:#b57b99'>"
    "<b>KIỀU NỮ QUÁN</b><br>"
    "PINK OLD MONEY CAFÉ · Everyday luxury, everyday you."
    "</p>",
    unsafe_allow_html=True
)
