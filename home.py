import streamlit as st

st.set_page_config(
    page_title="酒店收益看板",
    page_icon="🏨",
    layout="wide",
)

st.title("🏨 酒店收益与取消率分析")
st.caption("面向酒店收益经理的决策看板入口")

st.markdown(
    """
    这是一个多页面 Streamlit 应用。

    - 在左侧导航栏中选择 `app` 页面，查看酒店预订取消率看板
    - 通过数据趋势分析，识别高取消率渠道与时段
    - 支持按酒店类型与市场细分维度筛选
    """
)

st.info("提示：启动时请运行 `streamlit run home.py`，然后从左侧页面列表进入 `app` 页面。")
