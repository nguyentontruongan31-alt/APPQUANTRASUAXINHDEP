
import streamlit as st
import random
import qrcode
from io import BytesIO
from datetime import datetime

st.set_page_config(
    page_title="MOON TEA",
    page_icon="🌙",
    layout="wide"
)

# ===================== GIAO DIỆN =====================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #fff8f5, #fff0f6, #f1edff);
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 { color: #75476e; }
.hero {
    padding: 28px;
    border-radius: 24px;
    background: linear-gradient(120deg, #fff, #ffe3ef, #e8e0ff);
    box-shadow: 0 8px 25px #9d71941c;
    margin-bottom: 22px;
}
.brand {
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    color: #a35483;
    font-weight: bold;
}
.card {
    background: #ffffffd9;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #f0d9e8;
    margin-bottom: 12px;
}
.price {
    color: #c45186;
    font-weight: bold;
    font-size: 20px;
}
div.stButton > button,
div.stFormSubmitButton > button {
    background: linear-gradient(90deg, #d875a0, #a58be8);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff0f6, #f0ecff);
}
</style>
""", unsafe_allow_html=True)

# ===================== MENU ĐỒ UỐNG =====================

MENU = {
    "Trà sữa": [
        {
            "name": "Trà sữa trân châu đường đen",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=800&q=80",
            "desc": "Béo thơm, trân châu dẻo, đường đen đậm vị."
        },
        {
            "name": "Trà sữa ô long kem cheese",
            "price": 49000,
            "image": "https://images.unsplash.com/photo-1525385133512-2f3bdd039054?auto=format&fit=crop&w=800&q=80",
            "desc": "Ô long thơm dịu cùng lớp kem cheese."
        },
        {
            "name": "Trà sữa khoai môn",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=800&q=80",
            "desc": "Khoai môn ngọt dịu, màu tím pastel."
        },
        {
            "name": "Trà sữa dâu",
            "price": 47000,
            "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=800&q=80",
            "desc": "Vị dâu thơm ngọt và sữa tươi mịn."
        }
    ],
    "Matcha": [
        {
            "name": "Matcha latte",
            "price": 49000,
            "image": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha xanh thơm, sữa tươi béo nhẹ."
        },
        {
            "name": "Matcha dâu latte",
            "price": 55000,
            "image": "https://images.unsplash.com/photo-1546173159-315724a31696?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha thanh mát kết hợp dâu tây."
        },
        {
            "name": "Matcha kem cheese",
            "price": 55000,
            "image": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=800&q=80",
            "desc": "Matcha đậm vị và kem cheese béo mặn."
        }
    ],
    "Trà trái cây": [
        {
            "name": "Trà đào cam sả",
            "price": 42000,
            "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=800&q=80",
            "desc": "Trà thanh mát, đào giòn, cam và sả."
        },
        {
            "name": "Trà vải",
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1513558161293-c5b0b182a0e4?auto=format&fit=crop&w=800&q=80",
            "desc": "Hương vải ngọt dịu, thơm nhẹ."
        }
    ]
}

TOPPINGS = {
    "Không topping": 0,
    "Trân châu đen": 7000,
    "Trân châu trắng": 7000,
    "Thạch củ năng": 8000,
    "Pudding trứng": 8000,
    "Kem cheese": 12000,
    "Thạch dừa": 7000
}

VOUCHERS = {
    "MOON10": {"min": 100000, "type": "percent", "value": 10},
    "MATCHA15": {"min": 150000, "type": "percent", "value": 15},
    "FREESHIP": {"min": 80000, "type": "fixed", "value": 15000}
}

# ===================== TRẠNG THÁI ỨNG DỤNG =====================

defaults = {
    "cart": [],
    "page": "Trang chủ",
    "voucher": "",
    "discount": 0,
    "paid": False,
    "order_id": "",
    "payment_method": "Tiền mặt",
    "total_paid": 0,
    "customer": "",
    "reviews": [],
    "review_done": False,
    "spun": False,
    "prize": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def money(number):
    return f"{int(number):,}".replace(",", ".") + "đ"


def cart_subtotal():
    return sum(
        item["unit_price"] * item["qty"]
        for item in st.session_state.cart
    )


def make_qr(text):
    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#75476e", back_color="white")
    output = BytesIO()
    img.save(output, format="PNG")
    return output.getvalue()


# ===================== ĐIỀU HƯỚNG =====================

with st.sidebar:
    st.markdown(
        "<h1 style='text-align:center'>🌙 MOON TEA</h1>",
        unsafe_allow_html=True
    )
    st.caption("A little moonlight in every cup")
    st.divider()

    st.session_state.page = st.radio(
        "Điều hướng",
        [
            "Trang chủ",
            "Đặt món",
            "Giỏ hàng & Thanh toán",
            "Vòng quay may mắn",
            "Giới thiệu quán",
            "Đánh giá & Phản hồi"
        ]
    )

    st.divider()
    st.markdown("### 🛒 Giỏ hàng")
    st.write(
        f"Số lượng: {sum(i['qty'] for i in st.session_state.cart)} món"
    )
    st.markdown(f"**{money(cart_subtotal())}**")

st.markdown("""
<div class="hero">
    <div class="brand">☾ MOON TEA</div>
    <h3>Trà ngon, mood xinh, ngày dịu dàng ✨</h3>
    <p>Khám phá hương vị yêu thích trong không gian pastel Hàn Quốc.</p>
</div>
""", unsafe_allow_html=True)

# ===================== TRANG CHỦ =====================

if st.session_state.page == "Trang chủ":
    left, right = st.columns([1.2, 1])

    with left:
        st.title("Chạm vào vị ngọt của riêng bạn 💗")
        st.write("""
        MOON TEA là góc nhỏ dành cho những người yêu trà sữa,
        matcha và những khoảnh khắc thư giãn.
        
        Chọn thức uống, thêm topping yêu thích và tùy chỉnh
        độ ngọt theo đúng gu của bạn.
        """)
        if st.button("🧋 Bắt đầu đặt món"):
            st.session_state.page = "Đặt món"
            st.rerun()

    with right:
        st.image(
            "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

    st.markdown("### 🌟 Món được yêu thích")
    cols = st.columns(3)
    featured = [
        MENU["Trà sữa"][0],
        MENU["Matcha"][0],
        MENU["Trà trái cây"][0]
    ]

    for col, item in zip(cols, featured):
        with col:
            st.image(item["image"], use_container_width=True)
            st.markdown(f"**{item['name']}**")
            st.markdown(
                f"<div class='price'>{money(item['price'])}</div>",
                unsafe_allow_html=True
            )
            if st.button("Thêm nhanh", key="quick_" + item["name"]):
                st.session_state.cart.append({
                    "name": item["name"],
                    "qty": 1,
                    "base_price": item["price"],
                    "topping": "Không topping",
                    "sweetness": "50%",
                    "ice": "Có đá",
                    "unit_price": item["price"]
                })
                st.toast("Đã thêm vào giỏ hàng!")
                st.rerun()

# ===================== ĐẶT MÓN =====================

elif st.session_state.page == "Đặt món":
    st.title("🧋 Menu MOON TEA")
    category = st.selectbox("Chọn nhóm đồ uống", list(MENU.keys()))

    products = MENU[category]

    for start in range(0, len(products), 2):
        cols = st.columns(2)

        for col, item in zip(cols, products[start:start + 2]):
            with col:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.image(item["image"], use_container_width=True)
                st.subheader(item["name"])
                st.caption(item["desc"])
                st.markdown(
                    f"<div class='price'>{money(item['price'])}</div>",
                    unsafe_allow_html=True
                )

                with st.form("order_" + item["name"]):
                    qty = st.number_input(
                        "Số lượng",
                        min_value=1,
                        max_value=20,
                        value=1,
                        step=1
                    )
                    topping = st.selectbox(
                        "Topping",
                        list(TOPPINGS.keys())
                    )
                    sweetness = st.select_slider(
                        "Độ ngọt",
                        options=["0%", "30%", "50%", "70%", "100%"],
                        value="50%"
                    )
                    ice = st.radio(
                        "Lượng đá",
                        ["Có đá", "Ít đá", "Không đá"],
                        horizontal=True
                    )

                    add = st.form_submit_button(
                        "＋ Thêm vào giỏ",
                        use_container_width=True
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
                            "unit_price": item["price"] + topping_price
                        })
                        st.success("Đã thêm món vào giỏ!")
                        st.rerun()

                st.markdown("</div>", unsafe_allow_html=True)

# ===================== GIỎ HÀNG & THANH TOÁN =====================

elif st.session_state.page == "Giỏ hàng & Thanh toán":
    st.title("🧾 Giỏ hàng & Thanh toán")

    if not st.session_state.cart:
        st.info("Giỏ hàng trống. Hãy chọn món trong mục Đặt món.")
        if st.button("Quay lại menu"):
            st.session_state.page = "Đặt món"
            st.rerun()

    else:
        for idx, item in enumerate(st.session_state.cart):
            with st.container(border=True):
                col1, col2, col3 = st.columns([4, 1, 1])

                with col1:
                    st.markdown(f"**{item['name']}**")
                    st.caption(
                        f"Topping: {item.get('topping', 'Không topping')} · "
                        f"Độ ngọt: {item.get('sweetness', '50%')} · "
                        f"{item.get('ice', 'Có đá')}"
                    )

                with col2:
                    st.write(f"x {item['qty']}")

                with col3:
                    st.write(money(item["unit_price"] * item["qty"]))
                    if st.button("Xóa", key=f"delete_{idx}"):
                        st.session_state.cart.pop(idx)
                        st.rerun()

        subtotal = cart_subtotal()

        st.divider()
        st.subheader("🎟️ Voucher")

        with st.form("voucher_form"):
            voucher_code = st.text_input(
                "Nhập mã voucher",
                placeholder="MOON10 / MATCHA15 / FREESHIP"
            ).strip().upper()
            apply = st.form_submit_button("Áp dụng voucher")

            if apply:
                voucher = VOUCHERS.get(voucher_code)

                if voucher and subtotal >= voucher["min"]:
                    if voucher["type"] == "percent":
                        discount = round(subtotal * voucher["value"] / 100)
                    else:
                        discount = voucher["value"]

                    st.session_state.voucher = voucher_code
                    st.session_state.discount = discount
                    st.success(
                        f"Áp dụng thành công: giảm {money(discount)}"
                    )
                elif voucher:
                    st.session_state.voucher = ""
                    st.session_state.discount = 0
                    st.error(
                        "Đơn hàng chưa đạt giá trị tối thiểu của voucher."
                    )
                else:
                    st.session_state.voucher = ""
                    st.session_state.discount = 0
                    st.error("Mã voucher không hợp lệ.")

        discount = st.session_state.discount
        total = max(0, subtotal - discount)

        c1, c2, c3 = st.columns(3)
        c1.metric("Tạm tính", money(subtotal))
        c2.metric("Giảm giá", "-" + money(discount))
        c3.metric("Tổng thanh toán", money(total))

        st.divider()
        st.subheader("👤 Thông tin khách hàng")

        with st.form("checkout_form"):
            customer = st.text_input("Tên khách hàng")
            phone = st.text_input("Số điện thoại (không bắt buộc)")
            payment = st.radio(
                "Phương thức thanh toán",
                ["Tiền mặt", "Mã QR"],
                horizontal=True
            )
            checkout = st.form_submit_button(
                "Tiếp tục thanh toán",
                type="primary",
                use_container_width=True
            )

            if checkout:
                if not customer.strip():
                    st.error("Vui lòng nhập tên khách hàng.")
                else:
                    st.session_state.customer = customer.strip()
                    st.session_state.phone = phone.strip()
                    st.session_state.payment_method = payment
                    st.session_state.total_paid = total
                    st.session_state.order_id = (
                        "MT" + datetime.now().strftime("%y%m%d%H%M%S")
                    )
                    st.session_state.paid = False
                    st.rerun()

        if st.session_state.order_id and not st.session_state.paid:
            st.markdown("### Xác nhận đơn hàng")
            st.write(f"**Mã đơn:** {st.session_state.order_id}")
            st.write(f"**Khách hàng:** {st.session_state.customer}")
            st.write(f"**Số tiền:** {money(st.session_state.total_paid)}")

            if st.session_state.payment_method == "Mã QR":
                qr_content = (
                    f"MOON TEA | Don {st.session_state.order_id} | "
                    f"So tien {st.session_state.total_paid} VND"
                )
                st.image(
                    make_qr(qr_content),
                    width=230,
                    caption="QR demo — chưa kết nối ngân hàng"
                )
                st.warning(
                    "Đây là QR minh họa, chưa phải QR chuyển khoản "
                    "ngân hàng. Nút bên dưới chỉ mô phỏng xác nhận."
                )
            else:
                st.info("Bạn thanh toán tiền mặt tại quầy.")

            if st.button(
                "✅ Xác nhận thanh toán thành công",
                type="primary",
                use_container_width=True
            ):
                st.session_state.paid = True
                st.session_state.review_done = False
                st.session_state.page = "Đánh giá & Phản hồi"
                st.rerun()

        if st.session_state.paid:
            st.divider()
            st.markdown("## 🌙 MOON TEA — HÓA ĐƠN")
            st.write(f"Mã đơn: {st.session_state.order_id}")
            st.write(f"Khách hàng: {st.session_state.customer}")
            st.write(
                f"Phương thức thanh toán: "
                f"{st.session_state.payment_method}"
            )

            for item in st.session_state.cart:
                amount = item["unit_price"] * item["qty"]
                st.write(
                    f"- {item['name']} × {item['qty']}: {money(amount)}"
                )

            st.write(f"Tạm tính: {money(subtotal)}")
            st.write(f"Giảm giá: -{money(discount)}")
            st.subheader(f"TỔNG CỘNG: {money(total)}")

        if st.button("Tiếp tục chọn món"):
            st.session_state.page = "Đặt món"
            st.rerun()


# ===================== VÒNG QUAY MAY MẮN =====================

elif st.session_state.page == "Vòng quay may mắn":
    st.title("🎡 Vòng quay ánh trăng")
    st.write("Thử vận may để nhận voucher hoặc quà nhỏ từ MOON TEA!")

    prizes = [
        {
            "name": "Voucher giảm 10%",
            "detail": "Mã MOON10 — áp dụng cho đơn từ 100.000đ",
            "code": "MOON10"
        },
        {
            "name": "Tặng topping trân châu",
            "detail": "Vui lòng báo nhân viên khi sử dụng quà.",
            "code": None
        },
        {
            "name": "Voucher giảm 15.000đ",
            "detail": "Mã FREESHIP — áp dụng cho đơn từ 80.000đ",
            "code": "FREESHIP"
        },
        {
            "name": "Voucher Matcha giảm 15%",
            "detail": "Mã MATCHA15 — áp dụng cho đơn từ 150.000đ",
            "code": "MATCHA15"
        },
        {
            "name": "Chúc bạn may mắn lần sau",
            "detail": "Cảm ơn bạn đã chơi cùng MOON TEA!",
            "code": None
        }
    ]

    st.markdown("""
    <div style="
        text-align:center; padding:32px;
        background:linear-gradient(120deg,#ffe0ee,#e7deff);
        border-radius:28px; font-size:65px;">
        🎀 🎁 🌙 🎁 🎀
        <h2>MOON TEA LUCKY WHEEL</h2>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.spun:
        if st.button("✨ QUAY NGAY ✨", type="primary"):
            st.session_state.prize = random.choice(prizes)
            st.session_state.spun = True
            st.rerun()
    else:
        prize = st.session_state.prize
        st.success(f"🎉 Phần quà của bạn: {prize['name']}")
        st.write(prize["detail"])

        if prize["code"]:
            st.code(prize["code"])
            if st.button("Dùng voucher này"):
                st.session_state.page = "Giỏ hàng & Thanh toán"
                st.session_state.voucher = prize["code"]
                st.session_state.discount = 0
                st.rerun()

        if st.button("Quay lại từ đầu"):
            st.session_state.spun = False
            st.session_state.prize = None
            st.rerun()


# ===================== GIỚI THIỆU QUÁN =====================

elif st.session_state.page == "Giới thiệu quán":
    st.title("🌙 Câu chuyện MOON TEA")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

    with col2:
        st.subheader("Một chút ánh trăng trong mỗi chiếc ly")
        st.write("""
        MOON TEA lấy cảm hứng từ phong cách Hàn Quốc nhẹ nhàng,
        gam màu pastel và những khoảnh khắc nghỉ ngơi thật dễ chịu.

        Chúng mình muốn mỗi ly trà đều là một niềm vui nhỏ:
        từ trà sữa cổ điển, matcha xanh thơm đến trà trái cây tươi mát.
        """)

        st.markdown("### 🌸 Điều chúng mình yêu")
        st.write("- Tùy chỉnh độ ngọt và lượng đá.")
        st.write("- Nhiều loại topping để lựa chọn.")
        st.write("- Menu phù hợp cho những buổi gặp gỡ bạn bè.")

        st.markdown("### 📍 Thông tin quán")
        st.write("Địa chỉ: 123 Đường Ánh Trăng, TP. Hồ Chí Minh")
        st.write("Giờ mở cửa: 09:00 – 22:00")
        st.write("Hotline: 0900 123 456")

        st.caption(
            "Thông tin địa chỉ và hotline trên là mẫu; hãy sửa thành "
            "thông tin thật của quán."
        )

    if st.button("🧋 Đặt món ngay"):
        st.session_state.page = "Đặt món"
        st.rerun()


# ===================== ĐÁNH GIÁ & PHẢN HỒI =====================

elif st.session_state.page == "Đánh giá & Phản hồi":
    st.title("💌 Đánh giá & Phản hồi")

    if not st.session_state.paid:
        st.info(
            "Form đánh giá sẽ xuất hiện sau khi bạn xác nhận "
            "thanh toán thành công."
        )

        if st.button("Đến thanh toán"):
            st.session_state.page = "Giỏ hàng & Thanh toán"
            st.rerun()

    else:
        st.success(
            f"Cảm ơn {st.session_state.customer} đã đặt món tại MOON TEA!"
        )

        if not st.session_state.review_done:
            st.write("Trải nghiệm của bạn hôm nay thế nào?")

            with st.form("review_form"):
                stars = st.select_slider(
                    "Chấm điểm",
                    options=[1, 2, 3, 4, 5],
                    value=5,
                    format_func=lambda n: "⭐" * n
                )

                comment = st.text_area(
                    "Lời nhắn cho quán",
                    placeholder="Bạn thích món nào? Chúng mình cần cải thiện điều gì?"
                )

                name = st.text_input(
                    "Tên hiển thị",
                    value=st.session_state.customer
                )

                submit_review = st.form_submit_button(
                    "Gửi đánh giá 💗",
                    type="primary",
                    use_container_width=True
                )

                if submit_review:
                    st.session_state.reviews.append({
                        "name": name.strip() or "Khách MOON TEA",
                        "stars": stars,
                        "comment": comment.strip(),
                        "order": st.session_state.order_id,
                        "time": datetime.now().strftime("%d/%m/%Y %H:%M")
                    })
                    st.session_state.review_done = True
                    st.rerun()

        else:
            st.success("Đã nhận đánh giá. Cảm ơn bạn thật nhiều! 💗")

            if st.button("Tạo đơn hàng mới"):
                st.session_state.cart = []
                st.session_state.voucher = ""
                st.session_state.discount = 0
                st.session_state.paid = False
                st.session_state.order_id = ""
                st.session_state.total_paid = 0
                st.session_state.customer = ""
                st.session_state.review_done = False
                st.session_state.spun = False
                st.session_state.prize = None
                st.session_state.page = "Đặt món"
                st.rerun()

    if st.session_state.reviews:
        st.divider()
        st.subheader("💬 Phản hồi gần đây")

        for review in reversed(st.session_state.reviews[-10:]):
            with st.container(border=True):
                st.write(
                    f"**{review['name']}** · {'⭐' * review['stars']}"
                )
                if review["comment"]:
                    st.write(review["comment"])
                st.caption(
                    f"{review['time']} · Mã đơn {review['order']}"
                )


# ===================== FOOTER =====================

st.divider()
st.markdown(
    "<div style='text-align:center;color:#947c95'>"
    "Made with ♡ by MOON TEA · Sip slowly, shine softly 🌙"
    "</div>",
    unsafe_allow_html=True
)
