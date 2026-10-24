import streamlit as st
import random

# Cấu hình trang
st.set_page_config(
    page_title="Cosmic Tea - Tiệm Trà Sữa Ngân Hà",
    page_icon="🧋",
    layout="wide"
)

# Khởi tạo Session State để lưu giỏ hàng, voucher và trạng thái đơn hàng
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

# Dữ liệu Menu quán
MENU = {
    "Trà Sữa": [
        {
            "id": "ts_1",
            "name": "Trà Sữa Hố Đen (Black Hole Milk Tea)",
            "price": 45000,
            "img": "https://images.unsplash.com/photo-1541658016709-82535e94bc69?w=500&auto=format&fit=crop&q=60",
            "desc": "Trà đen đậm đà kết hợp sữa tươi nguyên chất và trân châu hoàng kim."
        },
        {
            "id": "ts_2",
            "name": "Trà Sữa Siêu Tân Tinh Oolong",
            "price": 50000,
            "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=500&auto=format&fit=crop&q=60",
            "desc": "Trà Oolong rang thơm lừng quyện cùng kem sữa cheese béo ngậy."
        },
        {
            "id": "ts_3",
            "name": "Trà Sữa Bá Tước Ngân Hà (Earl Grey)",
            "price": 48000,
            "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=500&auto=format&fit=crop&q=60",
            "desc": "Hương vị cam Bergamot thanh mát kết hợp sữa thơm mịn."
        }
    ],
    "Matcha": [
        {
            "id": "m_1",
            "name": "Matcha Latte Dải Ngân Hà",
            "price": 55000,
            "img": "https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=500&auto=format&fit=crop&q=60",
            "desc": "Bột matcha Nhật Bản nguyên chất 100% tầng vị đậm đà."
        },
        {
            "id": "m_2",
            "name": "Matcha Sao Băng (Matcha Macchiato)",
            "price": 52000,
            "img": "https://images.unsplash.com/photo-1517596044737-017e47269176?w=500&auto=format&fit=crop&q=60",
            "desc": "Matcha thanh mát phủ lớp bọt kem macchiato mặn ngọt hoàn hảo."
        }
    ]
}

TOPPINGS = {
    "Trân châu đen": 8000,
    "Trân châu trắng": 8000,
    "Thạch phô mai": 10000,
    "Pudding trứng": 10000,
    "Sương sáo": 6000
}

# Thanh điều hướng sidebar
st.sidebar.title("🌌 Cosmic Tea Menu")
menu_selection = st.sidebar.radio(
    "Di chuyển đến:",
    ["Giới thiệu quán", "Menu & Đặt món", "Giỏ hàng & Thanh toán", "Vòng quay may mắn"]
)

# ==========================================
# PHẦN 1: GIỚI THIỆU QUÁN
# ==========================================
if menu_selection == "Giới thiệu quán":
    st.title("🌌 Chào mừng đến với Cosmic Tea - Tiệm Trà Sữa Ngân Hà")
    st.image("https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&auto=format&fit=crop&q=80", use_container_width=True)
    
    st.markdown("""
    ### 🚀 Không gian mang đậm hơi thở vũ trụ
    **Cosmic Tea** được thành lập với cảm hứng từ những vì sao lấp lánh và không gian bao la của ngân hà. Chúng tôi mang đến cho bạn không chỉ những ly trà sữa thơm ngon tuyệt hảo mà còn là một hành trình vị giác bay bổng giữa các vì sao.
    
    * **Nguyên liệu chuẩn sao:** Trà hái từ những vùng cao nguyên thuần khiết, sữa tươi chọn lọc và trân châu làm thủ công mỗi ngày.
    * **Công thức độc quyền:** Sự pha trộn tinh tế giữa truyền thống và hiện đại giúp mỗi ngụm trà đều mang cảm giác sảng khoái, bừng tỉnh năng lượng.
    
    *Hãy ghé thăm tụ điểm không gian của chúng tôi hoặc đặt món ngay trên ứng dụng nhé!*
    """)

# ==========================================
# PHẦN 2: MENU & ĐẶT MÓN
# ==========================================
elif menu_selection == "Menu & Đặt món":
    st.title("🧋 Khám Phá Menu Ngân Hà")
    
    category = st.tabs(["🍵 Trà Sữa", "🌿 Matcha"])
    
    with category[0]:
        cat_name = "Trà Sữa"
        for item in MENU[cat_name]:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["name"])
                st.write(item["desc"])
                st.markdown(f"**Giá:** `{item['price']:,} đ`")
                
                with st.form(key=f"form_{item['id']}"):
                    q = st.number_input("Số lượng", min_value=1, max_value=20, value=1, key=f"q_{item['id']}")
                    toppings = st.multiselect("Chọn Topping", options=list(TOPPINGS.keys()), key=f"top_{item['id']}")
                    sweetness = st.selectbox("Độ ngọt", ["100% (Bình thường)", "70% (Ít ngọt)", "50% (Vừa)", "30% (Nhạt)", "0% (Không đường)"], key=f"swt_{item['id']}")
                    ice = st.selectbox("Đá", ["Đá bình thường", "Ít đá", "Không đá"], key=f"ice_{item['id']}")
                    
                    submitted = st.form_submit_button("🛒 Thêm vào giỏ hàng")
                    if submitted:
                        # Tính giá topping
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
                        st.success(f"Đã thêm {q}x {item['name']} vào giỏ hàng!")

    with category[1]:
        cat_name = "Matcha"
        for item in MENU[cat_name]:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["name"])
                st.write(item["desc"])
                st.markdown(f"**Giá:** `{item['price']:,} đ`")
                
                with st.form(key=f"form_{item['id']}"):
                    q = st.number_input("Số lượng", min_value=1, max_value=20, value=1, key=f"q_{item['id']}")
                    toppings = st.multiselect("Chọn Topping", options=list(TOPPINGS.keys()), key=f"top_{item['id']}")
                    sweetness = st.selectbox("Độ ngọt", ["100% (Bình thường)", "70% (Ít ngọt)", "50% (Vừa)", "30% (Nhạt)", "0% (Không đường)"], key=f"swt_{item['id']}")
                    ice = st.selectbox("Đá", ["Đá bình thường", "Ít đá", "Không đá"], key=f"ice_{item['id']}")
                    
                    submitted = st.form_submit_button("🛒 Thêm vào giỏ hàng")
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
                        st.success(f"Đã thêm {q}x {item['name']} vào giỏ hàng!")

# ==========================================
# PHẦN 3: GIỎ HÀNG & THANH TOÁN
# ==========================================
elif menu_selection == "Giỏ hàng & Thanh toán":
    st.title("🛒 Giỏ Hàng & Thanh Toán Đơn Hàng")
    
    if not st.session_state.cart:
        st.info("Giỏ hàng của bạn đang trống. Hãy qua phần 'Menu & Đặt món' để chọn thức uống nhé!")
    else:
        # Hiển thị danh sách món trong giỏ
        st.subheader("📋 Chi Tiết Món Đã Chọn")
        
        subtotal = 0
        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.markdown(f"**{idx+1}. {item['name']}**")
                topping_str = ", ".join(item['toppings']) if item['toppings'] else "Không có"
                st.caption(- f"Topping: {topping_str} | Ngọt: {item['sweetness']} | Đá: {item['ice']}")
            with col2:
                st.write(f"SL: {item['quantity']} x {item['price']:,} đ")
            with col3:
                st.write(f"**{item['total']:,} đ**")
            subtotal += item['total']
            st.divider()
            
        # Nhập mã voucher
        st.subheader("🎟️ Nhập Mã Voucher")
        col_v1, col_v2 = st.columns([2, 1])
        with col_v1:
            voucher_input = st.text_input("Nhập mã giảm giá (VD: COSMIC10, COSMIC20)", value=st.session_state.voucher_code)
        with col_v2:
            st.write("")
            st.write("")
            if st.button("Áp dụng mã"):
                if voucher_input.upper() == "COSMIC10":
                    st.session_state.discount_percent = 10
                    st.session_state.voucher_code = "COSMIC10"
                    st.success("Áp dụng mã giảm giá 10% thành công!")
                elif voucher_input.upper() == "COSMIC20":
                    st.session_state.discount_percent = 20
                    st.session_state.voucher_code = "COSMIC20"
                    st.success("Áp dụng mã giảm giá 20% thành công!")
                else:
                    st.session_state.discount_percent = 0
                    st.session_state.voucher_code = ""
                    st.error("Mã giảm giá không hợp lệ hoặc hết hạn!")

        # Tính tiền
        discount_amount = int(subtotal * (st.session_state.discount_percent / 100))
        final_total = subtotal - discount_amount
        
        st.markdown("---")
        st.subheader("💵 Tổng Kết Hóa Đơn")
        st.write(f"- **Tạm tính:** `{subtotal:,} đ`")
        if st.session_state.discount_percent > 0:
            st.write(f"- **Giảm giá ({st.session_state.discount_percent}%):** `- {discount_amount:,} đ`")
        st.markdown(f"### 🎯 Tổng cộng thanh toán: `{final_total:,} đ`")
        
        # Phương thức thanh toán
        st.subheader("💳 Phương Thức Thanh Toán")
        payment_method = st.radio("Chọn hình thức thanh toán:", ["Tiền mặt tại quầy", "Chuyển khoản QR Code"])
        
        if payment_method == "Chuyển khoản QR Code":
            st.info("Quét mã QR dưới đây để thanh toán qua Mobile Banking:")
            st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=CosmicTeaPaymentQRCode", width=200)
            st.caption("Nội dung chuyển khoản: THANH TOAN COSMIC TEA")
            
        if st.button("✅ Xác Nhận Thanh Toán", type="primary"):
            st.session_state.order_success = True
            st.balloons()
            st.success("Thanh toán thành công! Đơn hàng của bạn đã được chuyển đến quầy pha chế.")

        # Đánh giá & Phản hồi sau khi thanh toán thành công
        if st.session_state.order_success:
            st.markdown("---")
            st.subheader("⭐ Đánh giá & Phản Hồi")
            if not st.session_state.feedback_given:
                with st.form("feedback_form"):
                    rating = st.slider("Chấm điểm trải nghiệm quán (1 - 5 ⭐)", min_value=1, max_value=5, value=5)
                    message = st.text_area("Lời nhắn hoặc góp ý cho quán:")
                    submitted_fb = st.form_submit_button("Gửi đánh giá")
                    if submitted_fb:
                        st.session_state.feedback_given = True
                        st.success("Cảm ơn bạn đã gửi đánh giá! Chúc bạn thưởng thức trà ngon miệng.")
            else:
                st.info("Cảm ơn bạn đã gửi phản hồi cho Cosmic Tea!")
                
            if st.button("🧹 Làm mới đơn hàng mới"):
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
    st.title("🎡 Vòng Quay May Mắn Ngân Hà")
    st.write("Mỗi khách hàng có đơn hàng đều có cơ hội quay thưởng nhận mã giảm giá hoặc quà tặng hấp dẫn từ quán!")
    
    prizes = [
        "Mã giảm 10% (Nhập mã: COSMIC10)", 
        "Mã giảm 20% (Nhập mã: COSMIC20)", 
        "Tặng 1 Topping miễn phí", 
        "Chúc bạn may mắn lần sau!"
    ]
    
    if st.button("🎲 Quay Thưởng Ngay!", type="primary"):
        chosen_prize = random.choice(prizes)
        st.session_state.spin_prize = chosen_prize
        st.balloons()
        
    if st.session_state.spin_prize:
        st.markdown(f"### 🎉 Kết quả vòng quay của bạn:")
        st.success(f"**{st.session_state.spin_prize}**")
        if "10%" in st.session_state.spin_prize:
            st.info("Bạn có thể sang mục 'Giỏ hàng & Thanh toán' và nhập mã `COSMIC10` nhé.")
        elif "20%" in st.session_state.spin_prize:
            st.info("Bạn có thể sang mục 'Giỏ hàng & Thanh toán' và nhập mã `COSMIC20` nhé.")
    else:
        st.info("Nhấn nút phía trên để thử vận may của bạn!")
