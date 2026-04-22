import streamlit as st


# Set the page title and layout before rendering the rest of the app.
# This is the page setup step, not a widget step.
st.set_page_config(page_title="Understanding Streamlit Keys", layout="wide")

st.caption("`st.set_page_config` controls the browser tab title and the page layout.")

st.title("Understanding Streamlit `key`")

st.write(
    "A Streamlit key is a unique name for a widget. "
    "Use it when you need Streamlit to tell widgets apart or when you want to read and keep a widget value in `st.session_state`."
)

st.info(
    "A good mental model: the label is what the user sees, and the key is the internal ID Streamlit uses."
)

st.header("Quick idea: key vs session_state")
st.write(
    "Think of `key` as the widget's ID card. Streamlit uses it to tell widgets apart. "
    "Think of `st.session_state` as the app's short-term memory. It keeps values during reruns."
)

st.code(
    '''st.text_input("Your name", key="user_name")

st.write(st.session_state["user_name"])''',
    language="python",
)

st.caption(
    "When a widget has a key, Streamlit stores its value in `st.session_state` under that key."
)

if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if st.button("Increase counter", key="increase_counter_button"):
    st.session_state.click_count += 1

st.write(f"Counter value: {st.session_state.click_count}")

st.code(
    '''if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if st.button("Increase counter", key="increase_counter_button"):
    st.session_state.click_count += 1

st.write(f"Counter value: {st.session_state.click_count}")''',
    language="python",
)


st.header("1. Same label, different meaning")
st.write(
    "When you place similar widgets on one page, give each widget its own key. "
    "That way, Streamlit can keep their values separate."
)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Example: two buttons")
    st.code(
        '''if st.button("Preview report", key="preview_report_button"):
    st.write("Previewing the report")

if st.button("Export report", key="export_report_button"):
    st.write("Exporting the report")''',
        language="python",
    )
    preview_clicked = st.button("Preview report", key="preview_report_button")
    export_clicked = st.button("Export report", key="export_report_button")

    if preview_clicked:
        st.success("Preview report button clicked")

    if export_clicked:
        st.success("Export report button clicked")

with right_col:
    st.subheader("Why the key matters")
    st.write(
        "If you later change the page and add more widgets, the key prevents Streamlit from confusing one widget with another."
    )
    st.write(
        "This is especially useful when labels are repeated or when widgets are created dynamically."
    )


st.header("2. Repeating widgets in a loop")
st.write(
    "If you create multiple input boxes in a loop, each one needs a different key. "
    "A common pattern is to use the loop index in the key."
)

names = ["Alice", "Bob", "Carol"]
entered_names = []

st.code(
    '''names = ["Alice", "Bob", "Carol"]
entered_names = []

for index, default_name in enumerate(names):
    name = st.text_input(
        f"Name {index + 1}",
        value=default_name,
        key=f"name_input_{index}",
    )
    entered_names.append(name)''',
    language="python",
)

for index, default_name in enumerate(names):
    name = st.text_input(
        f"Name {index + 1}",
        value=default_name,
        key=f"name_input_{index}",
    )
    entered_names.append(name)

st.write("Current values:", entered_names)


st.header("3. Form fields that you want to read later")
st.write(
    "Form widgets often use keys because you may want to collect several values and use them after the user submits the form."
)

with st.form("report_form"):
    st.write("Fill in the form and press Submit")
    report_name = st.text_input("Report name", key="report_name_input")
    report_owner = st.text_input("Owner", key="report_owner_input")
    include_summary = st.checkbox("Include summary", key="include_summary_checkbox")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Form submitted")
    st.write("Report name:", report_name)
    st.write("Owner:", report_owner)
    st.write("Include summary:", include_summary)

st.code(
    '''with st.form("report_form"):
    report_name = st.text_input("Report name", key="report_name_input")
    report_owner = st.text_input("Owner", key="report_owner_input")
    include_summary = st.checkbox("Include summary", key="include_summary_checkbox")
    submitted = st.form_submit_button("Submit")''',
    language="python",
)


st.header("4. Dynamic widgets based on data")
st.write(
    "If your page creates widgets from a list or dataset, build the key from the item name. "
    "This makes each widget stable and easy to identify."
)

features = ["speed", "cost", "quality"]
feature_scores = {}

st.code(
    '''features = ["speed", "cost", "quality"]
feature_scores = {}

for feature in features:
    feature_scores[feature] = st.slider(
        f"Score for {feature}",
        min_value=0,
        max_value=10,
        value=5,
        key=f"feature_score_{feature}",
    )''',
    language="python",
)

for feature in features:
    feature_scores[feature] = st.slider(
        f"Score for {feature}",
        min_value=0,
        max_value=10,
        value=5,
        key=f"feature_score_{feature}",
    )

st.write("Feature scores:", feature_scores)


st.header("5. Reading widget values from session state")
st.write(
    "When a widget has a key, Streamlit saves its value in `st.session_state[key]`. "
    "That is useful when you want to inspect or reuse the value later."
)

st.code(
    '''st.text_input("Your name", key="user_name")
st.write(st.session_state["user_name"])''',
    language="python",
)

st.text_input("Your name", key="user_name")
st.write("Value stored in session state:", st.session_state["user_name"])


st.header("6. Callback example: update one value when another changes")
st.write(
    "A callback is a small function Streamlit runs automatically when a widget changes. "
    "This is useful when one field should update another field right away."
)


def convert_name_to_upper() -> None:
    st.session_state.upper_name = st.session_state.lower_name.upper()


if "lower_name" not in st.session_state:
    st.session_state.lower_name = "streamlit"

if "upper_name" not in st.session_state:
    st.session_state.upper_name = st.session_state.lower_name.upper()

st.text_input(
    "Type a name in lowercase",
    key="lower_name",
    on_change=convert_name_to_upper,
)

st.write(f"Uppercase version: {st.session_state.upper_name}")

st.code(
    '''def convert_name_to_upper() -> None:
    st.session_state.upper_name = st.session_state.lower_name.upper()

st.text_input(
    "Type a name in lowercase",
    key="lower_name",
    on_change=convert_name_to_upper,
)''',
    language="python",
)


st.header("7. Mirrored widgets: one value, two views")
st.write(
    "Sometimes you want two widgets to show the same value in different places. "
    "You can keep one source of truth in `st.session_state` and mirror it into another widget."
)


def sync_city_name() -> None:
    st.session_state.city_copy = st.session_state.city_main


if "city_main" not in st.session_state:
    st.session_state.city_main = "Stuttgart"

if "city_copy" not in st.session_state:
    st.session_state.city_copy = st.session_state.city_main

left_city, right_city = st.columns(2)

with left_city:
    st.text_input(
        "Main city field",
        key="city_main",
        on_change=sync_city_name,
    )

with right_city:
    st.text_input("Mirror city field", key="city_copy")

st.write(f"Main value: {st.session_state.city_main}")
st.write(f"Mirror value: {st.session_state.city_copy}")

st.code(
    '''def sync_city_name() -> None:
    st.session_state.city_copy = st.session_state.city_main

st.text_input("Main city field", key="city_main", on_change=sync_city_name)
st.text_input("Mirror city field", key="city_copy")''',
    language="python",
)


st.header("8. Reset button: clear the stored values")
st.write(
    "A reset button is useful when you want the user to start over. "
    "You clear the values in `st.session_state` and then rerun the app."
)


def reset_demo_values() -> None:
    st.session_state.click_count = 0
    st.session_state.lower_name = "streamlit"
    st.session_state.upper_name = "STREAMLIT"
    st.session_state.city_main = "Stuttgart"
    st.session_state.city_copy = "Stuttgart"


st.button("Reset demo values", key="reset_demo_values_button", on_click=reset_demo_values)

st.code(
    '''def reset_demo_values() -> None:
    st.session_state.click_count = 0
    st.session_state.lower_name = "streamlit"
    st.session_state.upper_name = "STREAMLIT"
    st.session_state.city_main = "Stuttgart"
    st.session_state.city_copy = "Stuttgart"


st.button("Reset demo values", key="reset_demo_values_button", on_click=reset_demo_values)

st.code(
    '''def reset_demo_values() -> None:
    st.session_state.click_count = 0
    st.session_state.lower_name = "streamlit"
    st.session_state.upper_name = "STREAMLIT"
    st.session_state.city_main = "Stuttgart"
    st.session_state.city_copy = "Stuttgart"

st.button("Reset demo values", key="reset_demo_values_button", on_click=reset_demo_values)''',
    language="python",
)


st.header("Rule of thumb")
st.success(
    "Use a key when you have repeated widgets, dynamic widgets, forms, or when you need to read the widget value from session state."
)
