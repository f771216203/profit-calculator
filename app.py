import streamlit as st

st.set_page_config(page_title="利潤與售價計算器", layout="wide")
st.title("💹 利潤與售價計算器")

currency_symbol = "¥"  # 固定使用人民幣

# --- 成本參數 ---
st.subheader("成本參數")
purchase_cost = st.number_input(f"採購價 ({currency_symbol})", min_value=0.0, value=150.0, step=1.0, format="%f")
fee_rate = 0.03  # 固定信用卡手續費3%
packaging = st.number_input(f"包裝費/件 ({currency_symbol})", min_value=0.0, value=5.0, step=0.5, format="%f")

# 運費輸入：每公斤價格與公斤數，若未填則使用預設
shipping_per_kg = st.number_input(f"運費每公斤價格 ({currency_symbol})", min_value=0.0, value=12.0, step=0.1, format="%f")
shipping_weight = st.number_input("運送重量 (公斤)", min_value=0.0, value=0.3, step=0.01, format="%f")
shipping = shipping_per_kg * shipping_weight

# 平台費用比例固定16.5%
platform_fee_rate = 0.165

# 基本成本 = 採購價加上信用卡手續費 + 包裝費 + 運費
base_cost = purchase_cost * (1 + fee_rate) + packaging + shipping

# --- 左右分欄 ---
col1, col2 = st.columns(2)

# 左側: 輸入採購價與利潤率
with col1:
    st.subheader("輸入採購價與利潤率")
    profit_margin_input = st.number_input("目標利潤率 (%)", min_value=0.0, value=30.0, step=0.1, format="%f", key="left_margin")
    selling_price_left = base_cost / (1 - platform_fee_rate) * (1 + profit_margin_input / 100)
    platform_fee_display = selling_price_left * platform_fee_rate  # 平台費用按售價計算
    total_cost_left = base_cost + platform_fee_display  # 總成本含平台費用
    st.markdown(f"<h1 style='color:green'>售價: {currency_symbol}{selling_price_left:,.2f}</h1>", unsafe_allow_html=True)
    st.write(f"總成本 (含平台費用): {currency_symbol}{total_cost_left:,.2f}")
    st.write(f"利潤率: {profit_margin_input:.2f}%")
    st.write(f"包裝費: {currency_symbol}{packaging:,.2f}")
    st.write(f"運費: {currency_symbol}{shipping:,.2f}")
    st.write(f"信用卡手續費: {currency_symbol}{purchase_cost * fee_rate:,.2f}")
    st.write(f"平台費用 (16.5%): {currency_symbol}{platform_fee_display:,.2f}")

# 右側: 輸入採購價與售價
with col2:
    st.subheader("輸入採購價與售價")
    selling_price_input = st.number_input(f"售價 ({currency_symbol})", min_value=0.0, value=299.0, step=0.1, format="%f", key="right_price")
    platform_fee_display_right = selling_price_input * platform_fee_rate  # 平台費用隨售價變動
    total_cost_right = base_cost + platform_fee_display_right  # 總成本含平台費用
    profit_margin_right = (selling_price_input - total_cost_right) / total_cost_right * 100  # 利潤率按總成本計算
    st.write(f"總成本 (含平台費用): {currency_symbol}{total_cost_right:,.2f}")
    st.write(f"售價: {currency_symbol}{selling_price_input:,.2f}")
    st.write(f"利潤率: {profit_margin_right:.2f}%")
    st.write(f"包裝費: {currency_symbol}{packaging:,.2f}")
    st.write(f"運費: {currency_symbol}{shipping:,.2f}")
    st.write(f"信用卡手續費: {currency_symbol}{purchase_cost * fee_rate:,.2f}")
    st.write(f"平台費用 (16.5%): {currency_symbol}{platform_fee_display_right:,.2f}")