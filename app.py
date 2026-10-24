import streamlit as st
import random

# Cấu hình trang
st.set_page_config(
    page_title="SLAY TEA - Tiệm Trà Sữa Slay & Chill",
    page_icon="💅",
    layout="wide"
)

# Khởi tạo Session State
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'discount_percent' not in st.session_state:
    st.session_state.discount_percent = 0
if 'voucher_code' not in st.session_state:
    st.session_state.voucher_code = ""
if 'spin_prize' not in st.session_state:
    st.session_state.spin_prize = None
if 'order_success' not in st.session_state:
    st.session_state.order_success = False
if 'feedback_given' not in st.session_state:
    st.session_state.feedback_given = False

# Dữ liệu Menu quán concept Slay
MENU = {
    "Trà Sữa": [
        {
            "id": "ts_1",
            "name": "Trà Sữa Slay Queen",
            "price": 45000,
            "img": "https://images.unsplash.com/photo-1541658016709-82535e94bc69?w=500&auto=format&fit=crop&q=60",
            "desc": "Trà đen vị đậm đà cùng lớp kem béo ngậy, uống vào là bật mood Slay ngay lập tức!"
        },
        {
            "id": "ts_2",
            "name": "Trà Sữa Thái Tử Nơ (Thai Milk Tea)",
            "price": 42000,
            "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=500&auto=format&fit=crop&q=60",
            "desc": "Hương vị trà Thái chuẩn vị, ngọt ngào nhưng không kém phần sang chảnh."
        },
        {
            "id": "ts_3",
            "name": "Trà Sữa Kiêu Kỳ Oolong Cheese",
            "price": 48000,
            "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=500&auto=format&fit=crop&q=60",
            "desc": "Oolong rang thơm phức phủ kem cheese mặn mặn béo ngậy đỉnh cao."
        }
    ],
    "Matcha": [
        {
            "id": "m_1",
            "name": "Matcha Chảnh Sảng (Matcha Latte)",
            "price": 52000,
            "img": "https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=500&auto=format&fit=crop&q=60",
            "desc": "Matcha Nhật Bản nguyên chất phối sữa tươi thanh mát, màu xanh slay chuẩn gu."
        },
        {
            "id": "m_2",
            "name": "Matcha Drama Macchiato",
            "price": 55000,
            "img": "https://images.unsplash.com/photo-1517596044737-017e47269176?w=500&auto=format&fit=crop&q=60",
            "desc": "Đậm đà vị matcha quyện cùng lớp macchiato sóng sánh ngập tràn drama."
        }
    ]
}

TOPPINGS = {
    "Trân châu đen Slay": 8000,
    "Trân châu hoàng gia": 10000,
    "Thạch phô mai Chảnh": 10000,
    "Pudding trứng béo ngậy": 10000,
    "Sương sáo Chill": 6000
}

# Sidebar điều hướng
st.sidebar.title("💅 SLAY TEA MENU")
menu_selection = st.sidebar.radio(
    "Khám phá ngay:",
    ["Giới thiệu quán", "Menu & Đặt món", "Giỏ hàng & Thanh toán", "Vòng quay may mắn"]
)

# ==========================================
# PHẦN 1: GIỚI THIỆU QUÁN
# ==========================================
if menu_selection == "Giới thiệu quán":
    st.title("💅 Chào mừng đến với SLAY TEA")
    st.caption("Uống trà sữa là phải Slay - Không Slay đời không nể!")
    st.image("https://images.unsplash.com/photo-1558857563-b371033873b8?w=1200&auto=format&fit=crop&q=80", use_container_width=True)
    
    st.markdown("""
    ### ✨ Về SLAY TEA
    Trà sữa không chỉ là một món uống, đó là **thái độ sống**! SLAY TEA ra đời dành riêng cho những tâm hồn yêu thích sự thời thượng, trẻ trung và chảnh sảng.
    
    * **Chất lượng đỉnh nóc:** Bột matcha chuẩn Nhật, cốt trà ủ trong ngày và topping làm mới liên tục.
    * **Góc check-in thần thánh:** Hương vị thơm ngon tuyệt hảo giúp bạn F5 năng lượng ngay lập tức.
    
    *Hãy chọn món ngay để trải nghiệm cảm giác Slay chuẩn gu nhé!*
    """)

# ==========================================
# PHẦN 2: MENU & ĐẶT MÓN
# ==========================================
elif menu_selection == "Menu & Đặt món":
    st.title("🧋 Menu Slay Đỉnh Nóc")
    
    tab1, tab2 = st.tabs(["✨ Trà Sữa Slay", "🌿 Matcha Chảnh"])
    
    with tab1:
        for item in MENU["Trà Sữa"]:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["name"])
                st.write(item["desc"])
                st.markdown(f"**Giá:** `{item['price']:,} đ`")
                
                with st.form(key=f"form_{item['id']}"):
                    q = st.number_input("Số lượng", min_value=1, max_value=20, value=1, key=f"q_{item['id']}")
                    toppings = st.multiselect("Topping kèm", options=list(TOPPINGS.keys()), key=f"top_{item['id']}")
                    sweetness = st.selectbox("Độ ngọt", ["100% (Bình thường)", "70% (Ít ngọt)", "50% (Vừa)", "30% (Slay nhạt)", "0% (Không đường)"], key=f"swt_{item['id']}")
                    ice = st.selectbox("Đá", ["Đá bình thường", "Ít đá", "Không đá"], key=f"ice_{item['id']}")
                    
                    submitted = st.form_submit_button("🛒 Thêm vào giỏ món")
                    if submitted:
                        topping_total = sum(TOPPINGS[t] for t in toppings)
                        unit_price = item["price"] + topping_total
                        cart_item = {
                            "name": item["name"],
                            "price": unit_price,
                            "quantity": q,
                            "toppings": toppings,
                            "sweetness": sweetness,
                            "ice": ice,
                            "total": unit_price * q
                        }
                        st.session_state.cart.append(cart_item)
                        st.toast(f"Đã thêm {q}x {item['name']} cực Slay vào giỏ!")

    with tab2:
        for item in MENU["Matcha"]:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["name"])
                st.write(item["desc"])
                st.markdown(f"**Giá:** `{item['price']:,} đ`")
                
                with st.form(key=f"form_{item['id']}"):
                    q = st.number_input("Số lượng", min_value=1, max_value=20, value=1, key=f"q_{item['id']}")
                    toppings = st.multiselect("Topping kèm", options=list(TOPPINGS.keys()), key=f"top_{item['id']}")
                    sweetness = st.selectbox("Độ ngọt", ["100% (Bình thường)", "70% (Ít ngọt)", "50% (Vừa)", "30% (Slay nhạt)", "0% (Không đường)"], key=f"swt_{item['id']}")
                    ice = st.selectbox("Đá", ["Đá bình thường", "Ít đá", "Không đá"], key=f"ice_{item['id']}")
                    
                    submitted = st.form_submit_button("🛒 Thêm vào giỏ món")
                    if submitted:
                        topping_total = sum(TOPPINGS[t] for t in toppings)
                        unit_price = item["price"] + topping_total
                        cart_item = {
                            "name": item["name"],
                            "price": unit_price,
                            "quantity": q,
                            "toppings": toppings,
                            "sweetness": sweetness,
                            "ice": ice,
                            "total": unit_price * q
                        }
                        st.session_state.cart.append(cart_item)
                        st.toast(f"Đã thêm {q}x {item['name']} vào giỏ!")

# ==========================================
# PHẦN 3: GIỎ HÀNG & THANH TOÁN
# ==========================================
elif menu_selection == "Giỏ hàng & Thanh toán":
    st.title("🛍️ Giỏ Hàng & Thanh Toán")
    
    if not st.session_state.cart:
        st.info("Giỏ hàng của bạn đang trống. Chọn vài món thật Slay ở mục 'Menu & Đặt món' nhé!")
    else:
        st.subheader("📋 Các Món Đã Chọn")
        subtotal = 0
        
        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.markdown(f"**{idx+1}. {item['name']}**")
                topping_str = ", ".join(item['toppings']) if item['toppings'] else "Không topping"
                st.caption(f"Topping: {topping_str} | Ngọt: {item['sweetness']} | Đá: {item['ice']}")
            with col2:
                st.write(f"SL: {item['quantity']} x {item['price']:,} đ")
            with col3:
                st.write(f"**{item['total']:,} đ**")
            subtotal += item['total']
            st.divider()
            
        # Phần Nhập Voucher
        st.subheader("🎟️ Nhập Mã Voucher Giảm Giá")
        col_v1, col_v2 = st.columns([2, 1])
        with col_v1:
            voucher_input = st.text_input("Nhập mã (VD: SLAY10, SLAY20)", value=st.session_state.voucher_code)
        with col_v2:
            st.write("")
            st.write("")
            if st.button("Áp dụng"):
                if voucher_input.upper() == "SLAY10":
                    st.session_state.discount_percent = 10
                    st.session_state.voucher_code = "SLAY10"
                    st.success("Đã áp dụng mã giảm 10%!")
                elif voucher_input.upper() == "SLAY20":
                    st.session_state.discount_percent = 20
                    st.session_state.voucher_code = "SLAY20"
                    st.success("Đã áp dụng mã giảm 20%!")
                else:
                    st.session_state.discount_percent = 0
                    st.session_state.voucher_code = ""
                    st.error("Mã không hợp lệ!")

        # Tính toán tiền
        discount_amount = int(subtotal * (st.session_state.discount_percent / 100))
        final_total = subtotal - discount_amount
        
        st.markdown("---")
        st.subheader("💵 Tổng Chi Phí Bill")
        st.write(f"- Tạm tính: `{subtotal:,} đ`")
        if st.session_state.discount_percent > 0:
            st.write(f"- Giảm giá ({st.session_state.discount_percent}%): `- {discount_amount:,} đ`")
        st.markdown(f"### 🎯 Thành tiền: `{final_total:,} đ`")
        
        # Phương thức thanh toán
        st.subheader("💳 Phương Thức Thanh Toán")
        payment_method = st.radio("Chọn phương thức:", ["Tiền mặt tại quầy", "Mã QR Chuyển Khoản"])
        
        if payment_method == "Mã QR Chuyển Khoản":
            st.info("Mở App Ngân hàng quét mã QR để chảnh sảng thanh toán:")
            st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=SlayTeaPaymentQR", width=200)
            st.caption("Nội dung CK: THANH TOAN SLAY TEA")
            
        # Nút bấm thanh toán
        if st.button("🚀 Xác Nhận Thanh Toán", type="primary"):
            st.session_state.order_success = True
            st.balloons()

        # Hiển thị kết quả thanh toán & Form Đánh giá
        if st.session_state.order_success:
            st.success("🎉 Thanh toán thành công! Đơn hàng Slay của bạn đã được tiếp nhận.")
            st.markdown("---")
            st.subheader("⭐ Đánh Giá & Phản Hồi Dành Cho Quán")
            
            if not st.session_state.feedback_given:
                with st.form("feedback_form"):
                    rating = st.slider("Chấm độ Slay của quán (1 - 5 ⭐)", min_value=1, max_value=5, value=5)
                    message = st.text_area("Để lại lời nhắn yêu thương cho quán:")
                    submitted_fb = st.form_submit_button("Gửi Đánh Giá")
                    
                    if submitted_fb:
                        st.session_state.feedback_given = True
                        st.success("Cảm ơn đánh giá cực Slay từ bạn! Chúc bạn có trải nghiệm tuyệt vời.")
                        st.rerun()
            else:
                st.info("Cảm ơn bạn đã để lại lời nhắn yêu thương cho Slay Tea!")
                
            if st.button("🔄 Đặt đơn mới"):
                st.session_state.cart = []
                st.session_state.discount_percent = 0
                st.session_state.voucher_code = ""
                st.session_state.order_success = False
                st.session_state.feedback_given = False
                st.rerun()

# ==========================================
# PHẦN 4: VÒNG QUAY MAY MẮN
# ==========================================
elif menu_selection == "Vòng quay may mắn":
    st.title("🎡 Vòng Quay May Mắn Slay Girl / Slay Boy")
    st.write("Quay là trúng - Nhận ngay mã voucher cực xịn!")
    
    prizes = [
        "Mã giảm 10% (Code: SLAY10)", 
        "Mã giảm 20% (Code: SLAY20)", 
        "Tặng 1 Topping Trân Châu Slay", 
        "Chúc bạn Slay hơn vào lần sau!"
    ]
    
    if st.button("🎲 Quay Thưởng Ngay", type="primary"):
        chosen_prize = random.choice(prizes)
        st.session_state.spin_prize = chosen_prize
        st.balloons()
        
    if st.session_state.spin_prize:
        st.markdown("### 🎉 Kết quả phần thưởng:")
        st.success(f"**{st.session_state.spin_prize}**")
        if "SLAY10" in st.session_state.spin_prize:
            st.info("Copy mã `SLAY10` sang phần 'Giỏ hàng & Thanh toán' để nhận ưu đãi nhé!")
        elif "SLAY20" in st.session_state.spin_prize:
            st.info("Copy mã `SLAY20` sang phần 'Giỏ hàng & Thanh toán' để nhận ưu đãi nhé!")
