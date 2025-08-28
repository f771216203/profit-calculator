import streamlit as st

st.set_page_config(page_title="利潤與售價計算器", layout="wide")
st.title("💹 利潤與售價計算器")

currency_symbol = "¥"  # 固定使用人民幣

# --- 成本參數 ---
st.subheader("成本參數")
purchase_cost_str = st.text_input(f"採購價 ({currency_symbol})", value="100.0", key="purchase_cost")
packaging_str = st.text_input(f"包裝費/件 ({currency_symbol})", value="5.0", key="packaging")
shipping_per_kg_str = st.text_input(f"運費每公斤價格 ({currency_symbol})", value="12.0", key="shipping_per_kg")
shipping_weight_str = st.text_input("運送重量 (公斤)", value="0.3", key="shipping_weight")

# 轉換輸入為浮點數
try:
    purchase_cost = float(purchase_cost_str)
except:
    purchase_cost = 100.0
try:
    packaging = float(packaging_str)
except:
    packaging = 5.0
try:
    shipping_per_kg = float(shipping_per_kg_str)
except:
    shipping_per_kg = 12.0
try:
    shipping_weight = float(shipping_weight_str)
except:
    shipping_weight = 0.3

shipping = shipping_per_kg * shipping_weight
fee_rate = 0.03  # 固定信用卡手續費3%
platform_fee_rate = 0.165

# 基本成本 = 採購價加上信用卡手續費 + 包裝費 + 運費
base_cost = purchase_cost * (1 + fee_rate) + packaging + shipping

# --- 左右分欄 ---
col1, col2 = st.columns(2)

# 左側: 輸入利潤率計算售價
with col1:
    st.subheader("輸入利潤率計算售價")
    profit_margin_input_str = st.text_input("目標利潤率 (%)", value="30.0", key="left_margin")
    try:
        profit_margin_input = float(profit_margin_input_str)
    except:
        profit_margin_input = 30.0

    # 售價公式：售價 = 基本成本 * (1 + 利潤率) / (1 - 平台費率)
    selling_price_left = base_cost * (1 + profit_margin_input / 100) / (1 - platform_fee_rate)
    platform_fee_display = selling_price_left * platform_fee_rate
    total_cost_left = base_cost + platform_fee_display

    st.markdown(f"<h1 style='color:yellow'>售價: {currency_symbol}{selling_price_left:,.2f}</h1>", unsafe_allow_html=True)
    st.write(f"總成本 (含平台費用): {currency_symbol}{total_cost_left:,.2f}")
    st.write(f"利潤率: {profit_margin_input:.2f}%")
    st.write(f"包裝費: {currency_symbol}{packaging:,.2f}")
    st.write(f"運費: {currency_symbol}{shipping:,.2f}")
    st.write(f"信用卡手續費: {currency_symbol}{purchase_cost * fee_rate:,.2f}")
    st.write(f"平台費用 (16.5%): {currency_symbol}{platform_fee_display:,.2f}")

# 右側: 輸入售價計算利潤率
with col2:
    st.subheader("輸入售價計算利潤率")
    selling_price_input_str = st.text_input(f"售價 ({currency_symbol})", value="299.0", key="right_price")
    try:
        selling_price_input = float(selling_price_input_str)
    except:
        selling_price_input = 299.0

    platform_fee_display_right = selling_price_input * platform_fee_rate
    total_cost_right = base_cost + platform_fee_display_right
    profit_margin_right = (selling_price_input - total_cost_right) / base_cost * 100  # 利潤率按基本成本計算

    st.markdown(f"<h1 style='color:yellow'>利潤率: {profit_margin_right:.2f}%</h1>", unsafe_allow_html=True)
    st.write(f"總成本 (含平台費用): {currency_symbol}{total_cost_right:,.2f}")
    st.write(f"售價: {currency_symbol}{selling_price_input:,.2f}")
    st.write(f"包裝費: {currency_symbol}{packaging:,.2f}")
    st.write(f"運費: {currency_symbol}{shipping:,.2f}")
    st.write(f"信用卡手續費: {currency_symbol}{purchase_cost * fee_rate:,.2f}")
    st.write(f"平台費用 (16.5%): {currency_symbol}{platform_fee_display_right:,.2f}")
