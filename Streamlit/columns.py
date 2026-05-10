import streamlit as st

# 页面基础配置
st.set_page_config(page_title="语料阅读看板", layout="wide")
st.markdown("""
    <style>
    /* 调整应用背景为温暖的米黄色 */
    .stApp {
        background-color: #FFFBE6;
    }
    /* 将所有的输入框和文本域改为大圆角 */
    .stTextArea textarea, .stTextInput input {
        border-radius: 20px !important;
        border: 2px solid #FFD700 !important;
    }
    /* 按钮定制：橙色系圆角按钮 */
    .stButton>button {
        background-color: #FF7F50;
        color: white;
        border-radius: 30px;
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)
# 侧边栏可以放置你的 API 配置，保持主界面简洁
with st.sidebar:
    st.header("⚙️ 工具配置")
    # 可以预留之前使用的 TMT API 密钥输入
    secret_key = st.text_input("APIKey", type="password")

# 主界面布局
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("输入语料")
    # 使用 form 避免每打一个字都触发 API 请求
    with st.form("translate_form"):
        text_input = st.text_area("粘贴中文内容：", height=300)
        submit = st.form_submit_button("开始处理")

with col2:
    st.subheader("分析结果")
    if submit and text_input:
        # 这里接入你之前的翻译函数
        st.info("正在处理中...")
        # 示例输出
        st.write("### 英文翻译")
        st.success("这里显示 TMT 接口返回的翻译结果")