import streamlit as st
from site_class_reference import render_site_class_table

st.set_page_config(layout="centered")
st.title("Site Class Determination - IS 1893 : 2025")

# ---------------- TOP INPUTS ----------------

col1, col2 = st.columns(2)

with col1:
    depth = st.number_input(
        "Depth of Influence (m)",
        min_value=0.001,
        value=1.0,
        step=0.1
    )

with col2:
    num_layers = st.number_input(
        "Number of Soil Layers",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

st.divider()

# ---------------- SESSION INIT ----------------

if "layers_input" not in st.session_state:
    st.session_state.layers_input = []

if len(st.session_state.layers_input) != int(num_layers):
    st.session_state.layers_input = [
        {
            "thickness": 1.0,
            "soil_type": "Saturated Sands",
            "fines": "Yes",
            "n_value": 10,
            "vs_value": 180.0
        }
        for _ in range(int(num_layers))
    ]

# ---------------- FORM ----------------

with st.form("soil_form"):

    header = st.columns([1,1,2,1,1,1])
    header[0].markdown("**Layer**")
    header[1].markdown("**Thickness (m)**")
    header[2].markdown("**Soil Type**")
    header[3].markdown("**Fines < 15%**")
    header[4].markdown("**(N₁)₆₀**")
    header[5].markdown("**Vₛᵢ (m/s)**")

    updated_layers = []

    for i in range(int(num_layers)):

        row = st.columns([1,1,2,1,1,1])
        row[0].write(f"Layer {i+1}")

        thickness = row[1].number_input(
            "Enter ti",
            min_value=0.001,
            value=float(st.session_state.layers_input[i]["thickness"]),
            step=0.1,
            key=f"th_{i}"
        )

        soil_type = row[2].selectbox(
            "Select Soil Type",
            ["Saturated Sands", "Dry Sands", "Clays", "Others"],
            index=["Saturated Sands", "Dry Sands", "Clays", "Others"]
            .index(st.session_state.layers_input[i]["soil_type"]),
            key=f"soil_{i}"
        )

        disable_fines = soil_type in ["Clays", "Others"]

        fines = row[3].selectbox(
            "Is Fines < 15%",
            ["Yes", "No"],
            index=0,
            key=f"fines_{i}",
            disabled=disable_fines
        )

        disable_n = soil_type == "Others"

        n_value = row[4].number_input(
            "Enter (N₁)₆₀",
            min_value=1,
            value=int(st.session_state.layers_input[i]["n_value"]),
            step=1,
            key=f"n_{i}",
            disabled=disable_n
        )

        # Vsi activation rule
        activate_vs = soil_type == "Others" or n_value < 10

        vs_value = row[5].number_input(
            "Enter Vₛᵢ",
            min_value=0.001,
            value=float(st.session_state.layers_input[i]["vs_value"]),
            step=1.0,
            key=f"vs_{i}",
            disabled=not activate_vs
        )

        updated_layers.append({
            "thickness": thickness,
            "soil_type": soil_type,
            "fines": "" if disable_fines else fines,
            "n_value": 0 if disable_n else n_value,
            "vs_value": vs_value if activate_vs else 0.0
        })
    total_thickness = sum(layer["thickness"] for layer in st.session_state.layers_input)
    valid_depth = total_thickness >= depth

    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

    with btn_col2:
        submitted = st.form_submit_button(
            "Calculate",
            disabled=not valid_depth,
            use_container_width=True
        )


    if submitted:
        st.session_state.layers_input = updated_layers
        st.success("Inputs saved successfully.")

# ---------------- VALIDATION ----------------


if not valid_depth:
    st.warning("Total thickness must be ≥ Depth of Influence.")

# ---------------- BUTTONS ----------------
# Centered button row 
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

with btn_col2:
    calculate_clicked = st.button(
        "Write Report",
        disabled=not valid_depth,
        use_container_width=True
    )

render_site_class_table()


# ---------------- CALCULATION ----------------

# if calculate_clicked:

#     numerator = sum(layer["thickness"] for layer in st.session_state.layers_input)
#     denominator = sum(
#         layer["thickness"] / layer["vs_value"]
#         for layer in st.session_state.layers_input
#         if layer["vs_value"] > 0
#     )

#     weighted_vs = numerator / denominator if denominator else 0

#     if weighted_vs >= 1500:
#         site_class = "A"
#     elif weighted_vs >= 760:
#         site_class = "B"
#     elif weighted_vs >= 360:
#         site_class = "C"
#     elif weighted_vs >= 180:
#         site_class = "D"
#     else:
#         site_class = "E"

#     st.metric("Weighted Average Vs (m/s)", round(weighted_vs, 2))
#     st.success(f"Site Class: {site_class}")
