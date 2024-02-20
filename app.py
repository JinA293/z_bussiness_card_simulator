import streamlit as st

# CSSを使って各形状のスタイルと配置を定義します。
SHAPE_STYLE = """
<style>
div.shapes-container {
    display: grid;
    justify-content: center;
    grid-template-columns: auto auto;
    gap: 10px;
    # margin-top: 20px;
}
.shape-container {
    position: relative;
    width: 100px;
    height: 100px;
}
.shape {
    width: 100px;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
}
.shape.circle {
    border-radius: 50%;
}
.shape.triangle-up {
    # width: 0;
    height: 0;
    # border-left: 50px solid transparent;
    border-right: 100px solid transparent;
    border-top: 100px solid;
}
.shape.triangle-down {
    width: 0;
    height: 0;
    border-left: 100px solid transparent;
    # border-right: 50px solid transparent;
    border-bottom: 100px solid;
    position: absolute;
    top: 0;
}
.shape.square {
    display: inline-block;
}
</style>
"""

# StreamlitにCSSを追加します。
st.markdown(SHAPE_STYLE, unsafe_allow_html=True)

# 4つの色を管理するための変数を初期化します。
if 'colors' not in st.session_state:
    st.session_state.colors = ['#c6171e', '#221a18', '#0e3a78', '#f4aa1b']  # デフォルト色

place_list = ["左上", "右上", "左下", "右下"]

# カラーコードの入力欄を生成します。
color_codes = [st.text_input(f"{place_list[i]} のオブジェクトカラーコード", value=st.session_state.colors[i], key=f"color_{i}") for i in range(4)]

# 反映ボタンを配置します。このボタンは4つの色を全て反映します。
if st.button("カラーコードを反映"):
    st.session_state.colors = color_codes

# 形状を描画する関数
def draw_shapes():
    st.markdown(
        f"""
        <div class="shapes-container">
            <div class="shape-container">
                <div class="shape circle" style="background-color: {st.session_state.colors[0]};"></div>
            </div>
            <div class="shape-container">
                <div class="shape triangle-up" style="border-top-color: {st.session_state.colors[1]};"></div>
            </div>
            <div class="shape-container">
                <div class="shape triangle-down" style="border-bottom-color: {st.session_state.colors[2]};"></div>
            </div>
            <div class="shape-container">
                <div class="shape square" style="background-color: {st.session_state.colors[3]};"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# 形状を描画します。
draw_shapes()
