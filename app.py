
import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Kiều Nữ Quán",
    page_icon="🌸",
    layout="wide"
)

# ==================== GIAO DIỆN ====================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #fff5fa, #ffe1ed, #fff9fc);
    color: #713c54;
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #873d60 !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe0ec, #fff8fb);
}
div.stButton > button {
    border-radius: 14px;
    border: 1px solid #e8a1bb;
    background: linear-gradient(135deg, white, #ffdce9);
    color: #843e60;
    font-weight: 700;
}
div.stButton > button:hover {
    border-color: #c85c87;
    color: #a63d6b;
}
.card {
    padding: 20px;
    border: 1px solid #f0bfd0;
    border-radius: 20px;
    background: rgba(255,255,255,.8);
    margin-bottom: 12px;
}
.hero {
    padding: 32px;
    border-radius: 25px;
    border: 1px solid #f0bfd0;
    background: linear-gradient(120deg, #fff, #ffdeeb);
}
</style>
""", unsafe_allow_html=True)


# ==================== THỰC ĐƠN ====================

PRODUCTS = [
    ("t01", "Hồng Trà Bá Tước", "Trà sữa", 29000, "🫖", "Trà đen thơm dịu, sữa béo nhẹ"),
    ("t02", "Ô Long Tiểu Thư", "Trà sữa", 32000, "🍵", "Ô long rang thơm"),
    ("t03", "Trân Châu Hoàng Gia", "Trà sữa", 35000, "🧋", "Trà sữa truyền thống"),
    ("t04", "Matcha Quý Cô", "Trà sữa", 35000, "🍵", "Matcha thơm xanh"),
    ("t05", "Kho Báu Hồng Ngọc", "Trà sữa", 36000, "🍓", "Trà sữa dâu"),
    ("t06", "Socola Nàng Thơ", "Trà sữa", 35000, "🍫", "Socola đậm vị"),
    ("t07", "Tiramisu Công Tước", "Trà sữa", 39000, "🍰", "Cà phê và kem tiramisu"),

    ("f01", "Đào Hồng Phu Nhân", "Trà trái cây", 30000, "🍑", "Trà đào thanh mát"),
    ("f02", "Vải Ngọc Quý", "Trà trái cây", 32000, "🍈", "Trà vải thơm dịu"),
    ("f03", "Dâu Tây Tiểu Thư", "Trà trái cây", 35000, "🍓", "Dâu chua ngọt"),
    ("f04", "Chanh Dây Quý Tộc", "Trà trái cây", 29000, "🍋", "Chanh dây tươi mát"),
    ("f05", "Nhiệt Đới Thượng Uyển", "Trà trái cây", 33000, "🥭", "Trái cây nhiệt đới"),

    ("c01", "Espresso Bá Tước", "Cà phê", 25000, "☕", "Cà phê đậm thơm"),
    ("c02", "Bạc Xỉu Tiểu Thư", "Cà phê", 28000, "🥛", "Sữa nhiều, cà phê dịu"),
    ("c03", "Latte Phu Nhân", "Cà phê", 35000, "☕", "Espresso và sữa"),
    ("c04", "Cà Phê Muối Hoàng Gia", "Cà phê", 35000, "🧂", "Kem muối béo nhẹ"),

    ("b01", "Bánh Mousse Hoa Hồng", "Bánh & ăn vặt", 32000, "🍰", "Mousse mềm mịn"),
    ("b02", "Croissant Quý Cô", "Bánh & ăn vặt", 25000, "🥐", "Bánh sừng bò thơm bơ"),
    ("b03", "Tiramisu Hoàng Gia", "Bánh & ăn vặt", 35000, "🍮", "Bánh cacao và kem"),
    ("b04", "Khoai Tây Lắc Truffle", "Bánh & ăn vặt", 29000, "🍟", "Khoai tây giòn"),
    ("b05", "Gà Popcorn Tiểu Thư", "Bánh & ăn vặt", 35000, "🍗", "Gà viên giòn"),
    ("b06", "Xúc Xích Hoàng Gia", "Bánh & ăn vặt", 22000, "🌭", "Xúc xích thơm ngon"),
    ("b07", "Phô Mai Que Quý Tộc", "Bánh & ăn vặt", 25000, "🧀", "Phô mai kéo sợi"),
    ("b08", "Bánh Tráng Tiểu Thư", "Bánh & ăn vặt", 20000, "🌶️", "Bánh tráng trộn"),

    ("o01", "Sữa Chua Ngọc Trai", "Khác", 25000, "🥣", "Sữa chua mềm mịn"),
    ("o02", "Soda Hồng Pha Lê", "Khác", 28000, "🥤", "Soda dâu sủi bọt"),
]

TOPPINGS = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
}

VOUCHERS = {
    "KIEUNU10": 0.10,
    "OLDMONEY": 0.15,
    "TIENNU": 0.05,
}


# ==================== HÀM DÙNG CHUNG ====================

def money(amount):
    return f"{int(amount):,}".replace(",", ".") + "đ"


def cart_total(cart):
    """Đọc được cả khóa unit/price và qty/quantity."""
    total = 0

    for item in cart:
        price = item.get("unit", item.get("price", 0))
        quantity = item.get("qty", item.get("quantity", 1))

        try:
            total += int(price) * int(quantity)
        except (ValueError, TypeError):
            continue

    return total


def normalize_cart():
    """Chuẩn hóa giỏ hàng cũ nếu còn dữ liệu từ phiên trước."""
    normalized = []

    for item in st.session_state.cart:
        if not isinstance(item, dict):
            continue

        price = item.get("unit", item.get("price", 0))
        quantity = item.get("qty", item.get("quantity", 1))

        try:
            price = int(price)
            quantity = max(1, int(quantity))
        except (ValueError, TypeError):
            continue

        item["unit"] = price
        item["price"] = price
        item["qty"] = quantity
        item["quantity"] = quantity
        normalized.append(item)

    st.session_state.cart = normalized


DEFAULTS = {
    "cart": [],
    "voucher": "",
    "discount_rate": 0.0,
    "reviews": [],
    "last_order": None,
    "spin_result": None,
    "order_number": 1,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

normalize_cart()


def add_product(product, quantity, topping, sweetness, ice, note):
    product_id, name, category, price, emoji, description = product
    unit_price = int(price) + TOPPINGS[topping]

    st.session_state.cart.append({
        "id": product_id,
        "name": name,
        "category": category,
        "unit": unit_price,
        "price": unit_price,
        "qty": int(quantity),
        "quantity": int(quantity),
        "topping": topping,
        "sweetness": sweetness,
        "ice": ice,
        "note": note.strip(),
    })

    st.toast(f"Đã thêm {name} vào giỏ hàng!", icon="🌸")


def show_product(product, prefix):
    product_id, name, category, price, emoji, description = product

    with st.container(border=True):
        st.markdown(f"## {emoji} {name}")
        st.caption(description)
        st.markdown(f"**{money(price)}**")

        with st.expander("Tùy chỉnh món ✨"):
            quantity = st.number_input(
                "Số lượng", 1, 20, 1,
                key=f"{prefix}_{product_id}_qty"
            )
            topping = st.selectbox(
                "Topping",
                list(TOPPINGS.keys()),
                key=f"{prefix}_{product_id}_topping"
            )

            col1, col2 = st.columns(2)

            with col1:
                sweetness = st.selectbox(
                    "Đường",
                    ["0%", "30%", "50%", "70%", "100%"],
                    index=2,
                    key=f"{prefix}_{product_id}_sweet"
                )

            with col2:
                ice = st.selectbox(
                    "Đá",
                    ["Không đá", "Ít đá", "Bình thường", "Nhiều đá"],
                    index=1,
                    key=f"{prefix}_{product_id}_ice"
                )

            note = st.text_input(
                "Ghi chú",
                key=f"{prefix}_{product_id}_note"
            )

            final_price = price + TOPPINGS[topping]

            if st.button(
                f"Thêm vào giỏ · {money(final_price)}",
                key=f"{prefix}_{product_id}_add",
                use_container_width=True
            ):
                add_product(
                    product, quantity, topping, sweetness, ice, note
                )


# ==================== MENU ĐIỀU HƯỚNG ====================

with st.sidebar:
    st.markdown("<div style='text-align:center;font-size:3rem'>🌸</div>",
                unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center'>Kiều Nữ Quán</h2>",
                unsafe_allow_html=True)
    st.caption("Tea • Cake • Little Luxury")
    st.divider()

    page = st.radio(
        "Khám phá",
        [
            "Trang chủ",
            "Thực đơn",
            "Giỏ hàng & thanh toán",
            "Vòng quay may mắn",
            "Về chúng mình",
            "Đánh giá",
        ]
    )

    st.divider()
    st.markdown(
        f"🛍️ **{sum(x['qty'] for x in st.session_state.cart)} món** trong giỏ"
    )
    st.caption("Một chút ngọt ngào, một chút kiêu sa.")


# ==================== TRANG CHỦ ====================

if page == "Trang chủ":
    st.markdown("""
    <div class="hero">
        <p>✦ A LITTLE LUXURY, EVERY DAY ✦</p>
        <h1 style="font-size:3.2rem">Kiều Nữ Quán</h1>
        <p>Chốn dừng chân ngọt ngào dành cho những tâm hồn yêu cái đẹp.</p>
        <p>🎀 Giá từ 20.000đ · 🧋 Trà & cà phê · 🍰 Bánh và ăn vặt</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🌷 Món được yêu thích")

    featured = [PRODUCTS[2], PRODUCTS[7], PRODUCTS[16]]
    columns = st.columns(3)

    for column, product in zip(columns, featured):
        with column:
            st.markdown(
                f"<div class='card'><div style='font-size:2.5rem'>{product[4]}</div>"
                f"<h3>{product[1]}</h3><p>{product[5]}</p>"
                f"<b>{money(product[3])}</b></div>",
                unsafe_allow_html=True
            )

    st.info("🎟️ Nhập mã KIEUNU10 ở trang thanh toán để giảm 10%.")


# ==================== THỰC ĐƠN ====================

elif page == "Thực đơn":
    st.title("Thực đơn quý cô 🌷")
    st.caption("Tên gọi kiêu sa, giá cả thân thương.")

    categories = ["Tất cả"] + list(dict.fromkeys(p[2] for p in PRODUCTS))
    selected_category = st.selectbox("Danh mục", categories)
    keyword = st.text_input("🔎 Tìm món theo tên")

    filtered = [
        p for p in PRODUCTS
        if (selected_category == "Tất cả" or p[2] == selected_category)
        and keyword.lower() in p[1].lower()
    ]

    if not filtered:
        st.warning("Không tìm thấy món phù hợp.")
    else:
        for start in range(0, len(filtered), 2):
            columns = st.columns(2)

            for column, product in zip(columns, filtered[start:start + 2]):
                with column:
                    show_product(product, "menu")


# ==================== GIỎ HÀNG ====================

elif page == "Giỏ hàng & thanh toán":
    st.title("Giỏ hàng & thanh toán 🛍️")

    if not st.session_state.cart:
        st.info("Giỏ hàng đang trống. Qua thực đơn chọn món nhé 🌸")

    else:
        for index, item in enumerate(list(st.session_state.cart)):
            unit = int(item.get("unit", item.get("price", 0)))
            quantity = int(item.get("qty", item.get("quantity", 1)))

            with st.container(border=True):
                col1, col2, col3 = st.columns([4, 2, 1])

                with col1:
                    st.markdown(f"**{item['name']}**")
                    st.caption(
                        f"{item.get('topping', 'Không topping')} · "
                        f"Đường {item.get('sweetness', '—')} · "
                        f"{item.get('ice', '—')}"
                    )
                    if item.get("note"):
                        st.caption(f"Ghi chú: {item['note']}")

                with col2:
                    st.write(f"{money(unit)} × {quantity}")
                    st.write(f"**{money(unit * quantity)}**")

                with col3:
                    if st.button("🗑️", key=f"delete_{index}"):
                        st.session_state.cart.pop(index)
                        st.rerun()

        subtotal = cart_total(st.session_state.cart)
        st.markdown(f"### Tạm tính: {money(subtotal)}")

        voucher = st.text_input(
            "🎟️ Mã giảm giá",
            value=st.session_state.voucher,
            placeholder="KIEUNU10 / OLDMONEY / TIENNU"
        ).strip().upper()

        if st.button("Áp dụng voucher"):
            st.session_state.voucher = voucher

            if voucher in VOUCHERS:
                st.session_state.discount_rate = VOUCHERS[voucher]
                st.success(
                    f"Đã áp dụng mã giảm {int(VOUCHERS[voucher] * 100)}%!"
                )
            else:
                st.session_state.discount_rate = 0.0
                st.error("Mã không hợp lệ.")

        discount_rate = st.session_state.discount_rate
        discount = int(subtotal * discount_rate)
        total = subtotal - discount

        if discount:
            st.write(f"Giảm giá: **−{money(discount)}**")

        st.markdown(f"## Tổng thanh toán: {money(total)}")
        st.divider()

        payment = st.radio(
            "Phương thức thanh toán",
            ["Tiền mặt khi nhận hàng", "Chuyển khoản (demo)"]
        )

        if payment == "Chuyển khoản (demo)":
            st.warning(
                "Bản demo chưa kết nối ngân hàng, chưa tạo QR thanh toán "
                "và chưa xác minh giao dịch."
            )

        with st.form("checkout_form"):
            customer = st.text_input("Tên người nhận")
            phone = st.text_input("Số điện thoại")
            address = st.text_input("Địa chỉ giao hàng")
            submit_order = st.form_submit_button(
                "Xác nhận đặt hàng",
                use_container_width=True
            )

        if submit_order:
            if not customer.strip() or not phone.strip() or not address.strip():
                st.error("Vui lòng nhập đầy đủ tên, số điện thoại và địa chỉ.")
            else:
                order = {
                    "number": st.session_state.order_number,
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "customer": customer.strip(),
                    "phone": phone.strip(),
                    "address": address.strip(),
                    "payment": payment,
                    "items": [dict(item) for item in st.session_state.cart],
                    "subtotal": subtotal,
                    "discount": discount,
                    "total": total,
                }

                st.session_state.last_order = order
                st.session_state.order_number += 1
                st.session_state.cart = []
                st.session_state.voucher = ""
                st.session_state.discount_rate = 0.0

                st.success(
                    f"Đặt hàng thành công! Mã đơn #{order['number']}. "
                    "Đây là bản demo, đơn chưa được gửi tới đơn vị giao hàng."
                )
                st.rerun()


# ==================== VÒNG QUAY ====================

elif page == "Vòng quay may mắn":
    st.title("Vòng quay may mắn 🎡")
    st.markdown(
        "<div class='hero'><h2>Lady Luck Club ✨</h2>"
        "<p>Một vòng quay nhỏ, một niềm vui xinh.</p></div>",
        unsafe_allow_html=True
    )

    prizes = [
        ("Giảm 5%", "TIENNU"),
        ("Giảm 10%", "KIEUNU10"),
        ("Giảm 15%", "OLDMONEY"),
        ("Chúc em may mắn lần sau", None),
    ]

    if st.button("Quay ngay nào 💖", use_container_width=True):
        st.session_state.spin_result = random.choice(prizes)

    if st.session_state.spin_result:
        prize, code = st.session_state.spin_result
        st.subheader(f"🎉 {prize}")

        if code:
            st.code(code)
            if st.button("Dùng mã ở thanh toán"):
                st.session_state.voucher = code
                st.session_state.discount_rate = VOUCHERS[code]
                st.info("Đã lưu mã. Em mở trang Giỏ hàng & thanh toán nhé.")


# ==================== GIỚI THIỆU ====================

elif page == "Về chúng mình":
    st.title("Về Kiều Nữ Quán 🌸")

    st.markdown("""
    <div class="hero">
        <h2>Vẻ đẹp nằm trong những điều nhỏ bé</h2>
        <p>Kiều Nữ Quán được tạo nên từ ý tưởng: ai cũng xứng đáng có
        một chút xa hoa trong ngày thường.</p>
        <p>Những cái tên mang hơi thở quý tộc, mức giá vẫn gần gũi
        để niềm vui không cần đắt đỏ.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Thông tin cửa hàng")
    st.write("📍 Địa chỉ: cập nhật địa chỉ cửa hàng tại đây")
    st.write("🕘 Giờ mở cửa: 09:00 – 22:00")
    st.write("☎️ Hotline: cập nhật số điện thoại tại đây")


# ==================== ĐÁNH GIÁ & HÓA ĐƠN ====================

elif page == "Đánh giá":
    st.title("Gửi lời thương đến Kiều Nữ Quán 💌")

    order = st.session_state.last_order

    if order:
        st.success(
            f"Đơn gần nhất #{order['number']} · "
            f"Tổng tiền {money(order['total'])}"
        )

        with st.expander("Xem hóa đơn"):
            st.write(f"Khách hàng: {order['customer']}")
            st.write(f"Ngày đặt: {order['date']}")
            st.write(f"Điện thoại: {order['phone']}")
            st.write(f"Địa chỉ: {order['address']}")
            st.write(f"Thanh toán: {order['payment']}")

            for item in order["items"]:
                unit = item.get("unit", item.get("price", 0))
                quantity = item.get("qty", item.get("quantity", 1))
                st.write(
                    f"- {item['name']} × {quantity}: "
                    f"{money(unit * quantity)}"
                )

            st.write(f"Tạm tính: {money(order['subtotal'])}")
            st.write(f"Giảm giá: {money(order['discount'])}")
            st.markdown(f"### Tổng cộng: {money(order['total'])}")

    with st.form("review_form", clear_on_submit=True):
        stars = st.radio(
            "Em chấm quán mấy sao?",
            [1, 2, 3, 4, 5],
            index=4,
            horizontal=True,
            format_func=lambda n: "⭐" * n
        )
        reviewer = st.text_input("Tên của em (không bắt buộc)")
        message = st.text_area("Lời nhắn dành cho quán")
        submit_review = st.form_submit_button("Gửi đánh giá 💗")

    if submit_review:
        st.session_state.reviews.append({
            "stars": stars,
            "name": reviewer.strip() or "Khách quý",
            "message": message.strip(),
            "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        })
        st.success("Cảm ơn em đã để lại lời thương 🌸")

    if st.session_state.reviews:
        st.subheader("Lời nhắn từ khách quý")

        for review in reversed(st.session_state.reviews[-10:]):
            with st.container(border=True):
                st.write(
                    f"{'⭐' * review['stars']} · **{review['name']}**"
                )
                if review["message"]:
                    st.write(review["message"])
                st.caption(review["date"])


# ==================== CHÂN TRANG ====================

st.divider()
st.markdown(
    "<div style='text-align:center;color:#a66c84'>"
    "Made with ♡ for Kiều Nữ Quán · Demo version"
    "</div>",
    unsafe_allow_html=True
)
