# Demo File For Streamlit Basics 
import streamlit as st
import numpy as np
import pandas as pd

# Section1: formatted text elements
st.title("Streamlit Examples - know Basic Elements")
st.header("Header")
st.subheader("Sub Header")

st.text("This is a text")
st.markdown("__This__ is a _**markdown**_")
st.caption("This is a caption")
st.code("print('Hello, World!')", language="python", line_numbers=True)    
st.latex(r'''This\:is\:\LaTeX\:equation: e^{i\pi} + 1 = 0 ''')

with st.echo():
    st.write("This is an echo")

with st.chat_message(name="user"):
    st.write("This is a user chat message")
with st.chat_message(name="assistant"):
    st.write("This is a bot chat message")
    
# Section2: data display elements
df = pd.DataFrame(
    {
        "Ch. #": [1, 2, 3, 4, 5],
        "Title": [
            "Introduction to Streamlit",
            "Setting up the Development Environment",
            "Creating and Deploying Your First Streamlit App",
            "Exploring Streamit's Flow and Architecture",
            "Persisting Data and State Using Session State",
        ],
        "Rating": [3, 3, 3, 3, 3],
    },
)

st.write("This is a static table")
st.table(df)

st.write("This is an interactive table")
st.dataframe(df)

st.write("This is an editable table")
edited_df = st.data_editor(df)

st.write(
    f"Highest rated chapter: __{edited_df['Title'][edited_df['Rating'].idxmax()]}__"
)

st.metric(
    "__Average Rating__",
    edited_df["Rating"].mean(),
    edited_df["Rating"].mean() - df["Rating"].mean(),
)

# Section3: chart elements
st.header("给大家画一些漂亮的图表吧！")

chart_data = pd.DataFrame(np.random.randn(50, 2), columns=["LAT", "LON"])

lcol, rcol = st.columns(2)

lcol.write("Scatter plot")
lcol.scatter_chart(chart_data)

rcol.write("Area chart")
rcol.area_chart(chart_data)

lcol.write("Bar chart")
lcol.bar_chart(chart_data)

rcol.write("Map")
rcol.map(chart_data + [48, 9])

# Section4: input widgets
lcol, rcol = st.columns(2)

checkbox = lcol.checkbox("This is a checkbox")
lcol.write(f"Value of checkbox: {checkbox}")

toggle = rcol.toggle("This is a toggle")
rcol.write(f"Value of toggle: {toggle}")

color = lcol.color_picker("This is a color picker")
lcol.write(f"Value of color picker: {color}")

multiselect = rcol.multiselect(
    "This is a multiselect", ["Option 1", "Option 2", "Option 3"]
)
rcol.write(f"Value of multiselect: {multiselect}")

radio = lcol.radio(
    "This is a radio",
    ["Option 1", "Option 2", "Option 3"],
    horizontal=True,
)
lcol.write(f"Value of radio: {radio}")

select_slider = rcol.slider(
    "This is a slider",
    value=(0, 10),
)
rcol.write(f"Value of slider: {select_slider}")

select_slider = lcol.select_slider(
    "This is a select slider",
    ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
    value=["Option 1", "Option 3"],
)
lcol.write(f"Value of select slider: {select_slider}")

date = rcol.date_input("This is a date input")
rcol.write(f"Value of date input: {date}")

time = lcol.time_input("This is a time input")
lcol.write(f"Value of time input: {time}")

text_area = rcol.text_area("This is a text area")
rcol.write(f"Value of text area: {text_area}")

chat_input = lcol.chat_input()
lcol.write(f"Value of chat input: {chat_input}")


# Section5：media elements
st.image("https://static.streamlit.io/examples/dog.jpg", caption="A cute dog image")

st.header("🎵 播放本地音频文件")


st.header("🎬 播放本地视频文件")

# 使用 st.file_uploader() 让用户上传视频文件
uploaded_video = st.file_uploader(
    "请在此处上传您的视频文件 (MP4, MOV, AVI)...", 
    type=['mp4', 'mov', 'avi']
)

if uploaded_video is not None:
    # 直接将上传的文件对象传递给 st.video
    st.video(uploaded_video)

# 使用 st.file_uploader() 让用户上传音频文件
uploaded_audio = st.file_uploader(
    "请在此处上传您的音频文件...", 
    type=['mp3','mp4', 'wav', 'ogg']
)

if uploaded_audio is not None:
    # 直接将上传的文件对象传递给 st.audio
    st.audio(uploaded_audio, format='mp4')

# Section6: layout elements


st.title("Streamlit 布局元素示例")

# 侧边栏示例
with st.sidebar:
    st.header("侧边栏")
    st.radio("选择一个选项", ["A", "B", "C"])
    st.text_input("侧边栏输入")

st.write("---")

# 多列布局示例
st.header("多列布局")
col1, col2, col3 = st.columns([1, 2, 1]) # 比例为 1:2:1

with col1:
    st.write("这是第一列")
    st.button("按钮 1")

with col2:
    st.write("这是第二列，宽度是其他列的两倍")
    st.selectbox("选择", ["苹果", "桃子","香蕉"])

with col3:
    st.write("这是第三列")
    st.checkbox("勾选我")

st.write("---")

# 选项卡布局示例
st.header("选项卡布局")
tab1, tab2 = st.tabs(["基本信息", "高级设置"])

with tab1:
    st.write("这里是基本信息")
    st.text_input("你的名字")

with tab2:
    st.write("这里是高级设置")
    st.slider("设置参数", 0, 100, 50)

st.write("---")

# 可展开/收缩器示例
st.header("可展开/收缩器")
with st.expander("点击查看更多信息"):
    st.write("这是隐藏在可展开区域中的内容。")
    st.info("一些额外的提示。")

st.write("---")

# 容器示例
st.header("容器")
with st.container():
    st.write("这个区域在一个容器里。")
    st.line_chart([1, 2, 3, 4, 5])
    st.write("容器可以帮助你组织内容。")

# 表单示例
st.header("表单")
with st.form("my_form"):
    st.write("请填写以下信息")
    name = st.text_input("姓名")
    email = st.text_input("邮箱")
    submitted = st.form_submit_button("提交")
    if submitted:
        st.success(f"提交成功！姓名: {name}, 邮箱: {email}")
        
st.subheader("Creating widget using `column` object")
text1 = "在Streamlit中，布局元素 (Layout Elements) 是用来帮助您组织和排列应用程序中内容的工具。"
text2 = "利用Claude Code的原生能力，构建一个低成本、高可控、专业分工的多AI协作框架。"

with st.echo():
    col1, col2 = st.columns(2)

    col1.write("Column 1")
    col1.write(text1)

    col2.write("Column 2")
    col2.write(text2)

st.subheader("Creating widgets using `column` as context manager")

with st.echo():
    col1, col2 = st.columns(2)

    with col1:
        st.write("Column 1")
        st.write(text1)

    with col2:
        st.write("Column 2")
        st.write(text2)
        

with st.echo():
    image_url = "https://static.streamlit.io/examples/cat.jpg"

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Without container")
        st.image(image_url, width=250)

    with col2:
        with st.container(height=300):
            st.subheader("With container")
            st.image(image_url, width=250)
            
            
# Section7：state elements
st.title("Streamlit Session State 示例")

# 1. 初始化 session_state 中的值（如果不存在）
if 'count' not in st.session_state:
    st.session_state.count = 0

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# 2. 从 session_state 获取并显示当前值
st.write(f"当前的计数是: {st.session_state.count}")

# 3. 通过按钮更新 session_state 中的值
if st.button("增加计数"):
    st.session_state.count += 1
    st.write("计数已增加！") # 这会在重新运行后显示

# 4. 小部件与 session_state 联动（通过 key 参数）
# 当用户在 text_input 中输入时，st.session_state.user_name 会自动更新
st.session_state.user_name = st.text_input(
    "请输入您的名字:",
    value=st.session_state.user_name, # 使用 session_state 中的值作为初始值
    key="name_input" # 指定 key，Streamlit 会自动将其值存储在 st.session_state["name_input"]
)

# 5. 显示用户输入的名字
st.write(f"您输入的名字是: {st.session_state.user_name}")

# 6. 另一个按钮，直接读取 session_state
if st.button("重置计数"):
    st.session_state.count = 0
    st.session_state.user_name = "" # 也可以重置其他状态
    st.rerun() # 强制 Streamlit 重新运行整个脚本，以便立即更新显示
    
    
with st.echo():
    st.success("This is a success message", icon=":material/check_circle:")
    st.info("This is an info message", icon=":material/info:")
    st.warning("This is a warning message", icon=":material/warning:")
    st.error("This is an error message", icon=":material/error:")
    st.exception(RuntimeError("This is an exception"))

    
    
with st.echo():
    from time import sleep

    with st.status("Becoming a Streamlit master...", expanded=True) as status:
        st.write("Reading this book...")
        sleep(3)
        st.write("Running the examples...")
        sleep(3)
        st.write("Practicing what I've learned...")
        status.update(
            label="I am now a Streamlit master!", state="complete", expanded=False
        )
    

with st.echo():
    import time

    my_bar = st.progress(0, text="Starting...")

    for percent_complete in range(100):
        my_bar.progress(
            percent_complete + 1,
            text="Done ✅"
            if percent_complete + 1 == 100
            else f"Progress: {percent_complete+1}%",
        )
        time.sleep(0.01)
    time.sleep(1)

    st.button("Rerun")
    

st.title("小部件回调 (Widget Callbacks) 示例")

# 1. 定义一个回调函数
# 这个函数会在 'temperature_c' 小部件的值改变时被自动调用
def convert_temperature():
    """当摄氏度输入框的值改变时，计算华氏度并存入session_state。"""
    st.session_state.temperature_f = st.session_state.temperature_c * 9/5 + 32
    print(f"回调函数被触发了！新的摄氏度是: {st.session_state.temperature_c}")

# 2. 初始化 session_state
if 'temperature_c' not in st.session_state:
    st.session_state.temperature_c = 0.0
if 'temperature_f' not in st.session_state:
    st.session_state.temperature_f = 32.0 # 0°C 对应的华氏度


# 3. 创建小部件，并绑定回调函数
# 当用户改变这个输入框的值时，`convert_temperature` 函数会被调用
st.number_input(
    "摄氏度",
    key="temperature_c",
    on_change=convert_temperature  # 在这里绑定回调！
)

# 4. 在主代码中，我们只负责显示结果，不再关心计算逻辑
st.write(f"计算出的华氏度是: {st.session_state.temperature_f:.2f}")


st.info("观察您的终端，每次改变摄氏度的值，您都会看到一条来自回调函数的打印信息。")
