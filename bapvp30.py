import streamlit as st
import base64

# 必須最先呼叫
st.set_page_config(page_title="0.7 計算機", layout="centered")

# 將圖片讀成 base64
def get_base64_img(image_path):
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
    return b64_data

# 嵌入背景圖
bg_img = get_base64_img("28.png")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    div.block-container {{
        background-color: transparent;
        padding: 0;
    }}
    </style>
""", unsafe_allow_html=True)


# 以下是你的原本邏輯
with st.container():
    st.markdown("<div class='main-block'>", unsafe_allow_html=True)

    st.title("0.7 計算機")

    if "input_value" not in st.session_state:
        st.session_state.input_value = 66
    if "clicked_rank" not in st.session_state:
        st.session_state.clicked_rank = None

    def set_value_from_button(val):
        st.session_state.input_value = val

    input_val = st.number_input("請輸入目前排名", step=1, key="input_value")
    result = int(input_val * 0.7 // 1)
    st.markdown(f"### 計算結果： **{result}**")

    st.subheader("5票10名至少68內：68→47→32→22→15→10")

    for rank in range(max(result - 2, 0), input_val + 1):
        if rank == input_val or rank == 0:
            continue
        rank_result = int(rank * 0.7 // 1)
        if st.button(f"目標 {rank} → {rank_result}", key=f"btn_{rank}", on_click=set_value_from_button, args=(rank,)):
            break

    st.markdown("</div>", unsafe_allow_html=True)
