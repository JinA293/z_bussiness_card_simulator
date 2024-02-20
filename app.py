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

# 初期色の定義
DEFAULT_COLORS = ['#c6171e', '#221a18', '#0e3a78', '#f4aa1b']
PLACE_NAMES = ["左上", "右上", "左下", "右下"]

# カラーコードの入力欄を生成する関数
def create_color_inputs():
    return [st.text_input(f"{PLACE_NAMES[i]} のオブジェクトカラーコード", value=st.session_state.colors[i], key=f"color_{i}") for i in range(4)]

# カラーコードを反映するボタンを生成する関数
def create_apply_button():
    if st.button("カラーコードを反映"):
        st.session_state.colors = color_inputs

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

# メインの処理
if __name__ == "__main__":
    # セッションステートの初期化
    if 'colors' not in st.session_state:
        st.session_state.colors = DEFAULT_COLORS

    # カラーコードの入力欄を生成
    color_inputs = create_color_inputs()

    # カラーコードを反映するボタンを生成
    create_apply_button()

    # 形状を描画
    draw_shapes()

# githubのURLを下部中央に追加する
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://github.com/JinA293/z_bussiness_card_simulator" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
