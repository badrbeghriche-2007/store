# -*- coding: utf-8 -*-
import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="دار الأناقة | الأثاث والمرايا",
    page_icon="🛋️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# رقم الواتساب المستلم مع رمز الجزائر الدولي (213)
WHATSAPP_NUMBER = "213784803429"

# 2. تخصيص الثيم باللونين الأبيض والبيج وخط تجوال
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .stApp {
        background-color: #FCFBF9;
        color: #3D3124;
    }
    
    .announcement-bar {
        background-color: #665035;
        color: #FFFFFF;
        padding: 10px 18px;
        border-radius: 14px;
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 25px;
    }
    
    .product-card {
        background-color: #FFFFFF;
        border: 1px solid #ECE4D5;
        border-radius: 24px;
        padding: 26px;
        box-shadow: 0 10px 25px -5px rgba(102, 80, 53, 0.08);
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 35px -5px rgba(102, 80, 53, 0.14);
        border-color: #CBB38E;
    }
    
    .badge {
        display: inline-block;
        background-color: #F6F2EB;
        color: #7D623F;
        padding: 4px 14px;
        border-radius: 10px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .price-text {
        font-size: 28px;
        font-weight: 800;
        color: #665035;
        margin: 10px 0;
    }
    
    .stButton>button {
        background-color: #665035 !important;
        color: #FFFFFF !important;
        border-radius: 14px !important;
        padding: 14px 20px !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background-color: #53412C !important;
        color: #FFFFFF !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(83, 65, 44, 0.25) !important;
    }

    .stTextInput input {
        border-radius: 12px !important;
        border: 1px solid #DFD1B8 !important;
        background-color: #FFFFFF !important;
        padding: 12px 14px !important;
        font-family: 'Tajawal', sans-serif !important;
    }
    .stTextInput input:focus {
        border-color: #665035 !important;
        box-shadow: 0 0 0 2px rgba(181, 150, 105, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. الشريط العلوي
st.markdown("""
<div class="announcement-bar">
    ✨ توصيل متوفر لجميع الولايات | الدفع عند الاستلام | تأكيد الطلبات عبر واتساب: <span dir="ltr"><b>0784803429</b></span>
</div>
""", unsafe_allow_html=True)

# 4. العنوان الرئيسي
st.markdown("<h1 style='text-align:center; color:#53412C; font-weight:800; font-size:36px; margin-bottom:8px;'>أثاث عصري ومرايا ديكور راقية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#7D623F; font-size:16px; margin-bottom:40px;'>اختر منتجك المفضل لتعبئة معلومات التوصيل وسيتم إرسال الطلب مباشرة باسمك عبر الواتساب</p>", unsafe_allow_html=True)

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# 5. عرض المنتجين
col1, col2 = st.columns(2, gap="large")

# الأثاث (65000 دج)
with col1:
    st.markdown("""
    <div class="product-card">
        <span class="badge">الأثاث المنزلي</span>
        <h2 style="color:#53412C; font-size:24px; font-weight:800; margin:0;">أثاث صالون عصري فاخر</h2>
        <div class="price-text">65,000 دج</div>
        <p style="color:#7D623F; font-size:14px; line-height:1.8; margin-top:10px;">
            طقم صالون عصري متكامل بتصميم ناعم ومريح باللونين الأبيض والبيج، مصنوع بجودة عالية ليضفي لمسة فخامة وراحة على منزلك.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("انقر هنا لطلب الأثاث (65000 دج)", key="btn_furniture"):
        st.session_state.selected_product = {
            "name": "أثاث صالون عصري فاخر",
            "price": "65000 دج"
        }

# المرآة (3000 دج)
with col2:
    st.markdown("""
    <div class="product-card">
        <span class="badge">المرايا والديكور</span>
        <h2 style="color:#53412C; font-size:24px; font-weight:800; margin:0;">مرآة ديكور مقوسة فاخرة</h2>
        <div class="price-text">3,000 دج</div>
        <p style="color:#7D623F; font-size:14px; line-height:1.8; margin-top:10px;">
            مرآة مقوسة عصرية فائقة النقاء بإطار هادئ بلون البيج الذهبي، تمنح الغرفة إضاءة ومظهراً جمالياً واسعاً وجذاباً.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("انقر هنا لطلب المرآة (3000 دج)", key="btn_mirror"):
        st.session_state.selected_product = {
            "name": "مرآة ديكور مقوسة فاخرة",
            "price": "3000 دج"
        }

# 6. واجهة تعبئة معلومات الزبون
if st.session_state.selected_product:
    prod = st.session_state.selected_product
    st.markdown("<br><hr style='border:1px solid #ECE4D5;'><br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background-color:#FFFFFF; border:1px solid #CBB38E; border-radius:20px; padding:20px; margin-bottom:20px;">
        <h3 style="color:#53412C; margin:0; font-size:22px; font-weight:800;">
            📝 استمارة الطلب: <span style="color:#665035;">{prod['name']}</span>
        </h3>
        <p style="color:#7D623F; margin-top:6px; font-size:15px;">
            السعر: <b>{prod['price']}</b> | الدفع عند الاستلام
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form(key="order_form", clear_on_submit=False):
        c_name1, c_name2 = st.columns(2)
        with c_name1:
            first_name = st.text_input("الاسم *", placeholder="مثال: محمد")
        with c_name2:
            last_name = st.text_input("اللقب *", placeholder="مثال: بن علي")
            
        phone = st.text_input("رقم الهاتف *", placeholder="07 / 06 / 05 XX XX XX XX")
        email = st.text_input("البريد الإلكتروني *", placeholder="example@email.com")
        address = st.text_input("مكان السكن (الولاية والعنوان الكامل) *", placeholder="الولاية، الدائرة أو البلدية، الحي...")
        
        submitted = st.form_submit_button("تأكيد الطلب وإرسال عبر واتساب (0784803429)")
        
        if submitted:
            if not first_name.strip() or not last_name.strip() or not phone.strip() or not email.strip() or not address.strip():
                st.error("⚠️ يرجى ملء كافة الحقول (الاسم، اللقب، الهاتف، البريد، ومكان السكن) لإتمام طلبك.")
            else:
                full_name = f"{first_name.strip()} {last_name.strip()}"
                
                # صياغة الرسالة باسم الشخص صاحب الطلب
                message = (
                    f"🛒 *طلب جديد باسم: {full_name}*\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"📦 *المنتج المطلوب:* {prod['name']}\n"
                    f"💰 *السعر:* {prod['price']}\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"👤 *الاسم:* {first_name.strip()}\n"
                    f"👤 *اللقب:* {last_name.strip()}\n"
                    f"📞 *رقم الهاتف:* {phone.strip()}\n"
                    f"📧 *البريد الإلكتروني:* {email.strip()}\n"
                    f"📍 *مكان السكن:* {address.strip()}\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"مرسل من طرف الزبون: *{full_name}*"
                )
                
                encoded_msg = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_msg}"
                
                st.success(f"✅ تم تجهيز طلبك باسم: **{full_name}** بنجاح!")
                st.markdown(f"""
                <div style="text-align:center; margin-top:15px;">
                    <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                        <div style="background-color:#10B981; color:#FFFFFF; padding:16px 24px; border-radius:16px; font-weight:800; font-size:17px; box-shadow:0 8px 20px rgba(16, 185, 129, 0.3);">
                            📲 اضغط هنا لفتح واتساب وإرسال الطلب الآن إلى 0784803429
                        </div>
                    </a>
                </div>
                """, unsafe_allow_html=True)